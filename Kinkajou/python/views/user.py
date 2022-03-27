# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect,request,jsonify,make_response,session
from model.models import User,Address,Brown_his,Product,User2product
from sqlalchemy import or_, and_, desc
from model.modelBase import Jsonfy
from common.tools import IOUtil,shopUtil
from common.Decorator import is_login
import  random
from model.modelBase import cache

user = Blueprint('user',__name__)

@user.route('/index', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        data = request.args
    elif request.method=='POST':
        data=request.form

    p1 = User(name="rewqq")
    p1.updateOrAdd();
    return "as"

##公众号登录，不用注册，没账号自动注册
@user.route('/login_openid', methods=['POST','GET'])
def loginbyopenid():
    openid = request.args.get('openid')
    r=User().query.filter(and_(User.openid == openid)).first()
    if r==None:
        userNew=User()
        userNew.openid=openid
        userNew.nickname="蜜熊"+openid[10:13]
        userNew.add()
        r = User().query.filter(and_(User.openid == openid)).one()
        r.token = IOUtil.createToken(r.id)
        return Jsonfy(data=r, code=1).__str__()
    r.token=IOUtil.createToken(r.id)
    aa=Jsonfy(data=r,code=1).__str__()
    # print(aa)
    return aa
##小程序登录，不用注册，没账号自动新建
@user.route('/login_MP', methods=['POST','GET'])
def login_MP():
    openid = request.args.get('openid')

    r=User().query.filter(User.openid_mp == openid).first()
    if r==None:
        userNew=User()
        userNew.openid_mp=openid
        userNew.nickname = "蜜熊" + openid[10:13]
        userNew.add()
        r = User().query.filter(User.openid_mp == openid).one()
        r.token = IOUtil.createToken(r.id)
        return Jsonfy(data=r, code=1).__str__()
    r.token=IOUtil.createToken(r.id)
    aa=Jsonfy(data=r,code=1).__str__()
    return aa


@user.route('/login', methods=['POST', 'GET'])
def login():
    user33 = session.get('userid')
    mobile = request.args.get('mobile')
    password = request.args.get('password')

    r = User().query.filter(and_(User.mobile == mobile, User.password == password)).first()
    if r == None:
        return Jsonfy(code=0, msg="没有该用户").__str__()


    # session["userid"] =r.id
    # user22 = session.get('userid')
    r.token=IOUtil.createToken(r.id)
    # a=Jsonfy(data=r,code=1).__str__()
    return Jsonfy(data=r,code=1).__str__()

@user.route('/register', methods=['POST', 'GET'])
def register():
    u=IOUtil.request2Obj(User(),request)
    u.add()
    return Jsonfy().__str__()
@user.route('/addAddress', methods=['POST', 'GET'])
# @is_login
def addAddress():
    id = request.args.get('id')
    if id==None:
        address = Address()
        address=IOUtil.request2Obj(address,request)
        if address.default=='false':
            address.default=False
        else:address.default=True
        address.userId = shopUtil.getUserId(request)
        address.add()
    else:
        address = Address().get(id)
        address.receiver = request.args.get('receiver')
        address.mobile = request.args.get('mobile')
        address.address = request.args.get('address')
        address.area = request.args.get('area')
        address.default = True
        if(request.args.get('default')=='false'):
            address.default =False

        address.userId =shopUtil.getUserId(request)
        address.updateOrAdd()
    address2=Address().get(address.id)
    return Jsonfy(data=address,code=1).__str__()
@user.route('/addressList', methods=['POST', 'GET'])
def addressList():
    # address=Address().all()
    address= Address().query.filter(Address.userId==shopUtil.getUserId(request)).filter(Address.orderId.is_(None)).filter(Address.status ==0).all()
    # cc=Jsonfy(data=address).__str__()
    return Jsonfy(data=address).__str__()
@user.route('/address', methods=['POST', 'GET'])
def address():
    orderid= request.args.get("orderid")
    if orderid!=None:
        result = Address().query.filter(Address.userId == shopUtil.getUserId(request)).filter(
            Address.orderId == orderid).first()
        return Jsonfy(data=result).__str__()
    result=Address().query.filter(Address.userId ==shopUtil.getUserId(request)).filter(Address.default ==True).filter(Address.status ==0).first()
    # address=.get(1)
    return Jsonfy(data=result).__str__()
@user.route('/deladdress', methods=['POST', 'GET'])
def deladdress():
    id=request.args.get("id")
    address=Address().query.filter(Address.userId ==shopUtil.getUserId(request)).filter(Address.id ==id).first()
    address.status=-1
    address.updateOrAdd();
    return Jsonfy().__str__()


###添加浏览记录
@user.route('/addhis', methods=['POST', 'GET'])
def addhis():
    productid=request.args.get('productid')
    # brownHises=Brown_his().query.filter(Brown_his.productid==productid).all()
    # # if brownHises!=None:
    # for brownHis in brownHises:
    #     brownHis.deleteById()
    bs = Brown_his()
    bs.productid = productid
    bs.add()
    return Jsonfy().__str__()
@user.route('/his', methods=['POST', 'GET'])
def his():
    products=request.args.get("products")
    if products==None:
        return Jsonfy(data=[]).__str__()
    productsList=products.split(',')
    query= Product().query.filter(Product.id.in_((productsList)))
    products = Product().paginate(query, int(1), int(20))
    # brownHises=Brown_his().query.filter(Address.id >1).limit(10).all()
    # products=[]
    # for productid in productsList:
    #     product=Product().get(productid)
    #     if product ==None:
    #         continue
    #     products.append(product)
    # products.append()
    return Jsonfy(count=products.total,data=products.items,has_next=products.has_next).__str__()

###收藏
@user.route('/addcollect', methods=['POST', 'GET'])
@is_login
def addcollect():
    productid=request.args.get('productid')
    collects=User2product().query.filter(and_(User2product.productid==productid,User2product.operate==2)).all()
    # if brownHises!=None:
    for collect in collects:
        collect.deleteById()
        return Jsonfy(data="取消收藏成功").__str__()
    collect = User2product()
    collect.productid = productid
    collect.userid=shopUtil.getUserId(request)
    collect.operate=2
    collect.add()
    return Jsonfy(data="收藏成功").__str__()

##查看收藏列表
@user.route('/collectList', methods=['POST', 'GET'])
@is_login
def collectList():
    productid = request.args.get('productid')
    if productid!=None and productid!=0 and productid!="":
        collects=User2product().query.filter(User2product.userid==shopUtil.getUserId(request)).filter(User2product.productid==productid).filter(User2product.operate==2).limit(10).all()
        if collects!=None:
            if len(collects)>0:
                return Jsonfy(data=True).__str__()
            else:
                return Jsonfy(data=False).__str__()
    collects=User2product().query.filter(User2product.operate==2).limit(10).all()
    products=[]
    for collect in collects:
        if collect.productid ==None:
            continue
        product=Product().get(collect.productid)
        if product==None:
            continue
        products.append(product)
    # products.append()
    return Jsonfy(data=products).__str__()
##取消收藏
@user.route('/cancelCollect', methods=['POST', 'GET'])
@is_login
def cancelCollect():
    productid = request.args.get('productid')
    collects = User2product().query.filter(and_(User2product.productid == productid, User2product.operate == 2)).all()
    # if brownHises!=None:
    for collect in collects:
        collect.deleteById()
    return Jsonfy().__str__()

##修改用户信息
@user.route('/editUser', methods=['POST', 'GET'])
@is_login
def editUser():
    nickname = request.args.get('nickname')
    name = request.args.get('name')
    age = request.args.get('age')
    mobile = request.args.get('mobile')
    user=User().get(shopUtil.getUserId(request))
    user.nickname=nickname
    user.name=name
    user.age=age
    user.mobile=mobile
    user.updateOrAdd()
    user=User().get(shopUtil.getUserId(request))
    user.token = request.headers.get('token')
    return Jsonfy(data=user).__str__()

##查询用户信息
@user.route('/getUser', methods=['POST', 'GET'])
@is_login
def getUser():
    user=User().get(shopUtil.getUserId(request))
    user.token= request.headers.get('token')
    return Jsonfy(data=user).__str__()

##4位验证码
##http://127.0.0.1:5000/user/getVerification
@user.route('/getVerification', methods=['POST', 'GET'])
def getVerification():
    list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    list_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 's', 't', 'x', 'y',
                'z']
    veri_str = random.sample(list_str, 2)
    veri_num = random.sample(list_num, 2)
    veri_out = random.sample(veri_num + veri_str, 4)
    veri_res = str(veri_out[0]) + str(veri_out[1]) + str(veri_out[2]) + str(veri_out[3])
    print(veri_res)
    cache.set("code",veri_res)
    return veri_res

@user.route('/getVerification_', methods=['POST', 'GET'])
def getVerification_():
    return cache.get("code")

