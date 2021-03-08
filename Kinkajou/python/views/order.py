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
@is_login
def addorder():

    productList=request.args.get('products')
    address = request.args.get('address')
    orderRemark= request.args.get('orderRemark')

    productListTemp=[]
    productList=json.loads(productList)
    address=json.loads(address)
    mount=0


    for product in productList:
        product2=Product().get(product.get('id'))
        p = Product_Order()
        p.mount=product.get('mount')
        p.productid=product.get('id')
        p.propid=product.get("propid")
        if p.propid==0 or p.propid=='0':
            mount = product.get('price') + mount
        else:
            mount = Skuthird().get(p.propid).price+mount
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
    query=""
    if orderStatus!=None and orderStatus!='0' and orderStatus!=0:
        query=Order().query.filter(Order.userId==shopUtil.getUserId(request)).filter(Order.orderStatus== orderStatus).order_by(desc(Order.create_time))
    elif orderid!=None and orderid!='0' and orderid!=0:
        query = Order().query.filter(Order.userId == shopUtil.getUserId(request)).filter(
            Order.id == orderid).order_by(desc(Order.create_time))
    else:
        query=Order().query.filter(Order.userId==shopUtil.getUserId(request)).order_by(desc(Order.create_time))

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

