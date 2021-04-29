from flask_babelex import Babel

from model.modelBase import app as app_model
from model.adminModels import User_Admin, Address_Admin, Category_Admin, Order_Admin, Product_Admin, PayRecord_Admin, User2product_Admin, Images_Admin,TO_DO_List_Admin,TO_DO_Type_Admin
from views.user import user
from views.product import product
from views.order import order
from views.common_v import common_v
from views.tuling import tuling
from views.weixin import wx
from views.admin import MyAdminIndexView
from model.modelBase import cache,db
from admin.opencode import MXFileAdmin
from flask_ckeditor import CKEditor, CKEditorField
import os.path as op
from flask import request,current_app
from flask_cors import CORS
from model.models import User
from werkzeug.security import generate_password_hash, check_password_hash
import flask_login as login
from flask_admin.contrib import sqla
from flask import Flask, url_for, redirect, render_template, request

app = app_model
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(product, url_prefix='/product')
app.register_blueprint(order, url_prefix='/order')
# app.register_blueprint(tuling, url_prefix='/tuling')
app.register_blueprint(common_v, url_prefix='/common')
app.register_blueprint(wx, url_prefix='/wx')
CORS(app)


##flask-admin
from flask_admin import Admin, BaseView, expose
admin=Admin(app,index_view=MyAdminIndexView(), base_template='my_master.html',template_mode='bootstrap3')
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
# admin.add_view(TO_DO_List_Admin(db.session,name="待办事项", endpoint='admin2.todo'))
# admin2 = Admin(app, url='/system_7', endpoint='system_7')



#admin.add_view(MyView(name=u'Hello'))
# admin.add_view(ModelView(Product, db.session, endpoint='admin.product',category="产品管理",name="产品信息"))
admin.add_view(Product_Admin( db.session, endpoint='admin.product',category="产品管理",name="产品信息"))

admin.add_view(Category_Admin( db.session, endpoint='admin.category',category="产品管理",name="产品类别"))

admin.add_view(User_Admin(db.session,name="用户信息", endpoint='admin.user',category="用户管理"))
admin.add_view(User2product_Admin(db.session,name="收藏信息", endpoint='admin.User2product',category="用户管理"))
admin.add_view(Address_Admin(db.session,name="用户地址", endpoint='admin.address',category="用户管理"))
admin.add_view(Order_Admin(db.session,name="订单记录", endpoint='admin.order',category="订单管理"))
admin.add_view(PayRecord_Admin(db.session,name="收款记录", endpoint='admin.payrecord',category="订单管理"))
admin.add_view(TO_DO_List_Admin(db.session,name="待办事项", endpoint='admin.todo'))


# admin.add_view(ImageView(db.session, endpoint='admin.product2',category="产品管理",name="产品信息"))


admin.add_view(Images_Admin(db.session,name="系统图片", endpoint='admin.images',category="系统管理"))
admin.add_view(TO_DO_Type_Admin(db.session,name="待办类型编辑", endpoint='admin.todotpye',category="系统管理"))

path = op.join(op.dirname(__file__), '../static/fileServer')
admin.add_view(MXFileAdmin(path, '/fileServer/', name='文件管理系统',category="系统管理"))
ckeditor = CKEditor(app)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'

# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)
init_login()
# Create admin


# Add view
# admin.add_view(MyModelView(User, db.session,endpoint='admin.user2'))

##日志---start----
import logging
from logging.handlers import TimedRotatingFileHandler

logger_sql = logging.getLogger('sqlalchemy.engine')  # 记录sql 到文件

handler = TimedRotatingFileHandler( "log/flask.log", when="D", interval=1, backupCount=15,encoding="UTF-8", delay=False, utc=True)
sql_handler = TimedRotatingFileHandler( "log/sql.log", when="D", interval=1, backupCount=15,encoding="UTF-8", delay=False, utc=True)

logging_format = logging.Formatter('localhost-%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
sql_handler.setFormatter(logging_format)
# handler.setLevel(logging.INFO)
# logging.basicConfig(level = logging.DEBUG)

logger_sql.addHandler(sql_handler)##sql日志文件
app.logger.addHandler(handler)
app.logger.level=logging.DEBUG

####添加CsrfProtect保护
from flask_wtf.csrf import CsrfProtect
CsrfProtect(app)

@app.after_request
def cors(response):
    from flask_wtf.csrf import generate_csrf
    csrf_token = generate_csrf()
    print(csrf_token)
    # 设置cookie传给前端
    response.set_cookie('csrf_token', csrf_token)
    return response
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
    # print(request.path)
    # request.path=request.path.replace('\\', '/')
    # print(request.path)
    logStr="请求路径"+request.path+"   请求数据get:" + request.args.__str__()+"    请求数据：post"+request.form.__str__(),"    请求数据：body"+request.data.__str__()
    #app.logger.info(logStr)


@app.route('/')
def hello_world():

   # app.logger.info("Info message")
   # app.logger.warning("Warning msg")
   # app.logger.error("Error msg!!!")

   # from flask import current_app
    #current_app.logger.info("simple page info...")
    #current_app.logger.warning("warning msg!")
   # current_app.logger.error("ERROR!!!!!")

    return 'Hello World!'

@app.route('/cache')
@cache.cached()##缓存视图
def test_cache():
    cache.set('name', 'xiaoming', timeout=30)##缓存数据，并设置超时时间，不设置时间为不超时
    cache.set('person', {'name': 'aaa', 'age': 20})##缓存对象
    x = cache.get('name')
    print(x)
    cache.set_many([('name1', 'hhh'), ('name2', 'jjj')])##多值缓存，
    print(cache.get_many("name1", "name2"))
    print(cache.delete("name"))##删除缓存
    print(cache.delete_many("name1", "name2"))
    return "cache is success"

@app.route('/favicon.ico')
def get_fav():
    print(__name__)
    return current_app.send_static_file('/favicon.ico')


