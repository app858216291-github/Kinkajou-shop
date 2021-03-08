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
import xmltodict
import time
import hashlib
wx = Blueprint('wx',__name__)
IMAGE_FOLDER  = 'static/upload/'


@wx.route('/index', methods=['POST','GET'])
def index():

    return "index"

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
