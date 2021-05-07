import requests
import hashlib
import base64
import json
import setting

# 请求url --正式地址
###免费版仅支持限500次/天（即时查询 支持四家 申通、圆通、百世、天天） 有效期半年  http://www.kdniao.com/
Url=setting.KdApiConfig.Url
# 电商加密私钥，快递鸟提供，注意保管，不要泄漏
# 请登陆快递鸟用户管理后台查看：http://kdniao.com/UserCenter/UserHome.aspx
AppKey=setting.KdApiConfig.AppKey
# 电商ID
EBusinessID = setting.KdApiConfig.EBusinessID

def md5(n):
    md5 = hashlib.md5()
    md5.update(str(n).encode("utf-8"))
    return md5.hexdigest()
# md5加密


def getSign(n):
    md5Data = md5(json.dumps(n)+AppKey)
    res = str(base64.b64encode(md5Data.encode("utf-8")), "utf-8")
    return res
# 签名


def getParams(shipperCode='HTKY',logisticCode='557041801175929'):
    # 请求接口指令
    RequestType = "1002"
    # RequestData = {'OrderCode': '',
    #                'ShipperCode': 'HTKY', 'LogisticCode': '557041801175929'}
    RequestData = {'OrderCode': '',
                   'ShipperCode': shipperCode, 'LogisticCode': logisticCode}

    data = {
        "RequestData": json.dumps(RequestData),
        "RequestType": RequestType,
        "EBusinessID": EBusinessID,
        "DataSign": getSign(RequestData),
        "DataType": 2
    }
    return data
# 请求参数

def post(url, data):
    res = requests.post(url, data)
    return res.text
# 发送post请求

def getResult(shipperCode='HTKY',logisticCode='557041801175929'):
    result = post(Url, getParams(shipperCode,logisticCode))
    print(result)
    return result
# 输出结果


# getResult()
