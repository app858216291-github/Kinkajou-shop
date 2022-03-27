# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect,request,jsonify,make_response,session
from jqdatasdk import *

from common import tools
from model.models import *
from model.netModels import *
from sqlalchemy import or_, and_, desc
from model.modelBase import Jsonfy
from common.tools import IOUtil,shopUtil
from common.Decorator import is_login
import  random
from model.modelBase import cache
from model.quantModels import Quant_RecommendStock

timer = Blueprint('timer',__name__)


def bkTojq(code='510300.XSHG'):
    if code.find(".sh") != -1 or code.find(".SH") != -1:  ##上海
        code = code.replace(".sh", "")
        code = code.replace(".SH", "")
        code = code + ".XSHG"

    elif code.find(".sz") != -1 or code.find(".SZ") != -1:  ##深圳
        code = code.replace(".sz", "")
        code = code.replace(".SZ", "")
        code = code + ".XSHE"
    return code
##http://127.0.0.1:4999/timer/stockDate?startdate=2021-10-14&enddate=2021-10-15
@timer.route('/stockDate', methods=['POST','GET'])
def stockData():

    startdate = request.args.get("startdate")
    endtdate = request.args.get("enddate")
    quants=Quant_RecommendStock().query.filter(Quant_RecommendStock.date==startdate).filter(Quant_RecommendStock.status!=-2).all()
    auth('13774514086', 'Fmz7670702')
    for quant in quants:
        stock=quant.code
        q = query(valuation.pe_ratio,
                  valuation.pb_ratio
                  ).filter(valuation.code.in_([bkTojq(stock)]))
        df0 = get_fundamentals_continuously(q, end_date=startdate, count=2, panel=False)[:5]
        print(df0)
        df = get_price(bkTojq(stock), start_date=startdate, end_date=endtdate, frequency="daily", fields=None,
                       skip_paused=False, fq='pre')
        print(df)
        if len(df)==4:
            quantNew=Quant_RecommendStock().get(quant.id)
            quantNew.nextday=float(df.iloc[1][1])
            quantNew.nextday2 =float(df.iloc[2][1])
            quantNew.nextday3 =float(df.iloc[3][1])
            quantNew.PER=float(df0.iloc[0][2])
            quantNew.roa=float(df0.iloc[0][3])
            quantNew.updateOrAdd()
        if len(df)==3:
            quantNew=Quant_RecommendStock().get(quant.id)
            quantNew.nextday=float(df.iloc[1][1])
            quantNew.nextday2 =float(df.iloc[2][1])
            quantNew.PER = float(df0.iloc[0][2])
            quantNew.roa=float(df0.iloc[0][3])
            quantNew.updateOrAdd()
        if len(df)==2:
            quantNew=Quant_RecommendStock().get(quant.id)
            quantNew.nextday=float(df.iloc[1][1])
            quantNew.PER = float(df0.iloc[0][2])
            quantNew.roa=float(df0.iloc[0][3])
            quantNew.updateOrAdd()
        if len(df)==1:
            quantNew=Quant_RecommendStock().get(quant.id)
            quantNew.price=float(df.iloc[0][1])
            quantNew.PER = float(df0.iloc[0][2])
            quantNew.roa=float(df0.iloc[0][3])
            quantNew.updateOrAdd()

    return Jsonfy(data=quant,code=1).__str__()



