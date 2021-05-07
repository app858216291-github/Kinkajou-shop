# -*- coding: utf-8 -*-
from model.models import Product,Address
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
        token = request.headers.get('token')
        userid = IOUtil.verifyToken(token)
        return userid









