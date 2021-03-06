# -*- coding: utf-8 -*-
import requests
from flask import Blueprint, render_template, redirect,request,jsonify,send_from_directory,url_for,send_file,session
from model.modelBase import Jsonfy

import setting
import xmltodict
import time
import json

from wechatpy.utils import random_string
wx = Blueprint('wx',__name__)
IMAGE_FOLDER  = 'static/upload/'


@wx.route('/index', methods=['POST','GET'])
def index():
    openid=request.args.get('openid')
    appid=setting.WeinXin.APP_ID
    timestamp=int(time.time())
    nonceStr=random_string(32)
    from wechatpy.client import WeChatClient
    # t=WeChatClient.jsapi.get_ticket()
    # signature=WeChatClient.jsapi.get_jsapi_signature()
    wc=WeChatClient(appid=setting.WeinXin.APP_ID,secret=setting.WeinXin.APP_SECRECT)
    tick=wc.jsapi.get_jsapi_ticket()
    print(tick)
    print(nonceStr)
    print(timestamp)
    signature=wc.jsapi.get_jsapi_signature(nonceStr, tick,timestamp,'http://h5.heshihuan.cn/')
    print(signature)
    # signature=wxjspay.get_jsapi_params(openid,price=1.1,orderNum='1203333333')['sign']

    config={}
    config['appid']=appid
    config['timestamp']=timestamp
    config['nonceStr']=nonceStr
    config['signature']=signature
    config['url']='http://www.heshihuan.cn/#/pages/product/product?id=6'
    return Jsonfy(data=config).__str__()



##http://127.0.0.1:5000/wx/mpPay?openid=oo0m04oxLhANWFBwMWezYRRRidzc
@wx.route('/mpPay', methods=['POST','GET'])
def mpPay():
    openid = request.args.get('openid')

    # wx=WX_PayToolUtil(APP_ID=setting.WeinXin.MP_APP_ID,MCH_ID=setting.WeinXin.MCH_ID,API_KEY=setting.WeinXin.API_KEY,NOTIFY_URL=setting.WeinXin.NOTIFY_URL)
    # res=wx.getPayUrl(orderid=IOUtil.orderNo(),openid=openid,goodsPrice=1)
    # pay = WeChatPay(appid=setting.WeinXin.MP_APP_ID, api_key=setting.WeinXin.API_KEY,sub_appid=setting.WeinXin.MP_APP_ID, mch_id=setting.WeinXin.MCH_ID)
    # res = pay.order.create(
    # trade_type="JSAPI",
    # body="εεζθΏ°",
    # total_fee=1,
    # notify_url=setting.WeinXin.NOTIFY_URL,
    # user_id=openid,
    # out_trade_no=IOUtil.orderNo())
    return Jsonfy(data=res).__str__()


@wx.route('/mpOpenId', methods=['POST','GET'])
def mpOpenId():
    code=request.args.get('code')
    parmas = {
        'appid': setting.WeinXin.MP_APP_ID,
        'secret': setting.WeinXin.MP_APP_SECRECT,
        'js_code': code,
        'grant_type': 'authorization_code'
    }

    url = 'https://api.weixin.qq.com/sns/jscode2session'
    r = requests.get(url, params=parmas)
    openid = r.json().get('openid', '')
    return Jsonfy(data=openid).__str__()



import requests
import hashlib
import xmltodict
import time
import random
import string



class WX_PayToolUtil():
    """ εΎ?δΏ‘ζ―δ»ε·₯ε· """

    def __init__(self, APP_ID, MCH_ID, API_KEY, NOTIFY_URL):
        self._APP_ID = APP_ID  # ε°η¨εΊID
        self._MCH_ID = MCH_ID  # # εζ·ε·
        self._API_KEY = API_KEY
        self._UFDODER_URL = "https://api.mch.weixin.qq.com/pay/unifiedorder"  # ζ₯ε£ιΎζ₯
        self._NOTIFY_URL = NOTIFY_URL  # εΌζ­₯ιη₯

    def generate_sign(self, param):
            '''ηζη­Ύε'''
            stringA = ''
            ks = sorted(param.keys())
            # εζ°ζεΊ
            for k in ks:
                stringA += (k + '=' + param[k] + '&')
            # ζΌζ₯εζ·KEY
            stringSignTemp = stringA + "key=" + self._API_KEY
            # md5ε ε―,δΉε―δ»₯η¨εΆδ»ζΉεΌ
            hash_md5 = hashlib.md5(stringSignTemp.encode('utf8'))
            sign = hash_md5.hexdigest().upper()
            return sign


    def getPayUrl(self, orderid, openid, goodsPrice, **kwargs):
        """εεΎ?δΏ‘ζ―δ»η«―εεΊθ―·ζ±οΌθ·εurl"""
        key = self._API_KEY
        nonce_str = ''.join(random.sample(string.letters + string.digits, 30))  # ηζιζΊε­η¬¦δΈ²οΌε°δΊ32δ½
        params = {
            'appid': self._APP_ID,  # ε°η¨εΊID
            'mch_id': self._MCH_ID,  # εζ·ε·
            'nonce_str': nonce_str,  # ιζΊε­η¬¦δΈ²
            "body": 'ζ΅θ―θ?’ε',  # ζ―δ»θ―΄ζ
            'out_trade_no': orderid,  # ηζηθ?’εε·
            'total_fee': str(goodsPrice),  # ζ δ»·ιι’
            'spbill_create_ip': "127.0.0.1",  # ε°η¨εΊδΈθ½θ·εε?’ζ·ipοΌwebη¨socektε?η°
            'notify_url': self._NOTIFY_URL,
            'trade_type': "JSAPI",  # ζ―δ»η±»ε
            "openid": openid,  # η¨ζ·id
         }
        # ηζη­Ύε
        params['sign'] = self.generate_sign(params)

        # python3δΈη§εζ³
        param = {'root': params}
        xml = xmltodict.unparse(param)
        response = requests.post(self._UFDODER_URL, data=xml.encode('utf-8'), headers={'Content-Type': 'text/xml'})
        # xml 2 dict
        msg = response.text
        xmlmsg = xmltodict.parse(msg)
        # 4. θ·εprepay_id
        if xmlmsg['xml']['return_code'] == 'SUCCESS':
            if xmlmsg['xml']['result_code'] == 'SUCCESS':
                prepay_id = xmlmsg['xml']['prepay_id']
                # ζΆι΄ζ³
                timeStamp = str(int(time.time()))
                # 5. δΊδΈͺεζ°
                data = {
                    "appId": self._APP_ID,
                    "nonceStr": nonce_str,
                    "package": "prepay_id=" + prepay_id,
                    "signType": 'MD5',
                    "timeStamp": timeStamp,
                }
                # 6. paySignη­Ύε
                paySign = self.generate_sign(data)
                data["paySign"] = paySign  # ε ε₯η­Ύε
                # 7. δΌ η»εη«―ηη­Ύεεηεζ°
                return data



class wxjsconfig:
    def index(self):
        """
        η₯θ―δΈ­εΏ
        :return:
        """
        id = self.get_argument('id', '')
        getSignPackage = self.getSignPackage()
        self.assign('getSignPackage', getSignPackage)
        self.display('knowledge/index.html')


    def getSignPackage(self):

        # θ·εΎjsapi_ticket
        jsapiTicket = self.getJsApiTicket()

        # ζ³¨ζ URL δΈε?θ¦ε¨ζθ·εοΌδΈθ½ hardcode.
        # protocol = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off' || $_SERVER['SERVER_PORT'] == 443) ? "https://" : "http://";
        # $url = "$protocol$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
        # θ·εε½ει‘΅ι’ηurl
        url = "{}://{}{}".format(self.request.protocol, self.request.host, self.request.uri)

        # θ·εtimestampοΌζΆι΄ζ³οΌ
        timestamp = int(time.time())
        # θ·εnoncestrοΌιζΊε­η¬¦δΈ²οΌ
        nonceStr = self.createNonceStr()

        # θΏιεζ°ηι‘ΊεΊθ¦ζη§ key εΌ ASCII η εεΊζεΊ
        string = "jsapi_ticket={}&noncestr={}&timestamp={}&url={}".format(jsapiTicket, nonceStr, timestamp, url)
        # εΎε°signature
        signature = hashlib.sha1(string).hexdigest();
        wxinfo = self.getwx()
        signPackage = {
            "appId": wxinfo['appid'],
            "nonceStr": nonceStr,
            "timestamp": timestamp,
            "url": url,
            "signature": signature,
            "rawString": string
        }

        return signPackage;


    def createNonceStr(self, length=16):
        # θ·εnoncestrοΌιζΊε­η¬¦δΈ²οΌ
        import random
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        str = "";
        for i in range(0, 16):
            str += chars[random.randint(0, len(chars) - 1):random.randint(0, len(chars) - 1) + 1]
        # for ($i = 0; $i < $length; $i++) {
        #   $str .= substr($chars, mt_rand(0, strlen($chars) - 1), 1);
        # }
        return str;


    def getJsApiTicket(self):

        # θ·εΎjsapi_ticket
        # θ·εΎjsapi_ticketδΉεοΌε°±ε―δ»₯ηζJS-SDKζιιͺθ―ηη­ΎεδΊ
        import urllib.request
        # jsapi_ticket εΊθ―₯ε¨ε±ε­ε¨δΈζ΄ζ°οΌδ»₯δΈδ»£η δ»₯εε₯ε°ζδ»ΆδΈ­εη€ΊδΎ
        # cookie('ticket',null);

        # θ·εaccess_token
        accessToken = self.accesstokens()
        # ε¦ζζ―δΌδΈε·η¨δ»₯δΈ URL θ·ε ticket
        # $url = "https://qyapi.weixin.qq.com/cgi-bin/get_jsapi_ticket?access_token=$accessToken";
        # θ·εjsapi_ticket
        url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={}&type=jsapi".format(accessToken)

        req = request.Request(url)
        res_data = request.urlopen(req)
        res = res_data.read()
        res = json.dumps(res)

        return str(res['ticket'])

##ε¬δΌε·εε€ειͺθ―
@wx.route('/token',methods=['GET','POST'])
def token():
    token = 'mytoken1'
    echostr = request.args.get('echostr')
    return echostr
    #return "8337549056785503916"
    print("θ―·ζ±θΏζ₯δΊ")
    import hashlib
    if request.method == 'GET':
        try:
            signature = request.args.get('signature')
            print(signature)
            timestamp = request.args.get('timestamp')
            print(timestamp)
            echostr = request.args.get('echostr')
            nonce = request.args.get('nonce')

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            if hashcode == signature:
                print("ζε")
                return echostr
            else:
                return ""
        except Exception:
            print("εΌεΈΈ")
            return ""





        print("1")
        signature = request.args.get('signature')
        print(signature)
        timestamp = request.args.get('timestamp')
        print(timestamp)
        echostr = request.args.get('echostr')
        nonce = request.args.get('nonce')
        print(nonce)
        openid = request.args.get('openid')
        session[request.args.get('openid')] = openid
        print("openθ·ε")
        print(openid)

        if len(request.args)==0:
            return "hello, this is handle view"
        list = [token, timestamp, nonce]
        list.sort()
        s = list[0]+list[1]+list[2]
        hashcode = hashlib.sha1(s.encode('utf-8')).hexdigest()
        if hashcode == signature:
            print("θ―·ζ±η»ζ1")
            print(echostr)
            return str(echostr)
        else:
            print('ιͺθ―ε€±θ΄₯')
            return "hi"

        print("θ―·ζ±η»ζ")
    ##ζΆζ―εε€
    if request.method=="POST":
        print("openθ·εPost")
        openid = request.args.get('openid');
        session['openid'] = openid
        print(openid)
        # θ‘¨η€ΊεΎ?δΏ‘ζε‘ε¨θ½¬εζΆζ―θΏζ₯
        xml_str = request.data
        if not xml_str:
            return ""
        # ε―Ήxmlε­η¬¦δΈ²θΏθ‘θ§£ζ
        xml_dict = xmltodict.parse(xml_str)
        xml_dict = xml_dict.get("xml")

        # ζεζΆζ―η±»ε
        msg_type = xml_dict.get("MsgType")
        if msg_type == "text":
            # θ‘¨η€Ίειηζ―ζζ¬ζΆζ―
            # ζι θΏεεΌοΌη»η±εΎ?δΏ‘ζε‘ε¨εε€η»η¨ζ·ηζΆζ―εε?Ή
            resp_dict = {
                "xml": {
                    "ToUserName": xml_dict.get("FromUserName"),
                    "FromUserName": xml_dict.get("ToUserName"),
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": "you say:" + xml_dict.get("Content")
                }
            }

            # ε°ε­εΈθ½¬ζ’δΈΊxmlε­η¬¦δΈ²
            resp_xml_str = xmltodict.unparse(resp_dict)
            # θΏεζΆζ―ζ°ζ?η»εΎ?δΏ‘ζε‘ε¨
            return resp_xml_str
        else:
            resp_dict = {
                "xml": {
                    "ToUserName": xml_dict.get("FromUserName"),
                    "FromUserName": xml_dict.get("ToUserName"),
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": "Dear I Love you so much"
                }
            }
            resp_xml_str = xmltodict.unparse(resp_dict)
            # θΏεζΆζ―ζ°ζ?η»εΎ?δΏ‘ζε‘ε¨
            return resp_xml_str

    # print("2")
