# -*- coding: utf-8 -*-
# demo03_SQLAlchemy.py
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
import json, time
import sys

sys.path.append("E:\codes\python\pyshop")
from model.modelBase import db, CommonModel
from flask_login import UserMixin


###----------------量化交易后台表-----------------------------------------------------------------------------------------

class Quant_RecommendStock(CommonModel, db.Model):
    code = db.Column(db.String(32))  ##股票编码
    codeName = db.Column(db.String(64))  ##股票名称
    date=db.Column(db.String(512)) ##日期
    roa = db.Column(db.Float)  ##上个季度roa
    PER=db.Column(db.Float) ##市盈率
    size=db.Column(db.Integer)##建议购买股数（满仓十万，算出ATR值）
    price=db.Column(db.Float)##当天价格
    nextday=db.Column(db.Float)##第二天价格
    nextday2 = db.Column(db.Float)  ##第三天价格
    nextday3 = db.Column(db.Float)  ##第四天价格
    price_now = db.Column(db.Float)  ##最新价格
    is_buy = db.Column(db.Boolean)  ##是否建仓
    kd=db.Column(db.Float)##当前KD值
    macd=db.Column(db.Float)##当前macd值

class Quant_Order(CommonModel, db.Model):
    code = db.Column(db.String(32))  ##股票编码
    codeName = db.Column(db.String(64))  ##股票名称
    position = db.Column(db.Integer)  ##当前仓位
    buyNow=db.Column(db.Boolean) ##是否急卖
    sellNow = db.Column(db.Boolean)  ##是否急卖
    buyAfter=db.Column(db.Float) ##委托买
    sellAfter=db.Column(db.Float)##委托卖
    monut=db.Column(db.Integer)##交易数量
    status=db.Column(db.Integer)##状态 1，正常，2，作废，3，交易完成

##股票池
class Quants(CommonModel, db.Model):
    code = db.Column(db.String(32))  ##股票编码
    codeName = db.Column(db.String(64))  ##股票名称
    roe=db.Column(db.Float)##市净率
    pe=db.Column(db.Float)##市盈率
    shizhi=db.Column(db.Float)##市值
    des=db.Column(db.Text)##描述
    attr1= db.Column(db.String(128))
    attr2 = db.Column(db.String(128))
    attr3 = db.Column(db.String(128))
    attr4 = db.Column(db.String(128))
    attr5 = db.Column(db.String(128))
    attrFloat1 = db.Column(db.Float)
    attrFloat2 = db.Column(db.Float)
    attrFloat3 = db.Column(db.Float)
    attrFloat4 = db.Column(db.Float)
    attrFloat5 = db.Column(db.Float)
    isBuy=db.Column(db.Boolean)##是否加入股票池
    refresTime=db.Column(db.DateTime)##时间

db.create_all()
# print(int(time.time()*1000))


