# -*- coding: utf-8 -*-
# demo03_SQLAlchemy.py
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
import json, time
import sys

sys.path.append("E:\codes\python\pyshop")
from model.modelBase import db, CommonModel
from flask_login import UserMixin


###----------------企业网站表-----------------------------------------------------------------------------------------
##首页
##首页轮播图
class Net_Index_Images(CommonModel, db.Model):
    name=db.Column(db.String(128))##图片名称
    url = db.Column(db.String(1024))  ## 图片链接
    yongtu = db.Column(db.String(512))  ##图片用途
    pic = db.Column(db.String(256))  ##图片


class Net_Index(CommonModel, db.Model):
    brand = db.Column(db.String(2048))  ##品牌
    brandImage = db.Column(db.String(2048))  ##品牌图片
    # introduceContent= db.Column(db.String(1024))
    culture = db.Column(db.String(2048))  ## 企业文化
    cultureImage = db.Column(db.String(512))  ##企业文化图片
    progress = db.Column(db.String(512))  ##企业历程
    progressImage = db.Column(db.String(512))  ##历程图片
    footer = db.Column(db.Text)  ##页面底部内容


##公司介绍
class Net_CompanyInfo(CommonModel, db.Model):
    #banner = db.Column(db.String(512))  ##大图
    introduce = db.Column(db.String(2048))  ##公司简介
    # introduceContent= db.Column(db.String(1024))
    culture = db.Column(db.String(2048))  ## 企业文化
    yongtuCompany = db.Column(db.String(512))  ##公司图片
    yongtuculture = db.Column(db.String(512))  ##文化图片


##公司荣誉
class Net_Honour(CommonModel, db.Model):
    time = db.Column(db.String(128))  ##时间
    content = db.Column(db.String(1024))  ##内容


## 产品信息
class Net_ProductInfo(CommonModel, db.Model):
    name = db.Column(db.String(128))  ##产品名称
    title = db.Column(db.String(1024))  ## 产品标题/简介
    picture = db.Column(db.String(512))  ##产品图片
    buy_url = db.Column(db.String(512))  ##购买链接


##类别
class Net_Category(CommonModel, db.Model):
    keyid = db.Column(db.Integer)  ##类别名称
    keyname = db.Column(db.String(128))  ##名称
    pid = db.Column(db.Integer, default=0)  ##父级id
    type = db.Column(db.Integer, default=0)  ##0,产品类别，1，新闻类别


##企业网站表 联系我们
class Net_Contact(CommonModel, db.Model):
    #banner = db.Column(db.String(512))  ##大图
    pic = db.Column(db.String(128))  ##大图
    zh_company = db.Column(db.String(521))  ## 中文名称
    en_company = db.Column(db.String(128))  ##英文公司名称
    email = db.Column(db.String(128))  ##邮箱
    phone = db.Column(db.String(128))  ##电话
    kf_phone = db.Column(db.String(128))  ##客服电话
    mobilephone = db.Column(db.String(128))  ##移动电脑
    x = db.Column(db.String(32))  ##坐标x
    y = db.Column(db.String(32))  ##坐标y
    logo = db.Column(db.String(256))  ##logo
    weixin = db.Column(db.String(256))  ##微信图片
    province = db.Column(db.String(32))  ##省
    city = db.Column(db.String(32))  ##市
    address = db.Column(db.String(256))  ##完整地址



##企业网站表 留言板
class Net_MessageBoard(CommonModel, db.Model):
    name = db.Column(db.String(128))  ##姓名
    mobile = db.Column(db.String(521))  ## 手机
    email = db.Column(db.String(128))  ##邮箱
    advice = db.Column(db.String(128))  ##建议


##企业网站表 加盟
class Net_Join(CommonModel, db.Model):
    name = db.Column(db.String(128))  ##姓名
    mobile = db.Column(db.String(521))  ## 手机
    email = db.Column(db.String(128))  ##邮箱
    condition = db.Column(db.String(128))  ##条件

##企业网站表 加盟_页面信息
class Net_Join_Page(CommonModel, db.Model):
    banner = db.Column(db.String(512))  ##大图
    market_left = db.Column(db.String(521))  ## 市场
    market_rigth = db.Column(db.String(521))  ## 市场
    qiye_left = db.Column(db.String(512))  ##企业
    qiye_right = db.Column(db.String(512))  ##企业
    zhaoshang_left = db.Column(db.String(512))  ##招商
    zhaoshang_center = db.Column(db.String(512))  ##招商
    zhaoshang_right = db.Column(db.String(512))  ##招商
    join_left = db.Column(db.String(512))  ##加盟
    join_right = db.Column(db.String(512))  ##加盟
    product_left = db.Column(db.String(512))  ##产品展示
    product_right = db.Column(db.String(512))  ##产品展示

# ##企业网站表 联系我们
# class Net_Contact(CommonModel, db.Model):
#     phone = db.Column(db.String(128))  ##电话
#     address = db.Column(db.String(521))  ## 地址
#     point = db.Column(db.String(128))  ##地图坐标
#     email = db.Column(db.String(128))  ##邮箱


##企业网站表，新闻类型
class Net_News_Category(CommonModel, db.Model):
    name = db.Column(db.String(128))  ##类别名称
    desc = db.Column(db.String(128))  ##类别描述

##企业网站表 行业动态
class Net_News(CommonModel, db.Model):
    title = db.Column(db.String(128))  ##新闻标题
    introduction = db.Column(db.String(1024))  ##导读
    date = db.Column(db.String(128))  ##新闻日期
    content = db.Column(db.String(1024))  ## 新闻内容
    author = db.Column(db.String(512))  ##新闻作者
    pic = db.Column(db.String(256))  ##图片
    category = db.Column(db.Integer)  ##新闻类别
    index = db.Column(db.Boolean)  ##是否推送首页

##产品表，父类
class Net_Product_Category_Parent(CommonModel, db.Model):
    name = db.Column(db.String(128))  ##类别名称
    desc = db.Column(db.String(128))  ##类别描述

##产品表，风格  目前没用到
# class Net_Product_Style(CommonModel, db.Model):
#     name = db.Column(db.String(128))  ##风格名称
#     desc = db.Column(db.String(128))  ##风格描述

##产品表，子类
class Net_Product_Category_Child(CommonModel, db.Model):
    name = db.Column(db.String(128))  ##类别名称
    desc = db.Column(db.String(128))  ##类别描述
    parentId = db.Column(db.Integer)  ##类别描述

##产品表
class NetProduct(CommonModel, db.Model):
    name = db.Column(db.String(128))  ##产品名称
    title=db.Column(db.String(128)) ##短标题
    categoryId = db.Column(db.Integer)  ##产品类别，对应childId
    style=db.Column(db.String(128)) ##风格
    pic=db.Column(db.String(128))##产品图片
    desc = db.Column(db.String(2048))  ##产品描述

##合作伙伴-核心业务
class Net_otherBussiness(CommonModel, db.Model):
    name = db.Column(db.String(128))  ##名称
    title=db.Column(db.String(512)) ##短标题
    categoryId = db.Column(db.Integer)  ##1为合作伙伴，2为核心业务
    url=db.Column(db.String(128)) ##跳转url
    pic=db.Column(db.String(128))##图片
    desc = db.Column(db.String(2048))  ##描述




db.create_all()
# print(int(time.time()*1000))


