# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect,request,jsonify
import model.models as models
from model.models import User,Address,Order,Product,PayRecord
from sqlalchemy import or_,and_
from model.modelBase import Jsonfy,JsonUtil
import json
from common.tuling import TuLing
import re
tuling = Blueprint('tuling',__name__)

@tuling.route('/index', methods=['POST','GET'])
def index():
    # orderBak = OrderBak().get(654674)

    return "as"


    result = "内部单号：" + str(orderBak.insideid) + "\n 快递单号：" + orderBak.logistics + "\n 手机号码：" + orderBak.mobile + "\n " + orderBak.address + "\n 客户：" + orderBak.customer + "\n 产品：" + orderBak.products + "\n 订单时间：" + orderBak.orderTime + "\n"
    return result

@tuling.route('/getList', methods=['POST','GET'])
def getList():
    pageNo = request.args.get("page")
    pageSize = request.args.get("limit")
    # pageSize = request.args.get("limit")
    kk=TuLing.getList(pageNo,pageSize)
    data=kk['faqList']
    count = kk['totalCount']
    return Jsonfy(data=data,count=count).__str__()

@tuling.route('/add', methods=['POST','GET'])
def add():
    # pageNo = request.args.get("page")
    answer=request.args.get("answer")
    question=request.args.get("question")
    kk=TuLing.add(answer,question)
    return Jsonfy(data=kk).__str__()

@tuling.route('/delete', methods=['POST','GET'])
def delete():
    faqId=request.args.get("faqId")
    kk=TuLing.delete(faqId)
    return Jsonfy(data=kk).__str__()


@tuling.route('/info', methods=['POST','GET'])
def info():
    kk=TuLing.info("adb")
    return "aa"


