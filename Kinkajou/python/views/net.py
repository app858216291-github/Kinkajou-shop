# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect,request,jsonify,make_response,session

from common import tools
from model.models import *
from model.netModels import *
from sqlalchemy import or_, and_, desc
from model.modelBase import Jsonfy
from common.tools import IOUtil,shopUtil
from common.Decorator import is_login
import  random
from model.modelBase import cache

net = Blueprint('net',__name__)

@net.route('/addMessage', methods=['POST','GET'])
def addMessage():
    messageBoard=Net_MessageBoard()
    messageBoard=tools.IOUtil.request2Obj(messageBoard,request)
    messageBoard.add()
    return Jsonfy(data=messageBoard,code=1).__str__()

@net.route('/addJoin', methods=['POST','GET'])
def addJoin():
    join=Net_Join()
    join=tools.IOUtil.request2Obj(join,request)
    join.add()
    return Jsonfy(data=join,code=1).__str__()


