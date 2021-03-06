from flask_admin.menu import MenuLink
from flask_babelex import Babel

from model.QuantAdminModels import *
from model.modelBase import app as app_model
from model.adminModels import *
from model.NetAdminModels import *
from service.ShopService import ShopService
from views.timer import timer
from views.user import user
from views.product import product
from views.order import order
from views.net import net
from views.common_v import common_v
#from views.tuling import tuling
from views.weixin import wx
from views.admin import MyAdminIndexView
from model.modelBase import cache,db
from admin.opencode import MXFileAdmin
from flask_ckeditor import CKEditor, CKEditorField
import os.path as op
from flask import request,current_app
from flask_cors import CORS
from model.models import User,Address
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
app.register_blueprint(net, url_prefix='/net')
app.register_blueprint(timer, url_prefix='/timer')

CORS(app)


##flask-admin
from flask_admin import Admin, BaseView, expose
admin=Admin(app,index_view=MyAdminIndexView(), base_template='my_master.html',template_mode='bootstrap3')
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
# admin.add_view(TO_DO_List_Admin(db.session,name="待办事项", endpoint='admin2.todo'))
# admin2 = Admin(app, url='/system_7', endpoint='system_7')


###商城后台  登录用户名：admin
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

###网站相关 登录用户名：home
admin.add_view(Index_Images_Admin(db.session,name="首页轮播图", endpoint='home.image',category="网站首页"))
admin.add_view(Net_Index_Admin(db.session,name="首页信息", endpoint='home.index',category="网站首页"))
admin.add_view(Net_OtherBussiness_Admin(db.session,name="合作伙伴-核心业务", endpoint='home.other',category="网站首页"))


admin.add_view(CompanyInfo_Admin(db.session,name="企业信息", endpoint='admin.companyInfo',category="公司介绍"))
admin.add_view(Honour_Admin(db.session,name="企业荣誉", endpoint='admin.honour',category="公司介绍"))


admin.add_view(News_Category_Admin(db.session,name="新闻类别", endpoint='admin.new.category',category="新闻动态"))
admin.add_view(News_Admin(db.session,name="新闻列表", endpoint='admin.new.list',category="新闻动态"))

admin.add_view(Net_Product_Category_Parent_Admin(db.session,name="产品类别-父类", endpoint='admin.product.parent',category="产品展示"))
#admin.add_sub_category(name="类别维护", parent_name="产品展示")
#admin.add_link(Net_Product_Category_Parent_Admin(db.session,name="父类维护", endpoint='admin.product.parent',category="类别维护"))
admin.add_view(Net_Product_Category_Child_Admin(db.session,name="产品类别-子类", endpoint='admin.product.child',category="产品展示"))
admin.add_view(Net_Product_Admin(db.session,name="产品维护", endpoint='admin.net.product',category="产品展示"))


admin.add_view(Net_Join_Page_Admin(db.session,name="内容编辑", endpoint='admin.joinPage',category="品牌招商"))
admin.add_view(Net_Join_Admin(db.session,name="加盟留言", endpoint='admin.join',category="品牌招商"))
admin.add_view(Contact_Admin(db.session,name="联系信息", endpoint='admin.contact',category="联系我们"))
admin.add_view(MessageBoard_Admin(db.session,name="留言板", endpoint='admin.messageBoard',category="联系我们"))

admin.add_view(Quant_Order_Admin(db.session,name="订单管理", endpoint='stock.order',category="实盘"))
admin.add_view(Quants_Admin(db.session,name="股票池", endpoint='stock.quants',category="实盘"))
admin.add_view(Quant_Recommend_Admin(db.session,name="推荐股票", endpoint='stock.recommend',category="推荐"))

# admin.add_view(CompanyInfo_Admin(db.session,name="企业信息", endpoint='admin.companyInfo',category="产品展示"))
# admin.add_view(CompanyInfo_Admin(db.session,name="企业信息", endpoint='admin.companyInfo',category="新闻动态"))
# admin.add_view(CompanyInfo_Admin(db.session,name="企业信息", endpoint='admin.companyInfo',category="品牌招商"))



# admin.add_view(CompanyInfo_Admin(db.session,name="企业信息", endpoint='admin.companyInfo',category="企业信息"))
# admin.add_view(Honour_Admin(db.session,name="企业荣誉", endpoint='admin.honour',category="企业荣誉"))
# admin.add_view(Contact_Admin(db.session,name="联系我们", endpoint='admin.contact',category="联系我们"))
# admin.add_view(MessageBoard_Admin(db.session,name="留言板", endpoint='admin.messageBoard',category="留言板"))
# admin.add_view(News_Admin(db.session,name="企业新闻", endpoint='admin.news',category="企业新闻"))
##三级导航
# admin.add_sub_category(name="Links", parent_name="网站管理")
# admin.add_link(MenuLink(name='Home Page', url='/', category='Links'))
# admin.add_view(Net_Join_Admin(db.session,name="加盟", endpoint='admin.join',category="网站管理"))
# admin.add_view(Net_MessageBoard_Admin(db.session,name="留言", endpoint='admin.messgaeBoard',category="网站管理"))


admin.add_view(WorkFlow_Admin(db.session,name="OA流程控制", endpoint='admin.oaflow',category="外部系统管理"))
##系统相关
admin.add_view(Images_Admin(db.session,name="系统图片", endpoint='admin.images',category="系统管理"))
admin.add_view(PYSHOP_CONSTANT_Admin(db.session,name="系统变量", endpoint='admin.cons',category="系统管理"))
admin.add_view(TO_DO_Type_Admin(db.session,name="待办类型编辑", endpoint='admin.todotpye',category="系统管理"))
admin.add_view(DictConfig_Admin(db.session,name="系统字典", endpoint='admin.dict',category="系统管理"))
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
    # print(csrf_token)
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
    print("进入")
    api_name = request.url
    ips = request.headers.getlist("X-Forwarded-For")
    ips.append(request.remote_addr)
    try:
        logStr = "请求路径" + request.path + "   请求数据get:" + request.args.__str__() + "    请求数据：post" + request.form.__str__(), "    请求数据：body" + request.data.__str__()
        print('before_request:', ips, api_name, logStr)
    except :
        print('before_request:', ips, api_name)
    ##黑名单处理
    blacklist=ShopService.getSysConfig("blacklist")
    blacklist=blacklist.split(',')
    for ip in ips:

        if blacklist.__contains__(ip):
            print("该IP已被列入黑名单", ip)
            return "0"


@app.route('/')
def hello_world():

   # app.logger.info("Info message")
   # app.logger.warning("Warning msg")
   # app.logger.error("Error msg!!!")

   # from flask import current_app
    #current_app.logger.info("simple page info...")
    #current_app.logger.warning("warning msg!")
   # current_app.logger.error("ERROR!!!!!")
    return redirect(url_for('admin.index'))
    #return 'Hello World!'

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
    return current_app.send_static_file('favicon.ico')

def getUserNameFromId(id):
    if id==None or id=="":
        return ""
    user=User().get(id)
    if user == None:
        return ""
    return str(user.name)
def getAddressFormId(id):

    if id==None or id=="":
        return ""
    address=Address().get(id)
    return address.receiver+"  "+address.mobile
# 全局错误AOP处理
@app.errorhandler(Exception)
def framework_error(e):
    print("异常")
    api_name = request.url
    ips = request.headers.getlist("X-Forwarded-For")
    ips.append(request.remote_addr)
    # ip = str(request.headers.getlist("X-Forwarded-For"))
    print("error info: %s" % e) # 对错误进行日志记录
    content=str(ips)+" "+api_name+" "+str("error info: %s" % e)
    print("异常2")
    print(content)
    # ShopService.sys_notify(content, "k-shop系统异常提醒")

app.jinja_env.globals.update(getUserNameFromId=getUserNameFromId,getAddressFormId=getAddressFormId)
