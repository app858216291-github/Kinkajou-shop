from flask_admin.contrib.sqla.fields import QuerySelectField
from flask_ckeditor import CKEditor, CKEditorField
from admin.opencode import MxImageUploadField
from model.models import *
from model.netModels import *
import os.path as op
import  os
from jinja2 import Markup
from model.adminModels import Common_Admin as BaseAdmin
from model.netModels import Net_Index_Images
from setting import Aliyun
import flask_login as login

file_path = op.join(op.dirname(__file__), '../static/product')  # 文件上传路径
try:
    os.mkdir(file_path)
except OSError:
    pass

##下拉选择
def getDictForChoice(name):
    return [(dictConfig.key, dictConfig.value) for dictConfig in (DictConfig().query.filter(DictConfig.name == name).all())]


class Common_Admin(BaseAdmin):

    def is_accessible(self):
        if login.current_user.is_authenticated:
            if login.current_user.username=='home':
                return True
            return False
        return False




#首页轮播图
class Index_Images_Admin(Common_Admin):

    columnsa=[
        ['name', '图片名称','text'],
        ['url', '跳转链接', 'text'],
        ['yongtu', '图片用途', 'text'],
        ['pic', '图片地址1920*600', 'image']
    ]


    def __init__(self, session, **kwargs):
        self.net_init(self.columnsa)
        super(Index_Images_Admin, self).__init__(Net_Index_Images, session, **kwargs)

#首页图文内容
class Net_Index_Admin(Common_Admin):
    columns = [
        ['brand', '品牌描述', 'CKEditorField'],
        ['brandImage' , '品牌图片', 'image'],
        ['culture' ,'文化710*660',  'CKEditorField'],
        ['progress' , '历程','CKEditorField'],
        ['footer', '页面底部内容', 'text']
    ]
    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(Net_Index_Admin, self).__init__(Net_Index, session, **kwargs)


class CompanyInfo_Admin(Common_Admin):

    columns = [
    ['banner','顶部大图1920*600','image'],
    ['introduce','公司简介','CKEditorField'],
    ['culture' ,'企业文化','CKEditorField'],
    ['yongtuCompany' ,'公司图片710*660','image'],
    ['yongtuculture' ,'文化图片960*700','image']
    ]

    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(CompanyInfo_Admin, self).__init__(Net_CompanyInfo, session, **kwargs)

class Honour_Admin(Common_Admin):
    column_list = ['id', 'time','content']
    column_labels = {
    'time': '时间',
    'content' : '荣誉内容'
    }

    def __init__(self, session, **kwargs):
        super(Honour_Admin, self).__init__(Net_Honour, session, **kwargs)

class Contact_Admin(Common_Admin):
    create_modal = True

    columns = [
        ['banner','顶部大图','image'],
        ['zh_company', '公司中文名','text'],
        ['en_company', '公司英文名','text'],
        ['email','公司邮箱','text'],
        ['phone','公司固定电话','text'],
        ['kf_phone','客服电话','text'],
        ['mobilephone', '移动号码','text'],
        ['logo','企业Logo（500*154）', 'image'],
        ['weixin','微信二维码（124*124）' , 'image'],
        ['province','省','text'],
        ['city', '市','text'],
        ['address', '完整地址','text']
    ]

    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(Contact_Admin, self).__init__(Net_Contact, session, **kwargs)
class MessageBoard_Admin(Common_Admin):
    column_list = ['id', 'name', 'mobile', 'email', 'advice']
    column_labels = {
        'name': '姓名',
        'mobile': '手机号',
        'email': '邮箱',
        'advice': '建议'
    }

    def __init__(self, session, **kwargs):
        super(MessageBoard_Admin, self).__init__(Net_MessageBoard, session, **kwargs)

class News_Category_Admin(Common_Admin):
    columns = [
        [ 'name', '类别名称', 'text'],
        [ 'desc' , '类别描述', 'text']
    ]
    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(News_Category_Admin, self).__init__(Net_News_Category, session, **kwargs)
class News_Admin(Common_Admin):
    columns = [
        [ 'title', '新闻标题', 'text'],
        [ 'date' , '日期', 'text'],
        [ 'content' , '新闻内容', 'CKEditorField'],
        ['author' , '新闻作者', 'text'],
        [ 'pic','新闻图片' ,'image'],
        ['introduction', '导读', 'CKEditorField'],

        [ 'category' , '新闻类别','QuerySelectField',[(todo_type.id, todo_type.name) for todo_type in (Net_News_Category().query.all())]],
        ['index', '是否推送首页（首页只能推送3条）', 'text']
    ]
    def _list_thumbnail2(view, context, model, name):
        if name == 'category':
            if model.category==None:
                return ""
            for category in (Net_News_Category().all()):
                if model.category==category.id:
                    return category.name

    column_formatters = {
        'category': _list_thumbnail2
    }
    def query_factory():
        return [(category.id) for category in (Net_News_Category().all())]
    def get_label(obj):
        return Net_News_Category().get(obj).name
    def get_pk(obj):
        return obj
    form_extra_fields = {
        # 'tasktype':form.Select2Field('任务类别', choices =todo_types,coerce=int )
        'category': QuerySelectField(label=u'新闻类别', query_factory=query_factory,get_label=get_label,get_pk=get_pk)
    }

    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(News_Admin, self).__init__(Net_News, session, **kwargs)



class Net_MessageBoard_Admin(Common_Admin):
    column_list = [ 'name','mobile','email','advice']
    column_labels = {
    'name': '姓名',
    'mobile' : '联系电话',
    'email' : '邮箱',
    'advice' : '建议'
    }
    form_columns = column_list
    def __init__(self, session, **kwargs):
        super(Net_MessageBoard_Admin, self).__init__(Net_MessageBoard, session, **kwargs)
class Net_Join_Admin(Common_Admin):
    column_list = [ 'name','mobile','email','condition']
    column_labels = {
        'name': '姓名',
        'mobile': '联系电话',
        'email': '邮箱',
        'condition': '条件'
    }
    form_columns = column_list

    def __init__(self, session, **kwargs):
        super(Net_Join_Admin, self).__init__(Net_Join, session, **kwargs)
class Net_Join_Page_Admin(Common_Admin):
    columns = [
        ['banner', '头部大图1920*550', 'image'],
        ['market_left', '市场分析-左313*239', 'CKEditorField'],
        ['market_rigth', '市场分析-右313*425', 'CKEditorField'],
        ['qiye_left', '企业和荣誉-左313*294', 'CKEditorField'],
        ['qiye_right', '企业和荣誉-右313*431', 'CKEditorField'],
        ['zhaoshang_left', '招商-左(313*224)*2', 'CKEditorField'],
        ['zhaoshang_center', '招商-中', 'CKEditorField'],
        ['zhaoshang_right', '招商-右382*604', 'CKEditorField'],
        ['join_left', '加盟-左313*295', 'CKEditorField'],
        ['join_right', '加盟-右', 'CKEditorField'],
        ['product_left', '产品-左313*359', 'CKEditorField'],
        ['product_right', '产品-右313*359', 'CKEditorField']
    ]


    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(Net_Join_Page_Admin, self).__init__(Net_Join_Page, session, **kwargs)

class Net_Product_Category_Parent_Admin(Common_Admin):
    columns = [
        [ 'name', '类别名称', 'text'],
        [ 'desc' , '类别描述', 'text']
    ]
    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(Net_Product_Category_Parent_Admin, self).__init__(Net_Product_Category_Parent, session, **kwargs)
class Net_Product_Category_Child_Admin(Common_Admin):
    columns = [
        [ 'name', '类别名称', 'text'],
        [ 'desc' , '类别描述', 'text'],
        ['parentId', '父级类别', 'text']
    ]
    def _list_thumbnail2(view, context, model, name):
        if name == 'parentId':
            if model.parentId==None:
                return ""
            for category in (Net_Product_Category_Parent().all()):
                if model.parentId==category.id:
                    return category.name

    column_formatters = {
        'parentId': _list_thumbnail2
    }
    def query_factory():
        return [(category.id) for category in (Net_Product_Category_Parent().all())]
    def get_label(obj):
        return Net_Product_Category_Parent().get(obj).name
    def get_pk(obj):
        return obj
    form_extra_fields = {
        # 'tasktype':form.Select2Field('任务类别', choices =todo_types,coerce=int )
        'parentId': QuerySelectField(label=u'新闻类别', query_factory=query_factory,get_label=get_label,get_pk=get_pk)
    }


    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(Net_Product_Category_Child_Admin, self).__init__(Net_Product_Category_Child, session, **kwargs)


class Net_Product_Admin(Common_Admin):
    columns = [
        [ 'name', '产品名称', 'text'],
        [ 'title' , '产品短标题', 'text'],
        ['categoryId', '类别', 'text'],
        ['pic', '产品图片313*338', 'image'],
        ['style', '风格', 'text'],

        ['desc', '产品描述', 'CKEditorField']
    ]



    def _list_thumbnail2(view, context, model, name):
        if name == 'categoryId':
            if model.categoryId==None:
                return ""
            for category in (Net_Product_Category_Child().all()):
                if model.categoryId==category.id:
                    return category.name

    column_formatters = {
        'categoryId': _list_thumbnail2
    }
    def query_factory():
        return [(category.id) for category in (Net_Product_Category_Child().all())]
    def get_label(obj):
        return Net_Product_Category_Child().get(obj).name
    def get_pk(obj):
        return obj
    form_extra_fields = {
        # 'tasktype':form.Select2Field('任务类别', choices =todo_types,coerce=int )
        'categoryId': QuerySelectField(label=u'产品类别', query_factory=query_factory,get_label=get_label,get_pk=get_pk)
    }
    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(Net_Product_Admin, self).__init__(NetProduct, session, **kwargs)



class Net_OtherBussiness_Admin(Common_Admin):
    columns = [
        [ 'name', '名称', 'text'],
        [ 'title' , '导读', 'text'],
        ['categoryId', '类别', 'Select2Field',[(1, '合作伙伴'), (2, '核心业务')]],
        ['pic', '图片', 'image'],
        ['url', '跳转链接', 'text'],
        ['desc', '描述', 'CKEditorField']
    ]

    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(Net_OtherBussiness_Admin, self).__init__(Net_otherBussiness, session, **kwargs)
