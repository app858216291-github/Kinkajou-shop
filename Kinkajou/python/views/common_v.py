# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect,request,jsonify,send_from_directory,url_for,send_file,Response,make_response,session
from model.models import User,Product,PayRecord,Order
from sqlalchemy import or_,and_
from model.modelBase import Jsonfy
from werkzeug.utils import secure_filename
import random,datetime,os
import traceback
from common import weixinpay,tools,aliyun
from common import wxjspay
from common import KdApiSearchDemo
from setting import FlaskConfig,Aliyun
common_v = Blueprint('common',__name__)
#文件上传存放的文件夹, 值为非绝对路径时，相对于项目根目录
IMAGE_FOLDER  = 'static/upload/'
#生成无重复随机数
gen_rnd_filename = lambda :"%s%s" %(datetime.datetime.now().strftime('%Y%m%d%H%M%S'), str(random.randrange(1000, 10000)))
#文件名合法性验证
allowed_file = lambda filename: '.' in filename and filename.rsplit('.', 1)[1] in set(['png', 'jpg', 'jpeg', 'gif', 'bmp','JPG','PNG'])

##D = get_class("datetime.datetime")
##D( 2010, 4, 22 )
##相当于java的Class.forName().newInstance()
def get_class( kls ):

    parts = kls.split('.')
    module = ".".join(parts[:-1])
    m = __import__( module )
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m
##globals()['classname'](args, to, constructor)

def uploadFile(f,dir="common"):
    if f and allowed_file(f.filename):
        return aliyun.upload(f,dir)
    else:
        return "filename is null"
@common_v.route('/index', methods=['POST','GET'])
def index():

    return "index"

@common_v.route('/showimg/<filename>')
def showimg_view(filename):
    return send_from_directory(IMAGE_FOLDER, filename)
##图片上传到阿里云，返回图片地址
@common_v.route('/upload/', methods=['POST','OPTIONS','GET'])
def upload_view():
    if id==None:
        res = dict(code=-1, msg=None)
        f = request.files.get('file')
        # aliyun.upload(f)-
        return Jsonfy(data=uploadFile(f)).__str__()
    f = request.files.get('file')
    dir = request.args.get('dir')
    if dir!=None:
        fileName = Aliyun.ReadUrl+dir+"/" + uploadFile(f,dir)
    else:
        fileName = Aliyun.ReadUrl+"/common/" + uploadFile(f,dir)

    return Jsonfy(data=fileName).__str__()

##图片上传到本地 万一阿里云收费了，则使用该方法
@common_v.route('/upload_heshihuan/', methods=['POST','OPTIONS','GET'])
def uploadLocal_view():
    f = request.files.get('file')
    path = "static/"
    file_path = path + f.filename
    f.save(file_path)
    fileName=FlaskConfig.FILESERVER+file_path
    # fileName = "http://127.0.0.1:5000/" + file_path

    return Jsonfy(data=fileName).__str__()


########################################################################################################
### 微信支付
########################################################################################################

##获取支付二维码
@common_v.route('/payPic/', methods=['POST','OPTIONS','GET'])
def payPic():
    productName = request.args.get('productName')
    orderNum=request.args.get('orderNum')
    price=request.args.get('price')
    attach = request.args.get('attach')
    try:
        pay_code = weixinpay.wxpay(productName,orderNum,price,attach)
        # id = request.args.get('package_id')
        byte_io = tools.IOUtil.set_qrcode(data=pay_code)

        return send_file(byte_io, mimetype='image/png')
    except:
        print(traceback.format_exc())
        print("error")
##获取支付码（二维码内容）
@common_v.route('/payCode/', methods=['POST', 'OPTIONS', 'GET'])
def payCode():
    productName = request.args.get('productName')
    orderNum = request.args.get('orderNum')
    price = request.args.get('price')
    attach = request.args.get('attach')
    try:
       pay_code = weixinpay.wxpay(productName, orderNum, price,attach)
       return Jsonfy(data=pay_code).__str__()
    except:
        print(traceback.format_exc())
        print("error")
        return Jsonfy(msg="fail").__str__()

##微信公众号支付
##http://127.0.0.1:5000/common/payjs2
##http://127.0.0.1:5000/common/payjs2?
@common_v.route('/payjs2', methods=['POST','GET'])
def payjs2():

    getInfo = request.args.get('getInfo', None)
    code = request.args.get('code', None)
    openid = session.get(request.args.get('code'))
    # openid2 =
    print("------------------------")
    print(openid)
    # aa=
    print("-------------------------")
    print("0")
    print(code)
    print(getInfo)
    print(openid)
    if not openid:
        if getInfo != 'yes':
            # 构造一个url，携带一个重定向的路由参数，
            # 然后访问微信的一个url,微信会回调你设置的重定向路由，并携带code参数
            print("2")
            # session['openid'] = 0
            return wxjspay.get_redirect_url()
        elif getInfo == 'yes':
            # 我设置的重定向路由还是回到这个函数中，其中设置了一个getInfo=yes的参数
            # 获取用户的openid
            openid = wxjspay.get_openid(request.args.get('code'), request.args.get('state', ''))
            if not openid:
                return '获取用户openid失败'
            print("1")
            print (openid)

            session[request.args.get('code')] = openid
            session[request.args.get('openid')]= openid
            print(request.args.get('code'))
            print("----++++")
            response = wxjspay.get_jsapi_params(openid)
            # response.set_cookie('openid', openid, expires=60 * 60 * 24 * 30)
            print(response)
            print("3")
            return (Jsonfy(data=response).__str__())
    result=wxjspay.get_jsapi_params(openid)
    return (Jsonfy(data=result).__str__())

##微信公众号支付获取openId
@common_v.route('/payGetOpenid', methods=['POST','GET'])
def payGetOpenid():
    getInfo = request.args.get('getInfo', None)
    code = request.args.get('code', None)
    if getInfo != 'yes':
        # 构造一个url，携带一个重定向的路由参数，
        # 然后访问微信的一个url,微信会回调你设置的重定向路由，并携带code参数
        return wxjspay.get_redirect_url()
    elif getInfo == 'yes':
        # 我设置的重定向路由还是回到这个函数中，其中设置了一个getInfo=yes的参数
        # 获取用户的openid
        openid = wxjspay.get_openid(request.args.get('code'), request.args.get('state', ''))
        if not openid:
            return (Jsonfy(data='获取用户openid失败').__str__())
        return (Jsonfy(data=openid).__str__())
    return
##微信公众号支付获取支付参数
@common_v.route('/payjs', methods=['POST','GET'])
def payjs():
    openid = request.args.get('openid')
    attach = request.args.get('attach')
    print(openid)
    print(attach)
    print("---")
    openid=openid.replace('"','')
    try:
        # result=aa=response.content.decode()
        return (Jsonfy(data= wxjspay.get_jsapi_params(openid,attach=attach)).__str__())
    except:
        print("--error-")
        traceback.print_exc()
        return (Jsonfy(code=-1,data= "支付参数获取失败").__str__())

##微信回调
@common_v.route('/notify/', methods=['POST', 'OPTIONS', 'GET'])
def notify():
    print(request.form)
    print(request.args)
    print(request.data)
    print("----------------------------------------------------------------")
    data=weixinpay.trans_xml_to_dict(request.data)
    payData = PayRecord()
    payData.returnstring = request.data
    data.setdefault("attach", "支付监听")
    if data["out_trade_no"]!=None:
        print(data["out_trade_no"])
        payData.tradeNo = data["out_trade_no"]
    if data["total_fee"] != None:
        print(data["total_fee"])
        payData.totalFee = data["total_fee"]
    if data["transaction_id"] != None:
        print(data["transaction_id"])
        payData.transactionId = data["transaction_id"]
    if data["attach"] != None:
        print(data["attach"])
        payData.attach = data["attach"]
    payData.add()

    # order=PayRecord().query.filter(Order.orderNo==data["attach"]).first()
    order = Order().query.filter(Order.orderNo == data["attach"]).first()
    print("订单修改操作"+order.orderNo)
    if(order!=None):
        print("进入订单修改操作")
        order.orderStatus=2
        order.updateOrAdd()
    return '''
            <xml>
            <return_code><![CDATA[SUCCESS]]></return_code>
            <return_msg><![CDATA[OK]]></return_msg>
            </xml>
            '''
##订单支付查询
@common_v.route('/pay/query/', methods=['POST', 'OPTIONS', 'GET'])
def query():
    attach=request.args.get('attach')
    payData = PayRecord()
    payData=PayRecord().query.filter(PayRecord.attach==attach).first()
    if payData!=None:
        payData.returnstring=""
    if payData==None:
        return Jsonfy(code=-1,msg="the tradeNo is empty").__str__()
    return Jsonfy(data=payData).__str__()
    return "abc"

##订单支付查询
@common_v.route('/pay/getOpenid/', methods=['POST', 'OPTIONS', 'GET'])
def getOpenid():
    # 设置临时openid,
    session["openid"]="oUrkV1R5f_Snab1jSmD7cYqhYQ3g"##迂回
    # session["openid"]='oUrkV1bRQ_fyzPaM77pVWnL8 - YVM'##兰界openId
    openid=session.get('openid')
    if openid == None:
        return "0"
    return openid





########################################################################################################
### 通用数据库操作接口
########################################################################################################
##添加数据
##http://127.0.0.1:5000/common/model/add/?modelName=User&username=abcd&password=7894567
@common_v.route('/model/add/', methods=['POST', 'OPTIONS', 'GET'])
def addModel():
    id = request.args.get('id')
    modelName=request.args.get('modelName')
    _model= get_class("model.models."+modelName)
    model=_model()
    tools.IOUtil.request2Obj(model,request)
    if id!=None:
        model.id=None
    model.add()
    model= _model().get(model.id)
    return Jsonfy(data=model).__str__()

##http://127.0.0.1:5000/common/model/eidt/?modelName=User&username=abcd&password=7894567&id=5
@common_v.route('/model/edit/', methods=['POST', 'OPTIONS', 'GET'])
def editModel():
    modelName=request.args.get('modelName')
    _model= get_class("model.models."+modelName)
    model=_model()
    tools.IOUtil.request2Obj(model,request)
    model.updateOrAdd()
    model= _model().get(model.id)
    return Jsonfy(data=model).__str__()

##http://127.0.0.1:5000/common/model/del/?modelName=User&id=5
@common_v.route('/model/del/', methods=['POST', 'OPTIONS', 'GET'])
def delModel():
    id = request.args.get('id')
    modelName=request.args.get('modelName')
    _model= get_class("model.models."+modelName)
    model=_model()
    model.id=id
    model.status=-2
    model.updateOrAdd() ##伪删除
    # model.deleteById()
    # model= _model().get(model.id)
    return Jsonfy(data=model).__str__()

##查询数据
#http://127.0.0.1:5000/common/model/queryAll/?modelName=User&page=1&pageSize=2
@common_v.route('/model/queryAll/', methods=['POST', 'OPTIONS', 'GET'])
def queryAll():

    page = request.args.get("page")
    pageSize = request.args.get("pageSize")
    if pageSize==None:
        pageSize = request.args.get("limit")
    modelName=request.args.get('modelName')
    _model= get_class("model.models."+modelName)
    model=_model()

    ##添加状态大于0
    filters = set()
    attrs = dir(_model())
    for attr in attrs:
        if attr=='status':
            f = (getattr(_model, attr) != -2)
            filters.add(f)
    # query=_model().query.filter(Order.status==1)
    # modelList2 = query.all()
    if page != None and pageSize != None:
        modelList = _model().paginate(_model().query.filter(*filters),int(page), int(pageSize))
    else:
        modelList = _model().paginate(_model().query.filter(*filters))
    return Jsonfy(count=modelList.total, data=modelList.items).__str__()

    # modelList=model.all()
    # model= _model().get(model.id)
    # return Jsonfy(data=modelList).__str__()

##根据ID查询数据
##http://127.0.0.1:5000/common/model/queryById/?id=24&modelName=User
@common_v.route('/model/queryById/', methods=['POST', 'OPTIONS', 'GET'])
def queryById():
    modelName=request.args.get('modelName')
    _model= get_class("model.models."+modelName)
    id = request.args.get('id')
    model=_model()
    model=model.get(id)
    # model= _model().get(model.id)
    return Jsonfy(data=model).__str__()

##根据查询条件查询数据
##http://127.0.0.1:5000/common/model/queryByFilter/?id=24&modelName=User
@common_v.route('/model/queryByFilter/', methods=['POST', 'OPTIONS', 'GET'])
def queryByFilter():
    modelName=request.args.get('modelName')
    _model= get_class("model.models."+modelName)
    filters=tools.IOUtil.request2ObjFilters(_model, request)
    result= _model.query.filter(*filters).all()
    return Jsonfy(data=result).__str__()


##根据快递单号查询百世快递
##快递公司编码，目前仅支持：
##申通快递 STO
##圆通速递 YTO
# 百世快递 HTKY
##天天快递 HHTT
##http://127.0.0.1:5000/common/model/checkLogistics/?id=24&modelName=User
@common_v.route('/model/checkLogistics/', methods=['POST', 'OPTIONS', 'GET'])
def checkLogistics():
    shipperCode=request.args.get('shipperCode')
    logisticCode = request.args.get('logisticCode')
    result=KdApiSearchDemo.getResult(shipperCode,logisticCode)
    return Jsonfy(data=result).__str__()





########################################################################################################
### 对外公共接口
########################################################################################################
##获取校验
##http://127.0.0.1:5000/common/other/verify /?username=123
@common_v.route('/other/verify /', methods=['POST', 'OPTIONS', 'GET'])
def verify():
    username=request.args.get('username')
    username=username+",false"
    result= username
    return Jsonfy(data=result).__str__()

