# -*- coding: utf-8 -*-
# demo03_SQLAlchemy.py
from datetime import datetime
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy, Pagination
from sqlalchemy.sql.sqltypes import DateTime
import json,logging
import pymysql
from setting import FlaskConfig
##pymysql 不支持3.5，所以加这句
pymysql.install_as_MySQLdb()

# app = Flask(__name__,static_folder='/static')
app = Flask(__name__,static_folder='../', static_url_path='')
app.config.from_object(FlaskConfig)


# 3、创建对象
db = SQLAlchemy(app)
lanjiedb = SQLAlchemy(app)
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
    remark = db.Column(db.String(128))
    # onlineId = Column(String(64))# 线上单号
    status = db.Column(db.Integer, default=0)  ## 0默认，-1错误，-2 数据被删除，1数据加到orderRencent表里
    ##增
    def add(self):
        db.session.add(self)
        # print(str(self))
        db.session.commit()
        return self
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





