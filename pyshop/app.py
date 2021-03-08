# -*- coding: utf-8 -*-
# demo03_SQLAlchemy.py
from datetime import datetime
from flask import request,current_app
from flask_cors import CORS
from common.tools import IOUtil as io
from model.modelBase import app as app_model
from views.user import user
from views.product import product
from views.order import order
from views.common_v import common_v
from views.tuling import tuling
from views.weixin import wx

import logging
app = app_model
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(product, url_prefix='/product')
app.register_blueprint(order, url_prefix='/order')
app.register_blueprint(tuling, url_prefix='/tuling')
app.register_blueprint(common_v, url_prefix='/common')
app.register_blueprint(wx, url_prefix='/wx')
CORS(app)

# @app.after_request
# def cors(environ):
#     environ.headers['Access-Control-Allow-Origin']='*'
#     environ.headers['Access-Control-Allow-Method']='*'
#     environ.headers['Access-Control-Allow-Headers']='x-requested-with,content-type'
#
#     # str2="返回数据"+str(environ.data)
#     # io.logger(str2)
#     return environ
@app.before_request
def before():
    # print(request.json)
    logStr="请求路径"+request.path+"   请求数据get:" + request.args.__str__()+"    请求数据：post"+request.form.__str__(),"    请求数据：body"+request.data.__str__()
    # print(logStr)


@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    # aa=globals()
    # bb=locals()
    app.run(host='0.0.0.0', port=5000,debug=True,)
    # CORS(app)
