# -*- coding: utf-8 -*-
import copy

from flask import Blueprint, render_template, redirect,request,jsonify
import model.models as models
from model.models import User,Address,Order,Product,PayRecord,Product_Order,Skuthird,product_order_v
from sqlalchemy import or_, and_, desc
from model.modelBase import Jsonfy,JsonUtil
import json
from common.tools import IOUtil,shopUtil
from common.Decorator import is_login
order = Blueprint('order',__name__)





@order.route('/index', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        data = request.args
    elif request.method=='POST':
        data=request.form

    p1 = User(name="rewqq")
    p1.updateOrAdd();
    return "as"
@order.route('/addorder', methods=['POST','GET'])
def addorder():

    productList=request.args.get('products')
    address = request.args.get('address')
    orderRemark= request.args.get('orderRemark')

    productListTemp=[]
    productList=json.loads(productList)
    address=json.loads(address)
    mount=1


    for product in productList:
        product2=Product().get(product.get('id'))
        p = Product_Order()
        p.mount=product.get('mount')
        p.productid=product.get('id')
        p.propid=product.get("propid")
        if p.propid==0 or p.propid=='0':
            mount = product.get('price') * mount
        else:
            mount = Skuthird().get(p.propid).price*p.mount
            sku= Skuthird().get(p.propid)
            p.basename=sku.basename
            p.funame = sku.funame
        productListTemp.append(p)

    address=Address().get(address.get("id"))

    order = Order()
    order.orderRemark=orderRemark
    order.mount=mount
    order.userId=shopUtil.getUserId(request)
    order.orderStatus=1
    order.addressId =address.id
    order.orderNo=IOUtil.orderNo()
    order.add()
    order.addProdutcts(productListTemp)
    order.addAddress(address)

    print(Jsonfy(data=Order().get(order.id).tojson()).__str__())

    return Jsonfy(data=order.tojson()).__str__()
    #     # return r.__str__()

@order.route('/orders', methods=['POST','GET'])
@is_login
def orders():
    orderStatus=request.args.get("orderStatus")
    orderid = request.args.get("orderid")
    needHelp=request.args.get("needHelp")
    if str(needHelp)=='1':
        needHelp = 1
    elif str(needHelp)=='0':
        needHelp = 0
    query = Order().query.filter(Order.userId == shopUtil.getUserId(request))
    if orderStatus != None and orderStatus != '0' and orderStatus != 0:
        query=query.filter(Order.orderStatus== orderStatus)
    if orderid != None and orderid != '0' and orderid != 0:
        query = query.filter(Order.id== orderid)
    if needHelp != None and needHelp != '':
        query = query.filter(Order.needHelp== needHelp)
    # if orderStatus!=None and orderStatus!='0' and orderStatus!=0:
    #     query=Order().query.filter(Order.userId==shopUtil.getUserId(request)).filter(Order.orderStatus== orderStatus).order_by(desc(Order.create_time))
    # elif orderid!=None and orderid!='0' and orderid!=0:
    #     query = Order().query.filter(Order.userId == shopUtil.getUserId(request)).filter(
    #         Order.id == orderid).order_by(desc(Order.create_time))
    # else:
    #     query=Order().query.filter(Order.userId==shopUtil.getUserId(request)).order_by(desc(Order.create_time))
    query.order_by(desc(Order.create_time))
    print(query)
    orders=Order().paginate(query,pageSize=10)
    for order in orders.items:
        products=product_order_v().query.filter(product_order_v.orderid==order.id).all();

        order.products=products
        if(order.orderStatus==1):
            # tradeNo=str(order.orderNo)
            payrecords=PayRecord().filter(PayRecord.tradeNo==order.orderNo)
            if len(payrecords) > 0:
                order.orderStatus=2
                # order.updateOrAdd()
    # orders=Order().query.filter(Order).order_by(Order.create_time).all()

    return Jsonfy(data=orders.items,count=orders.total).__str__()


@order.route('/pay', methods=['POST','GET'])
def pay():
    orderId = request.args.get('orderId')
    orderNo = request.args.get('orderNum')
    order=Order().query.filter(Order.orderNo==orderNo).first();
    if order==None:
        order=Order().get(orderId)
    order.orderStatus=2
    order.updateOrAdd()
    return Jsonfy().__str__()

@order.route('/needhelp', methods=['POST','GET'])
def needhelp():
    orderid = request.args.get('orderid')
    type = request.args.get('type')
    desc = request.args.get('desc')
    if type=='仅退款':
        type=0
    if type=='退款退货':
        type=1
    if type=='换货':
        type=2
    if type=='投诉':
        type=3

    order=Order().get(orderid)
    order.needHelp=1
    order.updateOrAdd()
    afterSales= models.AfterSales()
    afterSales.orderId=orderid
    afterSales.type=type
    afterSales.desc=desc
    afterSales.updateOrAdd()

    return Jsonfy().__str__()

@order.route('/cancelHelp', methods=['POST','GET'])
def cancelHelp():
    orderid = request.args.get('orderid')


    order=Order().get(orderid)
    order.needHelp=0
    order.updateOrAdd()


    return Jsonfy().__str__()
#
# @order.route('/addAfterSales', methods=['POST','GET'])
# def afterSales():
#     orderId = request.args.get('orderId')
#     orderNo = request.args.get('orderNum')
#     order=Order().query.filter(Order.orderNo==orderNo).first();
#     if order==None:
#         order=Order().get(orderId)
#     order.orderStatus=2
#     order.updateOrAdd()
#     return Jsonfy().__str__()



@order.route('/changeStatus', methods=['POST','GET'])
@is_login
def changeStatus():
    orderId = request.args.get('orderId')
    orderStatus = request.args.get('orderStatus')
    order=Order().get(orderId)
    order.orderStatus=orderStatus
    order.updateOrAdd()
    return Jsonfy().__str__()

# @order.route('/addtoken', methods=['POST','GET'])
# # @is_login
# def addtoken():
#     token=11
#
#     cache=Cache()
#     cache.set('name', 'xiaoming')
#     return Jsonfy(data=token).__str__()

