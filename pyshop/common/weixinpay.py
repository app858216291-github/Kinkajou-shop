# -*- coding: utf-8 -*-
#微信支付配置 获取收款二维码
# ========支付相关配置信息===========
import random
import time
import hashlib
from random import Random
from bs4 import BeautifulSoup
import requests
import setting
import qrcode
import setting

APP_ID = setting.WeinXin.APP_ID # 你公众账号上的appid
MCH_ID = setting.WeinXin.MCH_ID  # 你的商户号
API_KEY = setting.WeinXin.API_KEY  # 微信商户平台(pay.weixin.qq.com) -->账户设置 -->API安全 -->密钥设置，设置完成后把密钥复制到这里
APP_SECRECT = setting.WeinXin.APP_SECRECT
UFDODER_URL = setting.WeinXin.UFDODER_URL  # 该url是微信下单api

NOTIFY_URL = setting.WeinXin.NOTIFY_URL # 微信支付结果回调接口，需要改为你的服务器上处理结果回调的方法路径
CREATE_IP = setting.WeinXin.CREATE_IP  # 你服务器的IP


def get_sign(data_dict, key):
    """
    签名函数
    :param data_dict: 需要签名的参数，格式为字典
    :param key: 密钥 ，即上面的API_KEY
    :return: 字符串
    """
    params_list = sorted(data_dict.items(), key=lambda e: e[0], reverse=False)  # 参数字典倒排序为列表
    params_str = "&".join(u"{}={}".format(k, v) for k, v in params_list) + '&key=' + key
    # 组织参数字符串并在末尾添加商户交易密钥
    md5 = hashlib.md5()  # 使用MD5加密模式
    md5.update(params_str.encode('utf-8'))  # 将参数字符串传入
    sign = md5.hexdigest().upper()  # 完成加密并转为大写
    return sign


def order_num(phone):
    """
    生成扫码付款订单号
    :param phone: 手机号
    :return:
    """
    local_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    result = phone + 'T' + local_time + random_str(5)
    return result


def random_str(randomlength=8):
    """
    生成随机字符串
    :param randomlength: 字符串长度
    :return:
    """
    strs = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        strs += chars[random.randint(0, length)]
    return strs

def trans_dict_to_xml(data_dict):
    """
    定义字典转XML的函数
    :param data_dict:
    :return:
    """
    data_xml = []
    for k in sorted(data_dict.keys()):  # 遍历字典排序后的key
        v = data_dict.get(k)  # 取出字典中key对应的value
        if k == 'detail' and not v.startswith('<![CDATA['):  # 添加XML标记
            v = '<![CDATA[{}]]>'.format(v)
        data_xml.append('<{key}>{value}</{key}>'.format(key=k, value=v))
    return '<xml>{}</xml>'.format(''.join(data_xml))  # 返回XML


def trans_xml_to_dict(data_xml):
    """
    定义XML转字典的函数
    :param data_xml:
    :return:
    """
    soup = BeautifulSoup(data_xml, features='xml')
    xml = soup.find('xml')  # 解析XML
    if not xml:
        return {}
    data_dict = dict([(item.name, item.text) for item in xml.find_all()])
    return data_dict
def wxpay(productName,orderNum,price,attach="附件数据"):
    nonce_str = random_str() # 拼接出随机的字符串即可，我这里是用  时间+随机数字+5个随机字母

    total_fee = 1  # 付款金额，单位是分，必须是整数

    params = {
        'appid': APP_ID,  # APPID
        'mch_id': MCH_ID,  # 商户号
        'nonce_str': nonce_str,    # 随机字符串
        ##'out_trade_no': order_num(orderNum),  # 订单编号，可自定义
        'out_trade_no': orderNum,  # 订单编号，可自定义
        'total_fee': price, # 订单总金额
        'spbill_create_ip': CREATE_IP,  # 自己服务器的IP地址
        'notify_url': NOTIFY_URL,  # 回调地址，微信支付成功后会回调这个url，告知商户支付结果
        'body': productName,  # 商品描述
        'detail': 'xxx商品',  # 商品描述
        'trade_type': 'NATIVE',  # 扫码支付类型
        "attach":attach
    }

    sign = get_sign(params,API_KEY)  # 获取签名
    params['sign'] = sign  # 添加签名到参数字典
    # print(params)
    xml = trans_dict_to_xml(params)  # 转换字典为XML
    xml=xml.encode("utf-8")
    print(xml)
    response = requests.request('post', UFDODER_URL, data=xml)  # 以POST方式向微信公众平台服务器发起请求

    data_dict = trans_xml_to_dict(response.content)
    # print(response.content.decode("utf-8"))
    print(data_dict["code_url"])
    return data_dict["code_url"]


#将这个字符串转成二维码，就可以收钱了
# print(wxpay("123"))

