from flask import url_for
from flask_admin._backwards import ObsoleteAttr
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla.ajax import QueryAjaxModelLoader
from flask_admin.form import upload
# from flask_admin.model import form
from flask_admin.model.template import EndpointLinkRowAction
from markupsafe import Markup
from flask_ckeditor import CKEditor, CKEditorField

from admin.opencode import MxImageUploadField
from model.modelBase import db
from model.models import PayRecord, User, Category, Car, Order, Address, Rate, Product, Images, User2product, TO_DO_List,TO_DO_Type
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, form, expose

from sqlalchemy.event import listens_for
import os.path as op
import  os
from jinja2 import Markup
# from flask_admin.
from setting import Aliyun

file_path = op.join(op.dirname(__file__), '../static/product')  # 文件上传路径
try:
    os.mkdir(file_path)
except OSError:
    pass
class Common_Admin(ModelView):
    page_size = 20
    #是否可以是设置分页数量
    #can_set_page_size=True
    column_exclude_list = ("update_time","remark","status")
    #can_export = True
    #can_delete = False
    #can_delete = False
    #删除tab不可见，当时可删除
    action_disallowed_list = ['delete']

    edit_template = 'edit.html'  # 指定编辑记录的模板

class User_Admin(Common_Admin):



    # # 格式化列表的图像显示
    # column_formatters = {
    #     'signature': _list_thumbnail
    # }
    # 扩展列表显示的头像为60*60像素
    form_extra_fields = {
        'signature': form.ImageUploadField('signature',
                                          base_path=file_path,
                                          relative_path='uploadFile/',
                                          thumbnail_size=(60, 60, True))

    }
    form_extra_fields = {
        'signature': MxImageUploadField(label=u'图片',base_path = 'static'),
    }
    #column_list = ('id', 'username','mobile','mobile','mobile','mobile','mobile','mobile','mobile')
    column_list = ['id', 'username','mobile','nickname','openid','age']
    column_labels = {
    'username': '用户名',
    'mobile' : '手机号',
    'nickname' : '昵称',
    'age' : '年龄'
    }
    def __init__(self, session, **kwargs):
        super(User_Admin, self).__init__(User, session, **kwargs)

class Order_Admin(Common_Admin):

    can_delete = False
    column_searchable_list = ['orderStatus','orderNo']
    column_filters = column_searchable_list
    column_list = ['orderNo', 'pruductPriceCount','discount','yunfei','orderRemark','mount','orderStatus','logisticsNo','userId','addressId']
    column_labels = {
    'orderNo': '订单号',
    'pruductPriceCount' : '订单总额',
    'discount' : '折扣',
    'orderRemark' : '订单备注',
    'mount' : '支付金额',
    'orderStatus' : '订单状态',
    'logisticsNo' : '快递单号',
    'userId' : '所属用户',
    'addressId' : '收货地址',
    'yunfei':'运费'

    }
    # form_ajax_refs = {
    #     'userId': QueryAjaxModelLoader('address', db.session, User, filters=["id>1"], page_size=10)
    # }

    form_columns =  ['orderNo', 'pruductPriceCount','discount','yunfei','orderRemark','mount','orderStatus','logisticsNo','userId','addressId']
    form_extra_fields = {
        'orderStatus':form.Select2Field('订单状态', choices =[(1,'待付款'),(5,'已付款待发货'),(2,'待收货'),(3,'待评价'),(4,'售后')],coerce=int )
        # 'addressId':form()
    }
    # form_widget_args = {
    #     'orderNo': {
    #          'disabled': True
    #     }
    # }
    can_view_details = True
    column_display_actions = ['eidt','delete','detail']
    edit_modal = True
    edit_modal_template = 'admin/model/modals/edit.html'
    create_modal = True
    def formMatter(view, context, model, name):

        if name == "orderStatus":

            if model.orderStatus == 1:
                return "待付款"
            if model.orderStatus == 5:
                return "待发货"
            if model.orderStatus == 2:
                return "待收货"
            if model.orderStatus == 3:
                return "待评价"
            if model.orderStatus == 4:
                return "售后"

            return '订单完成'
        if name == 'file_url':
            if model.file_url == None or model.file_url == "":
                return ""
            else:
                return Markup('<a target="_blank" href="' + model.file_url + '">点击查看附件</a> ')

    column_formatters = {
        'orderStatus': formMatter
    }
    # page_size = 20
    def __init__(self, session, **kwargs):
        super(Order_Admin, self).__init__(Order, session, **kwargs)
class Address_Admin(Common_Admin):
    column_list = ['id', 'receiver','mobile','address','area','default','userId']
    column_labels = {
    'receiver': '收件人',
    'mobile' : '手机号',
    'address' : '省市',
    'default' : '年龄',
    'area' : '住址',
    'userId':'所属用户'
    }
    column_searchable_list = ['receiver','address']
    column_filters = column_searchable_list
    def __init__(self, session, **kwargs):
        super(Address_Admin, self).__init__(Address, session, **kwargs)
class Category_Admin(Common_Admin):
    # page_size = 5
    list_template = 'category_list.html'
    def __init__(self, session, **kwargs):
        super(Category_Admin, self).__init__(Category, session, **kwargs)


class Product_Admin(Common_Admin):
    column_searchable_list = ['title','category']
    column_filters = column_searchable_list
    column_list = ['title', 'main_image','detail_image','category','price','brownCount','size','color','price','store']
    form_columns = ['title', 'main_image','image800', 'image400','image200','image100', 'detail_image', 'category', 'price', 'brownCount', 'size', 'color', 'price',
                    'store']
    column_details_list= ['title', 'main_image','detail_image','category','price','brownCount','size','color','price','store']
    column_labels = {
    'title': '标题',
    'main_image' : '主图',
    'image800': '主图:第2张',
    'image400': '主图:第3张',
    'image200': '主图:第4张',
    'image100': '主图:第5张',

    'category' : '类别',
    'brownCount' : '浏览量',
    'size' : '尺码',
    'color' : '颜色',
    'price' : '价格',
    'detail_image': '详情',
    'store':'库存'
    }

    def _list_thumbnail(view, context, model, name):
        if name=='category':
            categoryName=Category().query.filter(Category.cid == model.category).first()
            if categoryName ==None:
                return ""
            return categoryName.name
        #if model.category:
        #    categoryName=Category().query.filter(Category.cid == model.category).first()
        #    if categoryName ==None:
        #        return ""

        #    return categoryName.name
        if not model.main_image:
            return ''
        return Markup('<img src="https://pyshop.oss-cn-beijing.aliyuncs.com/product/'+model.main_image+'?x-oss-process=image/resize,h_100'+'">')
        # return Markup('<img src="%s">' % url_for('static',
        #                                          filename='product/'+form.thumbgen_filename(model.main_image)))


    column_formatters = {
        'main_image': _list_thumbnail,
        'category': _list_thumbnail
    }
    # a=
    categorys=[(category.cid, category.name) for category in (Category().query.filter(Category.pid != 0).all())]
    # c=Category().query(Category.cid,Category.name).filter(Category.pid!=0).all()

    # Alternative way to contribute field is to override it completely.
    # In this case, Flask-Admin won't attempt to merge various parameters for the field.
    form_extra_fields = {
        'main_image': MxImageUploadField('主图',base_path=file_path, url_relative_path=Aliyun.ReadUrl+'product/'),
        'image800': MxImageUploadField('第2张主图',
                                       base_path=file_path, url_relative_path=Aliyun.ReadUrl+'product/'),
        'image400': MxImageUploadField('第3张主图',
                                       base_path=file_path, url_relative_path=Aliyun.ReadUrl+'product/'),

        'image200': MxImageUploadField('第4张主图',
                                       base_path=file_path, url_relative_path=Aliyun.ReadUrl+'product/'),
        'image100': MxImageUploadField('第5张主图',
                                       base_path=file_path, url_relative_path=Aliyun.ReadUrl+'product/'),
        'category':form.Select2Field('产品类别', choices =categorys,coerce=int )
    }

    # def date_validator(form, field):
    #     print("aa")
    #
    #
    # form_args = dict(
    #     category=dict(validators=[date_validator])
    # )

    # ajax_update= ['ti tle', 'main_image']
    ##list页面是否显示可编辑
    column_editable_list= ['title']
    # is_editable=
    # column_extra_row_actions=['user']
    form_overrides = dict(detail_image=CKEditorField)  # 重写表单字段，将 text 字段设为 CKEditorField
    create_template = 'create.html'  # 指定创建记录的模板
    edit_template = 'edit.html'  # 指定编辑记录的模板
    list_template = 'product-list.html'
    def __init__(self, session, **kwargs):
        super(Product_Admin, self).__init__(Product, session, **kwargs)

    # @expose('/')
    # def default(self):
    #     return self.render('product-list.html')
class Images_Admin(Common_Admin):
    column_list = ['id', 'name','url','yongtu','pic']
    column_labels = {
    'name': '图片名称',
    'url' : '跳转链接',
    'yongtu' : '图片用途',
    'pic' : '图片地址'
    }
    def __init__(self, session, **kwargs):
        super(Images_Admin, self).__init__(Images, session, **kwargs)
class User2product_Admin(Common_Admin):

    #def get_query(self):
    #    return self.session.query(
    #        User2product.id.label("id"),
    #        Farmer.name.label("name"),
    #        Farmer.village.label("village"),
    #        Farmer.phone.label("phone"),
    #        Farmer.area.label("area"),
    #        func.sum(Transaction.total).label("amount")
    #        ).join(Transaction).group_by(Farmer.id)
    def __init__(self, session, **kwargs):
        super(User2product_Admin, self).__init__(User2product, session, **kwargs)

class PayRecord_Admin(Common_Admin):

    column_searchable_list = ['transactionId','create_time']
    column_filters = column_searchable_list
    column_list = ['tradeNo', 'totalFee','transactionId','attach','returnstring','create_time']
    column_labels = {
    'tradeNo': '支付单号',
    'totalFee' : '支付金额',
    'transactionId' : '订单号',
    'attach' : '支付备注',
    'returnstring' : '回调备注',
    'create_time' : '支付时间',
    }
    # column_details_list=['transactionId']
    # form_columns = ['tradeNo', 'totalFee','transactionId']
    def __init__(self, session, **kwargs):
        super(PayRecord_Admin, self).__init__(PayRecord, session, **kwargs)
class TO_DO_List_Admin(Common_Admin):

    can_delete = False
    column_searchable_list = ['title','tasktype','is_finish']
    column_filters = column_searchable_list

    column_list = ['title','tasktype', 'done_date','content','file_url','is_finish']
    column_labels = {
    'title': '任务标题',
    'tasktype':'任务类型',
    'done_date' : '预计完成时间',
    'content' : '任务内容',
    'file_url' : '附件',
    'is_finish' : '是否完成'
    }
    form_columns = ['title','tasktype', 'done_date','content','file_url','is_finish']

    todo_types=[(todo_type.id, todo_type.type_name) for todo_type in (TO_DO_Type().query.filter(TO_DO_Type.is_use == True).all())]
    form_extra_fields = {
        'tasktype':form.Select2Field('任务类别', choices =todo_types,coerce=int )
    }

    def _list_thumbnail(view, context, model, name):
        if name=="tasktype":
            categoryName=TO_DO_Type().query.filter(TO_DO_Type.id == model.tasktype).first()
            if categoryName ==None:
                return ""

            return categoryName.type_name
        if name=="is_finish":

            if model.is_finish ==True:
                return "已完成"

            return '未完成'
        if name=='file_url':
            if model.file_url==None or model.file_url=="":
                return ""
            else:
                return Markup('<a target="_blank" href="'+model.file_url+'">点击查看附件</a> ')


    form_widget_args = {'tasktype':{'class': 'form-control','style': "width: 100px",'placeholder':'ex. M132 or T456'}

    #form_widget_args = {
    #'tasktype': {
    #    'readonly': True
    #}
}
    column_formatters = {
        'tasktype': _list_thumbnail,
        'is_finish':_list_thumbnail,
        'file_url':_list_thumbnail
    }

    ##筛选字段下拉值
    column_choices = {
                    'tasktype': todo_types,
                    'is_finish': [('0','未完成'),('','已完成')]
                }
    column_default_sort = ('update_time', True)
    print("aa")
    # def scaffold_sortable_columns(self):
    #     return {'is_finish':'is_finish'}

     #   if isinstance(attr, TO_DO_Type):

     #       return [MyEqualFilter(name, name)]
    # column_details_list=['transactionId']
    # form_columns = ['tradeNo', 'totalFee','transactionId']
    def __init__(self, session, **kwargs):
        super(TO_DO_List_Admin, self).__init__(TO_DO_List, session, **kwargs)
class TO_DO_Type_Admin(Common_Admin):
    can_delete = False

    column_list = ['type_name','type_des','is_use']
    column_labels = {
    'type_name': '任务类型',
    'type_des':'类型描述',
    'is_use':'启用'
    }
    form_columns = ['type_name','type_des','is_use']

    def __init__(self, session, **kwargs):
        super(TO_DO_Type_Admin,self).__init__(TO_DO_Type, session, **kwargs)

