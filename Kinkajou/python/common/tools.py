# -*- coding: utf-8 -*-
import os

from bs4 import BeautifulSoup

from model.models import Product, Address, DocManger
from flask import session
import json,time,logging
import qrcode
from io import BytesIO
import datetime


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8');
        return json.JSONEncoder.default(self, obj)
class JsonUtil():
    @staticmethod
    def dumps(obj):
        return json.dumps(obj, cls=MyEncoder, ensure_ascii=False)
    @staticmethod
    def loads(jsonStr):
        return json.loads(jsonStr)

class IOUtil():
    ##请求转对象
    @staticmethod
    def request2Obj(obj,request):
        attrs =dir(obj)
        for attr in attrs:
            if request.args.get(attr) != None:
                setattr(obj,attr,request.args.get(attr))
        # dict = obj.__dict__
        # for i in dict:
        #     if request.args.get(i) != None:
        #         setattr(obj,i,request.args.get(i))
        return obj

    ##请求转查询条件
    @staticmethod
    def request2ObjFilters(obj, request):
        filters = set()
        attrs = dir(obj())
        for attr in attrs:
            if request.args.get(attr) != None:
                f = (getattr(obj, attr) == request.args.get(attr))
                filters.add(f)
        return filters

    ##生成订单号
    @staticmethod
    def orderNo():
        curr_time = datetime.datetime.now()
        time_str = curr_time.strftime("%Y%m%d%H%M%S")
        return time_str
        # return str(int(time.ctime()*1000))

    # 加密
    @staticmethod
    def enctry(s):
        k = 'djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd'
        encry_str = ""
        for i, j in zip(s, k):
            # i为字符，j为秘钥字符
            temp = str(ord(i) + ord(j)) + '_'  # 加密字符 = 字符的Unicode码 + 秘钥的Unicode码
            encry_str = encry_str + temp
        return encry_str

    # 解密
    @staticmethod
    def dectry(p):
        k = 'djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd'
        dec_str = ""
        for i, j in zip(p.split("_")[:-1], k):
            # i 为加密字符，j为秘钥字符
            temp = chr(int(i) - ord(j))  # 解密字符 = (加密Unicode码字符 - 秘钥字符的Unicode码)的单字节字符
            dec_str = dec_str + temp
        return dec_str

    # 生成token
    @staticmethod
    def createToken(userid):
        timestamp = int(round(time.time() ))+60*60*24*30
        token=str(userid)+','+str(timestamp)
        return IOUtil.enctry(token)

    # 验证token
    @staticmethod
    def verifyToken(token):
        token = IOUtil.dectry(token)
        try:
            tokenList=token.split(',')
            if int(tokenList[1])>int(round(time.time() )):
                return int(tokenList[0])
        except Exception as e:
            print(str(e))
            return -1
        return -1

    @staticmethod
    def logger(mgs):
        # logging.basicConfig(filemode="a", format="%(asctime)s %(name)s:%(levelname)s:%(message)s",
        #                     datefmt="%d-%M-%Y %H:%M:%S")
        # # logging.FileHandler(filename='example.log', encoding='utf-8')
        # filehandler = logging.FileHandler("test2.log", encoding='UTF-8')
        # logging.getLogger().setLevel(logging.INFO)
        # logging.getLogger().addHandler(filehandler)
        # logging.info(mgs)
        pass

    from io import BytesIO
    import qrcode
    @staticmethod
    def set_qrcode(data):
        """
        根据传入的url 生成 二维码对象
        :param url:
        :return:
        """
        qr = qrcode.QRCode(version=1,  # 二维码大小 1～40
                           error_correction=qrcode.constants.ERROR_CORRECT_L,  # 二维码错误纠正功能
                           box_size=10,  # 二维码 每个格子的像素数
                           border=4)  # 二维码与图片边界的距离

        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
        byte_io = BytesIO()
        img.save(byte_io, 'PNG')
        byte_io.seek(0)
        return byte_io
class shopUtil:
    @staticmethod
    def ifNull(obj):
        if obj==None:
            return True
        elif isinstance(obj, bytes):
            str= str(obj, encoding='utf-8')
            if str.strip(str)=="":
                return True
        return False

    @staticmethod
    def getUserFromRequest(request,model):
        token = request.headers.get('token')
        userid = IOUtil.verifyToken(token)
        user=model.get(userid)
        return user
    @staticmethod
    def getUserId(request):
        admin = request.args.get('admin')
        if admin !=None:
            return int(admin)
        token = request.headers.get('token')
        userid = IOUtil.verifyToken(token)
        return userid

class eMailUtil:
    @staticmethod
    def sendMail(to_addr=['370377860@qq.com'],title='kinkajou提醒邮件',content=""):
        from email.mime.text import MIMEText
        from email.header import Header
        from email.mime.multipart import MIMEMultipart
        import smtplib
        from_addr = 'kinkajou@126.com'  # 用来发送邮件的邮箱地址
        password = 'GEBOBPOEBUCFVWNR'  # 邮箱密码或者是授权密码
        # to_addr = []  # 目标邮箱地址
        # to_addr.pop('370377860@qq.com')
        smtp_server = 'smtp.126.com'  # 这里是新浪的SMTP服务器地址
        # 发送的信息格式
        content = MIMEText(content, 'plain', 'utf-8')
        msg = MIMEMultipart()
        msg['From'] = Header(from_addr)  # 定义发件人
        msg['Subject'] = Header(title, 'utf-8')  # 定义邮件名
        msg.attach(content)  # 加上邮件的内容
        result=""
        try:
            server = smtplib.SMTP(smtp_server,25)
            # server.connect(smtp_server, 25)  # 连接SMTP服务器
            server.set_debuglevel(1)  # 打印调试信息
            server.login(from_addr, password)  # 登陆邮箱
            aa=server.sendmail(from_addr, to_addr, msg.as_string())  # 发送邮件
            print("Send successfully!")
            result="Send successfully!"
        except smtplib.SMTPException as e:
            result="发送失败"
            print(str(e))
            print("发送失败")
        server.quit()  # 退出
        return result;
    ##10进制转成64进制
    @staticmethod
    def encode_b64(n):
        table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'
        result = []
        temp = int(n)
        if 0 == temp:
            result.append('0')
        else:
            while 0 < temp:
                result.append(table[temp % 64])
                temp = int(temp / 64)
        return ''.join([x for x in reversed(result)])

    ##64进制转成10进制
    @staticmethod
    def decode_b64(str):
        table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
                 "6": 6, "7": 7, "8": 8, "9": 9,
                 "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "g": 16,
                 "h": 17, "i": 18, "j": 19, "k": 20, "l": 21, "m": 22, "n": 23,
                 "o": 24, "p": 25, "q": 26, "r": 27, "s": 28, "t": 29, "u": 30,
                 "v": 31, "w": 32, "x": 33, "y": 34, "z": 35,
                 "A": 36, "B": 37, "C": 38, "D": 39, "E": 40, "F": 41, "G": 42,
                 "H": 43, "I": 44, "J": 45, "K": 46, "L": 47, "M": 48, "N": 49,
                 "O": 50, "P": 51, "Q": 52, "R": 53, "S": 54, "T": 55, "U": 56,
                 "V": 57, "W": 58, "X": 59, "Y": 60, "Z": 61,
                 "-": 62, "_": 63}
        result = 0
        for i in range(len(str)):
            result *= 64
            result += table[str[i]]
        return result
        ##64进制转成10进制

    @staticmethod
    def docManger(f,abspath,prepath,house="aliyun"):
        # 文件属性
        file = type('',(), {})()
        file.fileName = abspath
        file.prepath =prepath
        file.abspath = abspath
        # fsize = os.path.getsize(f)
        # fsize = fsize / float(1024 * 1024)
        # fsize=round(fsize, 2)

        docManger = DocManger()
        t = int(time.time() * 1000000)
        print(t)
        key = shopUtil.encode_b64(t)
        docManger.key = key


        docManger.title = f.filename
        docManger.type = f.content_type
        docManger.abspath=file.fileName
        docManger.prepath=file.prepath
        docManger.warehouse=house
        # docManger.size=fsize
        docManger.add()
        return docManger.key

# eMailUtil.sendMail( ['370377860@qq.com'] , 'Python SMTP 邮件测试')

class productInfo4html():
    @staticmethod
    def download_file(url, floder=''):
        url = url.replace('_60x60q90.jpg', '')
        isExists = os.path.exists(floder)
        # 判断结果
        if not isExists:
            os.makedirs(floder)
        print('Downloading %s' %url)
        local_filename = "static/1111111" + url.split('/')[-1]
        # local_filename=local_filename+'/aa/'
        # print('file_name:', local_filename)
        # filename like xxx.jpg
        import requests
        header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
        html = requests.get(url, headers=header).text
        r = requests.get(url, stream=True, headers=header)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    # 文件方法 将缓冲区文件立即写入文件
                    f.flush()

    @staticmethod
    def valid_img(src):
        return src.endswith('jpg')
    @staticmethod
    def getproductInfo(html):
        soup = BeautifulSoup(html)
        zhutu = soup.find('ul', id='J_UlThumb')
        xiangqing = soup.find('div', id='description')
        for img in zhutu.find_all('img', src=productInfo4html.valid_img):
            src = img['src']
            # print('src is',src)
            if not src.startswith('http'):
                src = 'http:' + src
                productInfo4html.download_file(src)






