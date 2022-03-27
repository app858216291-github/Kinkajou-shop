# -*- coding: utf-8 -*-
import copy

from flask import Blueprint, render_template, redirect,request,jsonify,send_from_directory,url_for,session
from sqlalchemy.dialects import mysql

from model.models import User,Product,Car,Brown_his,Skufirst,Skusecond,Skuthird,Rate,Order,product_order_v,Product_Order,Category
from sqlalchemy import or_, and_, func, desc
import pymysql
from model.modelBase import Jsonfy
from werkzeug.utils import secure_filename
import random,datetime,os
from common import aliyun, tools
from common.tools import JsonUtil, IOUtil, shopUtil, productInfo4html
from model.modelBase import db
from common.Decorator import is_login
from model.modelBase import cache



product = Blueprint('product',__name__)
#文件上传存放的文件夹, 值为非绝对路径时，相对于项目根目录
IMAGE_FOLDER  = 'static/upload/'
#生成无重复随机数
gen_rnd_filename = lambda :"%s%s" %(datetime.datetime.now().strftime('%Y%m%d%H%M%S'), str(random.randrange(1000, 10000)))
#文件名合法性验证
allowed_file = lambda filename: '.' in filename and filename.rsplit('.', 1)[1] in set(['png', 'jpg', 'jpeg', 'gif', 'bmp'])



def uploadFile(f):
    if f and allowed_file(f.filename):
        return aliyun.upload(f)
    else:
        return "filename is null"
@product.route('/index', methods=['POST','GET'])
def index():
    return "index"
@product.route('/productList', methods=['POST','GET'])
def productList():
    # print(cache.get("key"))

    page=request.args.get("page")
    pageSize=request.args.get("pageSize")
    category=request.args.get("category")
    title = request.args.get("title")

    query=Product().query.filter(Product.orderId == 0).filter(Product.status == 0)

    if category!=None and category!=0 and category!="0":
        query=query.filter(Product.category == category)
    # prodcuts2=Product().query.filter(Product.orderId==0).all()
    if title!=None and title!="":
        query=query.filter(Product.title.like('%'+title+'%'))

    ##缓存
    key = str(query.statement.compile(dialect=mysql.dialect(), compile_kwargs={"literal_binds": True}))
    kk = cache.get(key)
    if kk != None:
        return kk
    if page!=None and pageSize!=None:
        prodcuts = Product().paginate(query,int(page),int(pageSize))
    else:
        prodcuts = Product().paginate(query)
    for product in prodcuts.items:
        sales = Product_Order().query.filter(Product_Order.productid == product.id).count()
        product.sales=sales
        product.main_image_key=product.main_image
        product.main_image=shopUtil.getFileFromKey(product.main_image)
    result=Jsonfy(count=prodcuts.total,data=prodcuts.items,has_next=prodcuts.has_next).__str__()

    cache.set(key,result)
    return  result

@product.route('/productListByOrder', methods=['POST','GET'])
def productListByOrder():
    page=request.args.get("page")
    limit=request.args.get("limit")
    orderid = request.args.get("orderid")
    if page!=None and limit!=None:

        prodcuts = product_order_v().paginate(product_order_v().query.filter(product_order_v.orderid == orderid),int(page),int(limit))
    else:
        prodcuts = product_order_v().paginate(product_order_v().query.filter(product_order_v.orderid == orderid))
    result=Jsonfy(count=prodcuts.total,data=prodcuts.items).__str__()
    return  result

@product.route('/addproduct', methods=['POST','GET'])
def addproduct():

    product = Product()
    product.title = request.args.get('title')
    product.main_image = request.args.get('main_image')
    product.price = request.args.get('price')
    product.sales = request.args.get('sales')
    product.store = request.args.get('store')
    product.color = request.args.get('color')
    product.size = request.args.get('size')
    product.detail_image = request.args.get('image200')
    product.image200 = request.args.get('image200')
    product.category = request.args.get('category')
    product.add()
    return Jsonfy().__str__()
@product.route('/editproduct', methods=['POST','GET'])
def editproduct():
    id=request.args.get('id')
    product = Product().get(id)
    if product==None:
        return "no product was found"
    if request.args.get('title')!=None:
        product.title = request.args.get('title')
    if request.args.get('main_image') != None:
        product.main_image = request.args.get('main_image')
    if request.args.get('detail_image') != None:
        product.detail_image = request.args.get('detail_image')
    if request.args.get('price') != None:
        product.price = request.args.get('price')
    if request.args.get('sales') != None:
        product.sales = request.args.get('sales')
    if request.args.get('store') != None:
        product.store = request.args.get('store')
    if request.args.get('image200') != None:
        product.image200 = request.args.get('image200')
    if request.args.get('number') != None:
        number=request.args.get('number')
        product.number = int(number)
    if request.args.get('category') != None:
        category = request.args.get('category')
        product.category = category
                # number
    product.updateOrAdd()
    return Jsonfy().__str__()


@product.route('/productDetail', methods=['POST','GET'])
def productDetail():
    # print(1)
    id = request.args.get('id')
    prop=request.args.get("prop")
    product=Product().get(id)
    ##销量
    sales = Product().query.filter(Product.productid == product.id).count()
    ##浏览量
    skim=Brown_his().query.filter(Brown_his.productid == product.id).count()
    sales = Product_Order().query.filter(Product_Order.productid == product.id).count()
    product.sales = sales
    product.skim=skim
    #统计所有sku的库存
    ret = db.session.execute("SELECT sum(store) as stores FROM skuthird WHERE productid=" + str(product.id))
    a = list(ret)
    if str(a[0]).find("None") == -1:
        product.store = int(a[0].stores.real)
    if not prop ==None and not prop==0 and not prop=='0':
        sku=Skuthird().get(prop)
        if sku!=None:
            product.color=sku.basename
            product.size=sku.funame
            product.price=sku.price
            product.store=sku.store

            product.imgsku_key = sku.pic
            product.imgsku =shopUtil.getFileFromKey( sku.pic)

    product.main_image_key=product.main_image
    product.main_image=shopUtil.getFileFromKey(product.main_image)
    product.image100_key=product.image100
    product.image100 = shopUtil.getFileFromKey(product.image100)
    product.image200_key=product.image200
    product.image200 = shopUtil.getFileFromKey(product.image200)
    product.image400_key=product.image400
    product.image400 = shopUtil.getFileFromKey(product.image400)
    product.image800_key=product.image800
    product.image800 = shopUtil.getFileFromKey(product.image800)
    result=Jsonfy(data=product).__str__()
    return  result

@product.route('/addCar', methods=['POST','GET'])
@is_login
def addCar():
    productid = request.args.get('productid')
    propid = request.args.get('propid')
    car=Car().query.filter(Car.productid==productid).filter(Car.propid==propid).first()
    if car==None:
        car = Car()
        productid = request.args.get('productid')
        car.productid=productid
        car.propid=propid
        car.mount=1
        car.userid=shopUtil.getUserId(request)
        car.add()
    else:
        car.mount=car.mount+1
        # car.propid = propid
        car.userid = shopUtil.getUserId(request)
        car.updateOrAdd()
    return  Jsonfy().__str__()

@product.route('/removeCar', methods=['POST','GET'])
@is_login
def removeCar():
    productid = request.args.get('productid')
    car=Car().query.filter(Car.productid==productid).first()
    if car==None:
        return Jsonfy(msg="购物车没有该产品").__str__()
    else:
        car.deleteById()
    return  Jsonfy().__str__()

@product.route('/carList', methods=['POST','GET'])
def carList():
    productids = request.args.get("productids")
    if productids!=None:
        productids = productids.split(",")
        cars = Car().query.filter(Car.productid.in_(productids)).all()
    else:
        cars = Car().all()

    # cars=Car().all()
    if cars==None:
        return Jsonfy(code=-1,msg="购物车为空").__str__()
    else:
        products=[]
        for car in cars:
            product=Product().get(car.productid)
            if product==None:
                continue
            p=copy.deepcopy(product)
            p.mount=car.mount
            if  car.propid!=None:
                sku=Skuthird().get(car.propid)
                if sku!=None:
                    p.color=sku.basename
                    p.size=sku.funame
                    p.price=sku.price
                    p.propid=car.propid
                    p.store=sku.store
                    p.imgsku=sku.pic
            else:
                ret = db.session.execute(
                    "SELECT sum(store) as stores FROM skuthird WHERE productid=" + str(car.productid))
                a = list(ret)
                if str(a[0]).find("None") == -1:
                    p.store = int(a[0].stores.real)

            products.append(p)
    return  Jsonfy(data=products).__str__()

@product.route('/changeCarMount', methods=['POST','GET'])
def changeCarMount():
    productid = request.args.get('productid')
    mount = request.args.get('mount')

    car = Car().query.filter(Car.productid == productid).filter(Car.userid == shopUtil.getUserId(request)).first()
    car.mount=mount
    car.updateOrAdd()
    return  Jsonfy().__str__()

@product.route('/skuedit', methods=['POST','GET'])
def skuedit():

    param = request.args.get('param')
    param = JsonUtil.loads(param)
    productid = param["productid"]
    shuxing = param["shuxing"]
    fujiashuxing = param["fujiashuxing"]
    skus = param["skus"]
    skufirst = param["skufirst"]

    skufirstM=Skufirst()
    skufirstM.baseid=skufirst["baseid"]
    skufirstM.basename=skufirst["basename"]
    skufirstM.fuid=skufirst["fuid"]
    skufirstM.funame=skufirst["funame"]
    skufirstM.productid=productid
    db.session.execute("delete from skusecond where productid="+str(productid))
    db.session.execute("delete from skufirst where productid=" + str(productid))
    db.session.execute("delete from skuthird where productid=" + str(productid))
    # db.session
    # shuxing.extend(fujiashuxing)
    for item in shuxing:
        skusecondM = Skusecond()
        if ("LAY_CHECKED" in item) and (item["LAY_CHECKED"]==True):
            skusecondM.productid=productid
            skusecondM.propertyid=item["propertyid"]
            skusecondM.propertyname = item["propertyname"]
            skusecondM.firstid=skufirstM.baseid
            skusecondM.add()
    for item in fujiashuxing:
        skusecondM = Skusecond()
        if ("LAY_CHECKED" in item) and (item["LAY_CHECKED"]==True):
            skusecondM.productid=productid
            skusecondM.propertyid=item["propertyid"]
            skusecondM.propertyname = item["propertyname"]
            skusecondM.firstid=skufirstM.fuid
            skusecondM.add()
    for item in skus:
        skuthirdM=Skuthird()
        skuthirdM.productid=productid
        skuthirdM.baseid=item["baseid"]
        skuthirdM.basename = item["basename"]
        skuthirdM.fuid = item["fuid"]
        skuthirdM.funame = item["funame"]
        skuthirdM.price = item["price"]
        skuthirdM.store = item["store"]
        if item.get("pic")!=None:
            skuthirdM.pic = item["pic"]
        skuthirdM.add()
    skufirstM.add()
    # skuthirdM = Skuthird().query.filter(Skuthird.productid == productid).all().


    return  Jsonfy().__str__()

@product.route('/skuview', methods=['POST','GET'])
def skuview():

    productid = request.args.get('productid')
    skufirstM=Skufirst().query.filter(Skufirst.productid==productid).first()
    skusecondM = Skusecond().query.filter(Skusecond.productid == productid).all()
    skuthirdM = Skuthird().query.filter(Skuthird.productid == productid).all()
    for third in skuthirdM:
        if third==None:
            continue
        if third.pic==None:
            continue
        if  str(third.pic).find("http")==-1 and len(third.pic)<15:
            third.pickey = third.pic
            third.pic=shopUtil.getFileFromKey(third.pic)

    result={}
    result["skufirst"]=skufirstM
    result["skusecond"] = skusecondM
    result["skuthird"] = skuthirdM

    return  Jsonfy(data=result).__str__()

@product.route('/addRate', methods=['POST','GET'])

def addRate():
    rate=Rate()
    rete=IOUtil.request2Obj(rate,request)
    prodcuts = Product_Order().query.filter(Product_Order.orderid == rete.orderid).all()
    # prodcuts = Product().query.filter(Product.orderId == rete.orderid).all()
    for product in prodcuts:
        rateTemp=Rate()
        rateTemp.productid=product.productid
        rateTemp.userid=shopUtil.getUserId(request)
        rateTemp.content=rete.content
        rateTemp.describeRate=rete.describeRate
        rateTemp.logisticsRate=rete.logisticsRate
        rateTemp.evaluate=rete.evaluate
        rateTemp.orderid=rete.orderid
        rateTemp.serviceRate=rete.serviceRate
        rateTemp.propid=product.propid
        if rateTemp.propid!=None and rateTemp.propid!=0 and rateTemp.propid!='0':
            rateTemp.basename=product.basename
            rateTemp.funame = product.funame
        # rate.id=None
        # rateTemp.productid=product.id
        rateTemp.add()
    order=Order().get(rate.orderid)
    order.orderStatus=6
    order.updateOrAdd()

    return  Jsonfy().__str__()

@product.route('/rateList', methods=['POST','GET'])
def rateList():
    # page = request.args.get("page")
    # pageSize = request.args.get("pageSize")
    productid = request.args.get('productid')
    if productid==None or productid==0 or productid=='0' or productid=='':
        return Jsonfy().__str__()
    rates=Rate().query.filter(Rate.productid== productid).order_by(desc(Rate.create_time)).all()
    for rate in rates:
        user=User().query.filter(User.id== rate.userid).first()
        rate.nickname=user.nickname
        if rate.propid==0 or rate.propid=='0':
            product=Product().get(rate.productid)
            rate.basename = product.color
            rate.funame = product.size
        else:
            sku=Skuthird().get(rate.propid)
            if sku!=None:
                rate.basename=sku.basename
                rate.funame=sku.funame
            else:
                rate.basename = ""
                rate.funame = ""
    # rates = Product().paginate(query,int(page),int(pageSize))
    return  Jsonfy(data=rates).__str__()

@product.route('/add_update_category', methods=['POST','GET'])
def add_update_category():
    node=request.args.get('node')
    node=JsonUtil.loads(node)
    print(node.get("cid"))
    print(node.get("pid") is not None)
    if node.get("cid")!=None and node.get("pid")!=None:
        category_2=Category().query.filter(Category.cid == int(node.get("cid"))).filter(Category.pid == int(node.get("pid"))).first()
        if category_2==None:
            category_2_=Category()
            category_2_.cid=node.get("cid")
            category_2_.pid = node.get("pid")
            category_2_.name = node.get("name")
            category_2_.add()
        else:
            category_2.cid = node.get("cid")
            category_2.pid = node.get("pid")
            category_2.name = node.get("name")
            category_2.updateOrAdd()

    return  Jsonfy(data=True).__str__()

@product.route('/maxId', methods=['POST','GET'])
def maxId():
    # category_2 = Category_2().query.max(id)
    category_2=Category().all()
    if len(category_2)==0:
        return Jsonfy(data=0).__str__()
    category_2 = db.session.query(func.max(Category.cid).label('id')).one()
    return  Jsonfy(data=category_2.id).__str__()

@product.route('/getCategory', methods=['POST','GET'])
def getCategory():
    # category_2 = Category_2().query.max(id)
    key="category_2_all"
    kk = cache.get(key)##查看缓存里是否有值，有的话直接取
    if kk!=None:
        return kk
    category_2=Category().query.filter(Category.pid!=0).order_by(desc(Category.pid)).all()
    cache.set(key, Jsonfy(Jsonfy(data=category_2).__str__(), timeout=6 * 60 * 60))  ##将查询结果缓存到缓存里
    return  Jsonfy(data=category_2).__str__()
@product.route('/deleteCategory', methods=['POST','GET'])
def deleteCategory():
    # category_2 = Category().query.max(id)
    pid = request.args.get('pid')
    cid = request.args.get('cid')

    category=Category().query.filter(Category.pid==pid).filter(Category.cid==cid).first()
    category.deleteById()

    return  Jsonfy(data=True).__str__()


# class Register(FlaskForm):
#     # 引入Form基类
#     from flask.ext.wtf import Form
#     # 引入Form元素父类
#     from wtforms import StringField, PasswordField
#     # 引入Form验证父类
#     from wtforms.validators import DataRequired, Length
#
#     __author__ = 'kikay'
#     username = StringField('name',validators=[DataRequired(message=u"用户名不能为空"),Length(10,20,message=u'长度位于10~20之间')],render_kw={'placeholder':u'输入用户名'})



##通过url创建商品
##http://127.0.0.1:5000/product/addProductFromUrl?url=http://admin.heshihuan.cn/fileServer/product/1.html
@product.route('/addProductFromUrl', methods=['POST', 'GET'])
def addProductFromUrl():
    if request.method == 'GET':
        return render_template('TBProductAdd.html')
    import urllib.request  # 导入urllib.request库
    # url = request.args.get('url')
    # text = request.args.get('text')
    url=request.form.get('url')
    text = request.form.get('text')
    info = {}
    if url == None and text != None:
        info = productInfo4html.getproductInfo(text)
    if url != None and text == None:
        a = urllib.request.urlopen(url)  # 打开指定网址
        html = a.read()  # 读取网页源码
        html = html.decode("utf-8")
        info = productInfo4html.getproductInfo(html)
    return Jsonfy(data=info).__str__()




# @product.route('/addProductFromUrl', methods=['POST','GET'])
# def addProductFromUrl():


        # soup = BeautifulSoup(html)
        # zhutu = soup.find('ul', id='J_UlThumb')
        # xiangqing = soup.find('div', id='description')
        # for img in zhutu.find_all('img', src=valid_img):
        #     src = img['src']
        #     # print('src is',src)
        #     if not src.startswith('http'):
        #         src = 'http:' + src
        #     download_file(src)
        # return  Jsonfy(data=True).__str__()




    # url = request.args.get('url')
    # import urllib.request  # 导入urllib.request库
    #
    # a = urllib.request.urlopen(url)  # 打开指定网址
    # html = a.read()  # 读取网页源码
    # html = html.decode("utf-8")
    # soup = BeautifulSoup(html)
    # zhutu = soup.find('ul', id='J_UlThumb')
    # xiangqing = soup.find('div', id='description')
    # for img in zhutu.find_all('img', src=valid_img):
    #     src = img['src']
    #     # print('src is',src)
    #     if not src.startswith('http'):
    #         src = 'http:' + src
    #     download_file(src)
    # return  Jsonfy(data=True).__str__()








