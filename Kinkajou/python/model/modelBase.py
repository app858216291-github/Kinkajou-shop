# -*- coding: utf-8 -*-
# demo03_SQLAlchemy.py
import os
import time
from datetime import datetime

import requests
from flask import Flask,jsonify
from flask_admin.contrib.sqla import ModelView
from flask_ckeditor import CKEditorField
from flask_sqlalchemy import SQLAlchemy, Pagination
from markupsafe import Markup
from sqlalchemy import func
from sqlalchemy.sql.sqltypes import DateTime
import json,logging
import pymysql


from setting import FlaskConfig, Aliyun
import flask_login as login
from flask_admin import Admin, form, expose
import logging
##pip install Flask-Caching
from flask_caching import Cache
##pymysql 不支持3.5，所以加这句
pymysql.install_as_MySQLdb()

# app = Flask(__name__,static_folder='/static')
app = Flask(__name__,template_folder='../templates',static_folder='../static', static_url_path='')
app.config.from_object(FlaskConfig)

##多数据源
SQLALCHEMY_BINDS = FlaskConfig.SQLALCHEMY_BINDS
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


cache = Cache(config={'CACHE_TYPE': 'simple'})
# cache1.init_app(app, config={ 'CACHE_TYPE' : 'redis','CACHE_REDIS_HOST':'192.168.1.20','CACHE_REDIS_PORT':'6390'})
cache.init_app(app)

# 3、创建对象
db = SQLAlchemy(app)
# lanjiedb.session.bind = lanjiedb.get_engine(bind='lanjie')
# db=""
class SQLERROR(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, CommonModel):
            return obj.tojson()
        if isinstance(obj, CommonModel_Empty):
            return obj.tojson()
        if isinstance(obj, _Pagination):
            return obj.tojson()
        return json.JSONEncoder.default(self, obj)
class JsonUtil():
    @staticmethod
    def dumps(obj):
        return json.dumps(obj, cls=MyEncoder, ensure_ascii=False)
    @staticmethod
    def loads(jsonStr):
        return json.loads(jsonStr)

class Jsonfy():
    def __init__(self, code=0,msg="sucess",data={},value="0",count=0,has_next=False,has_prev=False):
        self.code = code ##-2 未登录 ，-1 错误，0 默认，1成功
        self.message=msg
        self.data=data
        self.value=value
        self.count=count
        self.has_next=has_next
        self.has_prev=has_prev
    def __str__(self):
        return JsonUtil.dumps(self.__dict__)
class _Pagination():
    def __init__(self,pagination):
        self.page = pagination.page  ##指定页码，从1开始 默认值1
        self.per_page =  pagination.per_page  ## 每一页有几个条记录 默认值20
        self.total =  pagination.total  ## 总数据条数
        self.items = pagination.items  ## 记录内容
        self.has_next= pagination.has_next ##是否还有下一页
        self.has_prev= pagination.has_prev ##是否还有上一页
    ##对象转成json
    def tojson(self):
        result={
                "page":self.page,
                "per_page":self.per_page,
                "total":self.total,
                "items":self.items,
                "has_next": self.has_next,
                "has_prev": self.has_prev
                }
        return result



# 4、定义模型类
class CommonModel():
    # 主键，参数1：表示类型，参数2：约束范围
    id = db.Column(db.Integer, primary_key=True)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    #update_user = db.Column(db.Integer, default=0)
    remark = db.Column(db.String(128))
    # onlineId = Column(String(64))# 线上单号
    status = db.Column(db.Integer, default=0)  ## 0默认，-1错误，-2 数据被删除，1数据加到orderRencent表里
    ##增
    def add(self):
        db.session.add(self)
        # print(str(self))
        db.session.commit()

        return self.id
    ##存在则修改，不存在则增加
    def updateOrAdd(self):
        object = self.query.filter(self.__class__.id == self.id).first()
        if object == None:
            db.session.add(self)
        else:
            dicts = self.__dict__
            for key in dicts:
                if key == "_sa_instance_state" or key == "id":
                    continue
                if hasattr(object, key):
                    setattr(object, key, dicts[key])
                    # object.__dict__[key]=dicts[key]
        db.session.commit()
    ##根据id修改
    def updateById(self):
        dicts=self.__dict__
        object = self.query.filter(self.__class__.id ==self.id).first()
        if object==None:
            raise SQLERROR("表"+self.__class__.__name__+"不存在该ID："+str(self.id))
        for key in dicts:
            if key=="_sa_instance_state" or key=="id":
                continue
            if hasattr(object,key):

                setattr(object,key,dicts[key])
                # object.__dict__[key]=dicts[key]
        db.session.commit()
    ##根据ID删除
    def deleteById(self):
        object = self.query.filter(self.__class__.id == self.id).first()
        if object == None:
            raise SQLERROR("表" + self.__class__.__name__ + "不存在该ID：" + str(self.id))
        db.session.delete(object)
        db.session.commit()

    ##查询所有
    def all(self):
        return self.query.all()
    ##根据ID查询
    def get(self):
        return self.query.get(self.id)
    ##根据ID查询
    def get(self,id):
        return self.query.get(id)

     ##根据条件查询
    def filter(self, filter):
        return self.query.filter(filter).all()

    # 分页查询,
    def paginate(self,query,start=1,pageSize=20):
        return _Pagination(query.paginate(start,pageSize))
    ##对象转成json
    def tojson(self):
        result={}
        dict=self.__dict__
        for i in dict:
            if isinstance(dict[i], int) or isinstance(dict[i], datetime) or isinstance(dict[i], float) or isinstance(dict[i], str) or (type(dict[i]).__name__ == 'list') or (type(dict[i]).__name__ == 'dict')or (type(dict[i]).__name__ == 'set'):
                # print(type(dict[i]))
                result[i]=getattr(self, i)
        return result


class CommonModel_Empty():
    def add(self):

        db.session.add(self)
        # print(str(self))
        db.session.commit()
        return self

    def updateOrAdd(self):
        object = self.query.filter(self.__class__.id == self.id).first()
        if object == None:
            db.session.add(self)
        else:
            dicts = self.__dict__
            for key in dicts:
                if key == "_sa_instance_state" or key == "id":
                    continue
                if hasattr(object, key):
                    setattr(object, key, dicts[key])

        db.session.commit()

    def updateById(self):
        dicts = self.__dict__
        object = self.query.filter(self.__class__.id == self.id).first()
        if object == None:
            raise SQLERROR("表" + self.__class__.__name__ + "不存在该ID：" + str(self.id))
        for key in dicts:
            if key == "_sa_instance_state" or key == "id":
                continue
            if hasattr(object, key):
                setattr(object, key, dicts[key])
                # object.__dict__[key]=dicts[key]
        db.session.commit()

    def deleteById(self):
        object = self.query.filter(self.__class__.id == self.id).first()
        if object == None:
            raise SQLERROR("表" + self.__class__.__name__ + "不存在该ID：" + str(self.id))
        db.session.delete(object)
        db.session.commit()

    def all(self):
        return self.query.all()

    def get(self):
        return self.query.get(self.id)

    def get(self, id):
        return self.query.get(id)

    def filter(self, filter):
        return self.query.filter(filter).all()

    def paginate(self, query, start=1, pageSize=20):
        return _Pagination(query.paginate(start, pageSize))

    def tojson(self):
        result = {}
        dict = self.__dict__
        for i in dict:
            if isinstance(dict[i], int) or isinstance(dict[i], datetime) or isinstance(dict[i], float) or isinstance(
                    dict[i], str) or (type(dict[i]).__name__ == 'list') or (type(dict[i]).__name__ == 'dict') or (
                    type(dict[i]).__name__ == 'set'):
                # print(type(dict[i]))
                result[i] = getattr(self, i)
        return result

import os.path as op
file_path = op.join(op.dirname(__file__), '../static/product')  # 文件上传路径
try:
    os.mkdir(file_path)
except OSError:
    pass
##框架唯一闭源的点，校验注册码
class  BaseModelFormSet(ModelView):
    @staticmethod
    def dectry(p):
        k = 'djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74sd'
        dec_str = ""
        for i, j in zip(p.split("_")[:-1], k):
            temp = chr(int(i) - ord(j))
            dec_str = dec_str + temp
        return dec_str
    @staticmethod
    def p__iter_():
        key=FlaskConfig.key
        key_url=FlaskConfig.key_url
        t1=int(BaseModelFormSet.dectry(key))
        t = time.time()
        t=int(t)
        if t>t1:
            print("system is time out")
            res = requests.get(url=key_url, params={})
            remote = json.loads(res.text)
            key = remote["data"]
            t1=int(BaseModelFormSet.dectry(key))
        t = time.time()
        t=int(t)
        if t>t1:
            exit(-1)
# BaseModelFormSet.p__iter_()
#####以上代码可删除###
class Common_Admin(ModelView):
    def is_accessible(self):
        if login.current_user.is_authenticated:
            if login.current_user.username == 'admin':
                return True
            return False
        return False
    def get_query(self):
        return self.session.query(self.model).filter(self.model.status != -2)
        # return super(MyView, self).get_query().filter(User.username == current_user.username)
    def get_count_query(self):
        """
            Return a the count query for the model type

            A ``query(self.model).count()`` approach produces an excessive
            subquery, so ``query(func.count('*'))`` should be used instead.

            See commit ``#45a2723`` for details.
        """
        return self.session.query(func.count('*')).select_from(self.model).filter(self.model.status != -2)
    page_size = 20
    # 是否可以是设置分页数量
    # can_set_page_size=True
    ##id只读，不允许修改
    form_widget_args = {
        'id': {
            'readonly': True
        }
    }
    column_exclude_list = ("update_time", "remark", "status")
    # can_export = True
    # can_delete = False
    # can_delete = False
    # 删除tab不可见，当时可删除
    action_disallowed_list = ['delete']

    edit_template = 'edit.html'  # 指定编辑记录的模板

    def net_init(self, columns):
        # columnsa = [
        #     ['name', '图片名称', 'text'],
        #     ['url', '跳转链接', 'CKEditorField'],
        #     ['yongtu', '图片用途', 'Select2Field',[('1', '待付款'), ('5', '已付款待发货')]],
        #     ['pic', '图片地址', 'image']
        # ]
        imageAttr = []
        CKEditorAttr = []
        Select2FieldAttr = []

        if self.column_list == None:
            self.column_list = []
        if self.column_labels == None:
            self.column_labels = {}
        if self.form_columns == None:
            self.form_columns = []
        if self.form_overrides == None:
            self.form_overrides = dict()
        if self.form_extra_fields == None:
            self.form_extra_fields = {}
        if self.column_formatters == None:
            self.column_formatters = {}

        for column in columns:
            self.column_labels[column[0]] = column[1]
            self.column_list.append(column[0])
            if column[2] == "image":
                imageAttr.append(column[0])
            if column[2] == "CKEditorField":
                CKEditorAttr.append(column[0])
            if column[2] == "Select2Field":
                Select2FieldAttr.append([column[0], column[1], column[2], column[3]])

        self.form_columns = self.column_list
        ##html编辑器
        for key in CKEditorAttr:
            self.form_overrides[key] = CKEditorField

        ##图片
        def _list_thumbnail(view, context, model, name):
            for image in imageAttr:
                if name == image:
                    if getattr(model, image) == None:
                        return "";
                    return Markup(
                        '<img style="width: 100px" src="https://pyshop.oss-cn-beijing.aliyuncs.com/product/' + getattr(
                            model, image) + '?x-oss-process=image/resize,h_100">')
            for select2Field in Select2FieldAttr:
                if name == select2Field[0]:
                    for tuple_key in select2Field[3]:
                        if getattr(model, name) == tuple_key[0]:
                            return tuple_key[1]

        for key2 in imageAttr:
            from admin.opencode import MxImageUploadField
            self.form_extra_fields[key2] = MxImageUploadField(self.column_labels[key2], base_path=file_path,
                                                              url_relative_path=Aliyun.ReadUrl + 'product/')
            self.column_formatters[key2] = _list_thumbnail
        for select2Field in Select2FieldAttr:
            self.column_formatters[select2Field[0]] = _list_thumbnail
        for select in Select2FieldAttr:
            self.form_extra_fields[select[0]] = form.Select2Field(select[1], choices=select[3], coerce=int)  ##只能值是数字

        ##html编辑器，不支持弹出框编辑
        if CKEditorAttr.__len__() > 0:
            self.edit_modal = False
            self.create_modal = False
            self.create_template = 'create.html'
            self.edit_template = 'edit.html'
            ##html编辑器，不支持弹出框编辑

