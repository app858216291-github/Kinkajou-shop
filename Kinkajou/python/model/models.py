# -*- coding: utf-8 -*-
# demo03_SQLAlchemy.py
from datetime import datetime


from flask_sqlalchemy import SQLAlchemy
import json,time
import sys
sys.path.append("E:\codes\python\pyshop")
from model.modelBase import db,CommonModel



class User(CommonModel,db.Model):
    username= db.Column(db.String(64))
    password=db.Column(db.String(64))
    mobile=db.Column(db.String(64))
    phone=db.Column(db.String(64))
    name = db.Column(db.String(64))
    portrait= db.Column(db.String(256))
    nickname=db.Column(db.String(64))
    openid = db.Column(db.String(64))
    age=db.Column(db.Integer,default=18)
    address= db.Column(db.String(256))#联系地址
    signature=db.Column(db.String(256),default='这个人很懒，什么都没留下')##个性签名


##产品信息，有userId则为购物车产品，有orderid则为订单产品
class Product(CommonModel,db.Model):
    orderId=db.Column(db.Integer,default=0)##所属订单
    title= db.Column(db.String(64))
    main_image=db.Column(db.String(4096)) ##主图格式[图片1，图片2]
    detail_image=db.Column(db.String(4096))##详情页图[图片1，图片2]
    image800=db.Column(db.String(512))##800*800展示图
    image400=db.Column(db.String(512))
    image200=db.Column(db.String(512))
    image100 = db.Column(db.String(512))
    category=db.Column(db.String(4))
    price = db.Column(db.Float)
    sales = db.Column(db.Integer) ##销售件数
    store = db.Column(db.Integer) ##库存
    brownCount = db.Column(db.Integer)  ##浏览次数
    # detail = db.Column(db.String(2048)) ##详情页
    size=db.Column(db.String(64))       ##尺寸
    color=db.Column(db.String(64))      ##颜色Category
    category=db.Column(db.String(16))   ##类别
    number=db.Column(db.Integer)        ##购物车里产品数量
    productid = db.Column(db.Integer)  ##订单或者购物车产品时，该字段存产品id
    propId=db.Column(db.Integer) ##产品属性id，对应skuthird对应的主键



##收货地址，有order则为订单地址
class Address(CommonModel,db.Model):
    orderId = db.Column(db.Integer)  ##所属订单
    receiver= db.Column(db.String(64))
    mobile=db.Column(db.String(128))
    address=db.Column(db.String(128)) ##地址
    area=db.Column(db.String(64)) ##街道门牌
    default = db.Column(db.Boolean)##是否为默认地址
    userId=db.Column(db.Integer)##所属用户

class Order(CommonModel,db.Model):
    orderNo=db.Column(db.String(128))               ##唯一订单号
    pruductPriceCount=db.Column(db.Float)          ## 订单总金额
    discount = db.Column(db.Float)                 ## 折扣金额
    yunfei = db.Column(db.Float)                   ## 运费
    orderRemark = db.Column(db.String(512))              ## 备注
    mount = db.Column(db.Float)                    ## 支付金额
    orderStatus = db.Column(db.Integer,default=0)            ## 订单状态1待付款，2待收货，3待评价,4售后,9关闭订单，5已付款（待发货）,6订单完成
    logisticsNo=db.Column(db.String(64))  ##物流单号
    userId = db.Column(db.Integer)  ##所属用户
    addressId= db.Column(db.Integer)
    def addProdutcts(self,list=[]):
        for product in list:
            p=Product_Order();
            p.productid=product.productid
            p.orderid=self.id
            p.propid=product.propid
            p.mount=product.mount
            p.add()
    def addAddress(self,address):
        address.orderid=self.id
        a=Address()
        a.orderid=self.id
        a.mobile=address.mobile
        a.address=address.address
        a.area=address.area
        a.add()

##订单-商品表
class Product_Order(CommonModel, db.Model):
    orderid=db.Column(db.Integer)##订单ID
    productid = db.Column(db.Integer)  ## 产品ID
    propid = db.Column(db.Integer,default=0)  ##产品属性
    mount = db.Column(db.Integer)  ##产品数量
    basename=db.Column(db.String(128))##sku属性1
    funame=db.Column(db.String(128))##sku属性2

##订单-商品详情视图
class product_order_v( CommonModel,db.Model):
    orderid=db.Column(db.Integer)##订单ID
    productid = db.Column(db.Integer)  ## 产品ID
    propid = db.Column(db.Integer,default=0)  ##产品属性
    mount = db.Column(db.Integer)  ##产品数量
    basename=db.Column(db.String(128))
    funame=db.Column(db.String(64))
    title=db.Column(db.String(64))
    main_image=db.Column(db.String(64))
    image800 = db.Column(db.String(64))
    image400 = db.Column(db.String(64))
    price = db.Column(db.Float)
    size = db.Column(db.String(64))
    color = db.Column(db.String(64))





class PayRecord(CommonModel,db.Model):
    tradeNo= db.Column(db.String(64))   ## 业务订单号
    totalFee=db.Column(db.String(64))  ##支付金额
    transactionId=db.Column(db.String(64)) ##支付订单号
    attach=db.Column(db.String(64))  ##用户回传数据
    returnstring=db.Column(db.String(4086))  ##回调报文

class Car(CommonModel, db.Model):  ##购物车
    productid = db.Column(db.Integer)  ## 产品Id
    mount = db.Column(db.Integer)  ## 产品件数
    userid=db.Column(db.Integer)  ## 所属用户
    propid=db.Column(db.Integer)  ##产品属性


class Brown_his(CommonModel, db.Model):  ##浏览历史
    productid = db.Column(db.Integer)  ## 产品Id
    # mount = db.Column(db.Integer)  ## 产品件数
    userid=db.Column(db.Integer)  ## 所属用户

class User2product(CommonModel, db.Model):  ##收藏夹
    productid = db.Column(db.Integer)  ## 产品Id
    # mount = db.Column(db.Integer)  ## 产品件数
    userid=db.Column(db.Integer)  ## 所属用户
    operate=db.Column(db.Integer,default=0) ##操作 1,浏览，2收藏

# class Category(CommonModel, db.Model):
#     cid=db.Column(db.String(32))## 类别ID，f开头一级类，s开头二级类，t开头三级类，fo开头 四级类
#     pid=db.Column(db.String(32)) ## 父级id
#     name=db.Column(db.String(32)) ##类别名
#     picture=db.Column(db.String(1024)) ##图标


class Category(CommonModel, db.Model):
    cid=db.Column(db.Integer)## 类别ID，f开头一级类，s开头二级类，t开头三级类，fo开头 四级类
    pid=db.Column(db.Integer) ## 父级id
    name=db.Column(db.String(32)) ##类别名
    picture=db.Column(db.String(1024)) ##图标
    hasChild=db.Column(db.String(16))##是否有子节点

##好评返现表
class Haopin(CommonModel, db.Model):
    mobile=db.Column(db.String(32))## 收货手机号
    orderid=db.Column(db.String(64)) ## 订单号
    pictures=db.Column(db.String(2048)) ##晒图
    awardid=db.Column(db.Integer) ##奖品id
    award = db.Column(db.String(1024))  ##奖品
    zhifubao = db.Column(db.String(128))  ##支付宝账号
    zhifubaoName= db.Column(db.String(128))  ##支付宝户名

##商品评价
class Rate(CommonModel, db.Model):
    userid=db.Column(db.String(32))## 用户
    rate=db.Column(db.Integer) ## 评价星级
    describeRate=db.Column(db.Integer) ## 描述分
    logisticsRate=db.Column(db.Integer)## 物流分
    serviceRate=db.Column(db.Integer)## 服务分
    evaluate=db.Column(db.String(256))## 评价内容
    content=db.Column(db.String(2048)) ##评价内容
    orderid=db.Column(db.Integer) ## 订单id
    award = db.Column(db.String(1024))  ##奖品
    productid = db.Column(db.Integer)  ##产品
    propid=db.Column(db.Integer)##评价对应的产品属性
    basename = db.Column(db.String(256))  ##评价对应的产品属性
    funame = db.Column(db.String(256))  ##评价对应的产品属性


##商品一级属性
class Skufirst(CommonModel, db.Model):
    productid=db.Column(db.String(32))## 产品id
    baseid=db.Column(db.Integer) ## 主属性id
    basename=db.Column(db.String(128)) ##主属性名称
    fuid = db.Column(db.Integer)  ## 附属性id
    funame = db.Column(db.String(128))  ##附属性名称
##商品二级属性
class Skusecond(CommonModel, db.Model):
    productid=db.Column(db.String(32))## 产品id
    propertyid=db.Column(db.Integer) ## 属性id
    propertyname=db.Column(db.String(128)) ##属性名称
    firstid=db.Column(db.Integer) ##属性父级id


##商品属性库存-价格表
class Skuthird(CommonModel, db.Model):
    productid=db.Column(db.String(32))##产品id
    baseid = db.Column(db.Integer)  ## 主属性id
    basename = db.Column(db.String(128))  ##主属性名称
    fuid = db.Column(db.Integer)  ## 附属性id
    funame = db.Column(db.String(128))  ##附属性名称
    price= db.Column(db.Float)
    store=db.Column(db.Integer)
    pic=db.Column(db.String(128))  ##sku主图

##首页图片属性表
class Images(CommonModel, db.Model):
    name=db.Column(db.String(128))##图片名称
    url = db.Column(db.String(1024))  ## 图片链接
    yongtu = db.Column(db.String(512))  ##图片用途
    pic = db.Column(db.String(256))  ##图片

###系统参数表
class PYSHOP_CONSTANT(CommonModel, db.Model):
    key=db.Column(db.String(64))
    value=db.Column(db.String(128))

###----------------企业网站表-----------------------------------------------------------------------------------------
##公司介绍
class Net_CompanyInfo(CommonModel, db.Model):
    introduce=db.Column(db.String(2048))##公司简介
    # introduceContent= db.Column(db.String(1024))
    culture = db.Column(db.String(2048))  ## 企业文化
    yongtuCompany = db.Column(db.String(512))  ##公司图片
    yongtuculture = db.Column(db.String(512))  ##文化图片

##公司荣誉
class Net_Honour(CommonModel, db.Model):
    time=db.Column(db.String(128))##时间
    content= db.Column(db.String(1024))##内容

## 产品信息
class Net_ProductInfo(CommonModel, db.Model):
    name=db.Column(db.String(128))##产品名称
    title = db.Column(db.String(1024))  ## 产品标题/简介
    picture = db.Column(db.String(512))  ##产品图片
    buy_url = db.Column(db.String(512))  ##购买链接

##类别
class Net_Category(CommonModel, db.Model):
    keyid=db.Column(db.Integer)##类别名称
    keyname = db.Column(db.String(128))  ##名称
    pid=db.Column(db.Integer,default=0)##父级id
    type=db.Column(db.Integer,default=0)##0,产品类别，1，新闻类别

##企业网站表 联系我们
class Net_Contact(CommonModel, db.Model):
    pic = db.Column(db.String(128))  ##大图
    zh_company = db.Column(db.String(521))  ## 中文名称
    en_company = db.Column(db.String(128))  ##英文公司名称
    email = db.Column(db.String(128))  ##邮箱
    phone = db.Column(db.String(128))  ##电话
    x = db.Column(db.String(32))  ##坐标x
    y= db.Column(db.String(32))  ##坐标y

# class Net_MessageBoard(CommonModel, db.Model):
#     name=db.Column(db.String(128))##姓名
#     mobile = db.Column(db.String(521))  ## 手机
#     email = db.Column(db.String(128))  ##邮箱
#     advice = db.Column(db.String(128))  ##建议

##企业网站表 留言板
class Net_MessageBoard(CommonModel, db.Model):
    name=db.Column(db.String(128))##姓名
    mobile = db.Column(db.String(521))  ## 手机
    email = db.Column(db.String(128))  ##邮箱
    advice = db.Column(db.String(128))  ##建议

# ##企业网站表 联系我们
# class Net_Contact(CommonModel, db.Model):
#     phone = db.Column(db.String(128))  ##电话
#     address = db.Column(db.String(521))  ## 地址
#     point = db.Column(db.String(128))  ##地图坐标
#     email = db.Column(db.String(128))  ##邮箱





##企业网站表 行业动态
class Net_News(CommonModel, db.Model):
    title=db.Column(db.String(128))##新闻标题
    date = db.Column(db.String(128))  ##新闻日期
    content = db.Column(db.String(1024))  ## 新闻内容
    author = db.Column(db.String(512))  ##新闻作者
    pic= db.Column(db.String(256)) ##图片

##----------------------------------外部模块使用------------------------------------------------------
class PZH_CONSTANT(CommonModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    erpVersion=db.Column(db.String(32))
# abc=User()
# cc=abc.all()
# print("dd")
##生成model
#flask-sqlacodegen "mysql+pymysql://lanjie:Lj123456@rm-m5e86q52h5lpu678evo.mysql.rds.aliyuncs.com/lanjie" --tables car --outfile "test1.py"  --flask 根据数据库生成model(表名大小写敏感)
##新建表
db.create_all()
# print(int(time.time()*1000))


