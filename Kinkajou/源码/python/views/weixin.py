# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect,request,jsonify,send_from_directory,url_for,send_file,session

from model.models import User,Product,PayRecord,Order
from sqlalchemy import or_,and_
from model.modelBase import Jsonfy
from werkzeug.utils import secure_filename
import random,datetime,os
import traceback
from common import weixinpay,tools,aliyun
from common import wxjspay
import trace
import setting
import xmltodict
import time
import hashlib
import wechatpy
from wechatpy.pay.utils import (
    calculate_signature, calculate_signature_hmac, _check_signature, dict_to_xml
)
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

import json
import hashlib
class wxjsconfig:
    def index(self):
        """
        知识中心
        :return:
        """
        id = self.get_argument('id', '')
        getSignPackage = self.getSignPackage()
        self.assign('getSignPackage', getSignPackage)
        self.display('knowledge/index.html')


    def getSignPackage(self):

        # 获得jsapi_ticket
        jsapiTicket = self.getJsApiTicket()

        # 注意 URL 一定要动态获取，不能 hardcode.
        # protocol = (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] !== 'off' || $_SERVER['SERVER_PORT'] == 443) ? "https://" : "http://";
        # $url = "$protocol$_SERVER[HTTP_HOST]$_SERVER[REQUEST_URI]";
        # 获取当前页面的url
        url = "{}://{}{}".format(self.request.protocol, self.request.host, self.request.uri)

        # 获取timestamp（时间戳）
        timestamp = int(time.time())
        # 获取noncestr（随机字符串）
        nonceStr = self.createNonceStr()

        # 这里参数的顺序要按照 key 值 ASCII 码升序排序
        string = "jsapi_ticket={}&noncestr={}&timestamp={}&url={}".format(jsapiTicket, nonceStr, timestamp, url)
        # 得到signature
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
        # 获取noncestr（随机字符串）
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

        # 获得jsapi_ticket
        # 获得jsapi_ticket之后，就可以生成JS-SDK权限验证的签名了
        import urllib.request
        # jsapi_ticket 应该全局存储与更新，以下代码以写入到文件中做示例
        # cookie('ticket',null);

        # 获取access_token
        accessToken = self.accesstokens()
        # 如果是企业号用以下 URL 获取 ticket
        # $url = "https://qyapi.weixin.qq.com/cgi-bin/get_jsapi_ticket?access_token=$accessToken";
        # 获取jsapi_ticket
        url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token={}&type=jsapi".format(accessToken)

        req = request.Request(url)
        res_data = request.urlopen(req)
        res = res_data.read()
        res = json.dumps(res)

        return str(res['ticket'])

##公众号回复和验证
@wx.route('/token',methods=['GET','POST'])
def token():
    token = 'mytoken1'
    print("请求进来了")
    if request.method == 'GET':
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
        print("open获取")
        print(openid)

        if len(request.args)==0:
            return "hello, this is handle view"
        list = [token, timestamp, nonce]
        list.sort()
        s = list[0]+list[1]+list[2]
        hashcode = hashlib.sha1(s.encode('utf-8')).hexdigest()
        if hashcode == signature:
            print("请求结束")
            return echostr
        else:
            print('验证失败')
            return "hi"

        print("请求结束")
    ##消息回复
    if request.method=="POST":
        print("open获取Post")
        openid = request.args.get('openid');
        session['openid'] = openid
        print(openid)
        # 表示微信服务器转发消息过来
        xml_str = request.data
        if not xml_str:
            return ""
        # 对xml字符串进行解析
        xml_dict = xmltodict.parse(xml_str)
        xml_dict = xml_dict.get("xml")

        # 提取消息类型
        msg_type = xml_dict.get("MsgType")
        if msg_type == "text":
            # 表示发送的是文本消息
            # 构造返回值，经由微信服务器回复给用户的消息内容
            resp_dict = {
                "xml": {
                    "ToUserName": xml_dict.get("FromUserName"),
                    "FromUserName": xml_dict.get("ToUserName"),
                    "CreateTime": int(time.time()),
                    "MsgType": "text",
                    "Content": "you say:" + xml_dict.get("Content")
                }
            }

            # 将字典转换为xml字符串
            resp_xml_str = xmltodict.unparse(resp_dict)
            # 返回消息数据给微信服务器
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
            # 返回消息数据给微信服务器
            return resp_xml_str

    # print("2")
