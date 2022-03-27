##企业宣传网站的后台
from flask import url_for
from flask_admin._backwards import ObsoleteAttr
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla.ajax import QueryAjaxModelLoader
from flask_admin.contrib.sqla.fields import QuerySelectField
from flask_admin.form import upload, FormOpts
# from flask_admin.model import form
from flask_admin.model.template import EndpointLinkRowAction
from markupsafe import Markup
from flask_ckeditor import CKEditor, CKEditorField
from wtforms import validators

from admin.opencode import MxImageUploadField
from common import tools
from model.modelBase import db
from model.models import *
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, form, expose
from flask_admin import form as formTem

from sqlalchemy.event import listens_for
import os.path as op
import  os
from jinja2 import Markup
# from flask_admin.
from setting import Aliyun
from model.modelBase import Common_Admin
import flask_login as login

file_path = op.join(op.dirname(__file__), '../static/product')  # 文件上传路径
try:
    os.mkdir(file_path)
except OSError:
    pass

##下拉选择
def getDictForChoice(name):
    return [(dictConfig.key, dictConfig.value) for dictConfig in (DictConfig().query.filter(DictConfig.name == name).all())]


class User_Admin(Common_Admin):
    # can_view_details = True
    # # 格式化列表的图像显示
    # column_formatters = {
    #     'signature': _list_thumbnail
    # }
    # 扩展列表显示的头像为60*60像素
    form_extra_fields = {
        'portrait': form.ImageUploadField('portrait',
                                          base_path=file_path,
                                          relative_path='uploadFile/',
                                          thumbnail_size=(60, 60, True))
    }
    form_extra_fields = {
        'portrait': MxImageUploadField(label=u'头像',base_path=file_path, url_relative_path=Aliyun.ReadUrl+'product/'),
    }
    column_list = [ 'username','mobile','nickname','openid','openid_mp','age']
    form_columns=['id', 'username','mobile','name','nickname','openid','openid_mp','age','credit','portrait','create_time','signature']
    column_labels = {
    'username': '用户名',
    'mobile' : '手机号',
    'name': '姓名',
    'nickname' : '昵称',
    'age' : '年龄',
    'password': '密码',
    'phone': '固定电话号码',
    'address': '地址',
    'portrait': '头像',
    'create_time': '创建时间',
    'credit':'积分',
    'signature':'个性签名'
    }
    column_exclude_list = ("update_time", "remark", "status")
    column_display_actions = ['eidt', 'delete', 'detail']
    column_searchable_list = ['username', 'mobile','name','nickname','address','signature']
    column_filters = column_searchable_list
    def __init__(self, session, **kwargs):
        super(User_Admin, self).__init__(User, session, **kwargs)
from flask import g, request, url_for, flash
from flask import (current_app, request, redirect, flash, abort, json,
                   Response, get_flashed_messages, stream_with_context)
from flask_admin.babel import gettext, ngettext
from flask_admin.model.helpers import prettify_name, get_mdict_item_or_list
def get_redirect_target(param_name='url'):
    target = request.values.get(param_name)
class Order_Admin(Common_Admin):
    @expose('/ajax/update/', methods=('POST',))
    def ajax_update(self):
        """
            Edits a single column of a record in list view.
        """


        if not self.column_editable_list:
            abort(404)

        form = self.list_form()

        # prevent validation issues due to submitting a single field
        # delete all fields except the submitted fields and csrf token
        for field in list(form):
            if (field.name in request.form) or (field.name == 'csrf_token'):
                pass
            else:
                form.__delitem__(field.name)

        if self.validate_form(form):
            pk = form.list_form_pk.data
            record = self.get_one(pk)
            a = request.form.get("receiver")
            b=request.form.get("address")
            c = request.form.get("area")
            d = request.form.get("mobile")

            if a != None or b!=None or c!=None or d!=None:
                record=self.session.query(Address).get(record.addressId)
            

            if record is None:
                return gettext('Record does not exist.'), 500

            if self.update_model(form, record):
                # Success
                return gettext('Record was successfully saved.')
            else:
                # Error: No records changed, or problem saving to database.
                msgs = ", ".join([msg for msg in get_flashed_messages()])
                return gettext('Failed to update record. %(error)s',
                               error=msgs), 500
        else:
            for field in form:
                for error in field.errors:
                    # return validation error to x-editable
                    if isinstance(error, list):
                        return gettext('Failed to update record. %(error)s',
                                       error=", ".join(error)), 500
                    else:
                        return gettext('Failed to update record. %(error)s',
                                       error=error), 500
    @expose('/edit/', methods=('GET', 'POST'))
    def edit_view(self):
        """
            Edit model view
        """
        return_url = get_redirect_target() or self.get_url('.index_view')

        if not self.can_edit:
            return redirect(return_url)

        id = get_mdict_item_or_list(request.args, 'id')
        if id is None:
            return redirect(return_url)

        model=self.session.query(Order).get(id)
        # model=self.session.query(User).get(model.userId)
        if model is None:
            flash(gettext('Record does not exist.'), 'error')
            return redirect(return_url)

        form = self.edit_form(obj=model)
        if not hasattr(form, '_validated_ruleset') or not form._validated_ruleset:
            self._validate_form_instance(ruleset=self._form_edit_rules, form=form)

        if self.validate_form(form):
            if self.update_model(form, model):
                flash(gettext('Record was successfully saved.'), 'success')
                if '_add_another' in request.form:
                    return redirect(self.get_url('.create_view', url=return_url))
                elif '_continue_editing' in request.form:
                    return redirect(request.url)
                else:
                    # save button
                    return redirect(self.get_save_return_url(model, is_created=False))

        if request.method == 'GET' or form.errors:
            self.on_form_prefill(form, id)

        form_opts = FormOpts(widget_args=self.form_widget_args,
                             form_rules=self._form_edit_rules)

        if self.edit_modal and request.args.get('modal'):
            template = self.edit_modal_template
        else:
            template = self.edit_template

        return self.render(template,
                           model=model,
                           form=form,
                           form_opts=form_opts,
                           return_url=return_url)
    @expose('/user/')
    def user_view(self):
        """
            Details model view
        """
        return_url = get_redirect_target() or self.get_url('.index_view')

        if not self.can_view_details:
            return redirect(return_url)

        id = get_mdict_item_or_list(request.args, 'id')
        if id is None:
            return redirect(return_url)
        model=self.session.query(User).get(id)
        model.image="https://pyshop.oss-cn-beijing.aliyuncs.com/product/202104251304259182.jpg?x-oss-process=image/resize,h_101"
        # model = self.get_one(id)

        if model is None:
            flash(gettext('Record does not exist.'), 'error')
            return redirect(return_url)

        if self.details_modal and request.args.get('modal'):
            # template = self.details_modal_template
            template = 'admin/models/details.html'
        else:
            # template = self.details_modal_template
            template = 'admin/models/details.html'

        de=[('id', 'ID'), ('username', '用户名'),('mobile', '手机号') ,('nickname', '昵称') ,('age', '年龄')  ,('image', '图片')  ]
        return self.render(template,
                           model=model,
                           details_columns=de,
                           get_value=self.get_detail_value,
                           return_url=return_url)

    @expose('/address/')
    def address_view(self):
        """
            Details model view
        """
        return_url = get_redirect_target() or self.get_url('.index_view')

        if not self.can_view_details:
            return redirect(return_url)

        id = get_mdict_item_or_list(request.args, 'id')
        if id is None:
            return redirect(return_url)
        model = self.session.query(Address).get(id)
        # model = self.get_one(id)

        if model is None:
            flash(gettext('Record does not exist.'), 'error')
            return redirect(return_url)

        if self.details_modal and request.args.get('modal'):
            template = self.details_modal_template
        else:
            template = self.details_modal_template

        de = [('id', 'ID'), ('receiver', '收货人'), ('mobile', '收货人电话'), ('address', '收货地址'), ('area', '街道门牌')]
        return self.render(template,
                           model=model,
                           details_columns=de,
                           get_value=self.get_detail_value,
                           return_url=return_url)



    can_delete = False
    column_searchable_list = ['orderStatus','orderNo','receiver','mobile','logisticsNo','orderRemark','address','area']
    column_filters = column_searchable_list
    column_list = ['orderNo', 'pruductPriceCount','orderRemark','mount','orderStatus','logisticsType','logisticsNo','userId','receiver','mobile','address','area']
    column_labels = {
    'orderNo': '订单号',
    'pruductPriceCount' : '订单总额',
    'discount' : '折扣',
    'orderRemark' : '订单备注',
    'mount' : '支付金额',
    'orderStatus' : '订单状态',
     'logisticsType':'快递公司',
    'logisticsNo' : '快递单号',
    'userId' : '所属用户',
    'yunfei':'运费',
    'receiver':'收件人',
    'mobile':'收件人手机号',
    'address':'地址（省市县）',
    'area':'街道'
    }

    # form_ajax_refs = {
    #     'userId': QueryAjaxModelLoader('address', db.session, User, filters=["id>1"], page_size=10)
    # }

    form_columns =  column_list
    form_extra_fields = {
        'orderStatus':form.Select2Field('订单状态', choices =[(1,'待付款'),(5,'已付款待发货'),(2,'待收货'),(3,'待评价'),(4,'售后')],coerce=int ),
        'logisticsType':form.Select2Field('快递公司', choices =[(1,'中通'),(2,'韵达'),(3,'申通'),(4,'圆通'),(5,'顺丰')],coerce=int ),

    }
    column_editable_list = ['receiver','mobile','logisticsNo','orderRemark','address','area']
    # form_widget_args = {
    #     'orderNo': {
    #          'disabled': True
    #     }
    # }
    can_view_details = True
    # column_display_actions = ['eidt','delete','detail']
    edit_modal = True
    edit_modal_template = 'admin/model/modals/edit.html'
    list_template = 'order-list.html'
    create_modal = True
    def formMatter(view, context, model, name):
        if name == "logisticsNo":
            if model.logisticsNo == "" or model.logisticsNo==None :
                return "无快递单号"
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
        # if name=='userId':
        #     return '兰花爱好者'
        # if name=='addressId':
        #     return Markup('这里是收<br>货人信息')
        if name == 'logisticsType':
            if model.logisticsType==1:
                return '中通'
            if model.logisticsType==2:
                return '韵达'
            if model.logisticsType==3:
                return '申通'
            if model.logisticsType==4:
                return '圆通'
            if model.logisticsType==5:
                return '顺丰'
            if model.logisticsType==99:
                return '其他'

    column_formatters = {
        'orderStatus': formMatter,
        'logisticsNo':formMatter,
        # 'addressId':formMatter,
        'logisticsType':formMatter
    }

     ##筛选字段下拉值
    column_choices = {
                    'orderStatus': [(1,'待付款'),(2,'待收货'),(3,'待评价')]

                }
    # page_size = 20


    def __init__(self, session, **kwargs):
        super(Order_Admin, self).__init__(Order_v, session, **kwargs)
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
    edit_modal = False
    create_modal = False
    column_searchable_list = ['title','category']
    column_filters = column_searchable_list
    column_list = ['title', 'main_image','category','price','size','color','price','store']
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
            return tools.shopUtil.getFileFromKey(model.main_image)
        return Markup('<img src="'+tools.shopUtil.getFileFromKey(model.main_image)+'?x-oss-process=image/resize,h_101'+'">')
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
        'main_image': MxImageUploadField('主图',base_path=file_path, url_relative_path=""),
        # 'main_image': MxImageUploadField('主图', base_path=file_path, url_relative_path=""),
        'image800': MxImageUploadField('第2张主图',
                                       base_path=file_path, url_relative_path=""),
        'image400': MxImageUploadField('第3张主图',
                                       base_path=file_path, url_relative_path=""),

        'image200': MxImageUploadField('第4张主图',
                                       base_path=file_path, url_relative_path=""),
        'image100': MxImageUploadField('第5张主图',
                                       base_path=file_path, url_relative_path=""),
        'category':form.Select2Field('产品类别', choices =categorys,coerce=int )
    }

    ##筛选字段下拉值
    column_choices = {
                    'category': categorys

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

    def _list_thumbnail(view, context, model, name):
        if name=='pic':
            return Markup('<img style="width: 100px" src="'+model.pic+'">')



    column_formatters = {
        'pic': _list_thumbnail,

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
    column_list = ['tradeNo', 'totalFee','transactionId','attach','create_time']
    column_labels = {
    'tradeNo': '订单号',
    'totalFee' : '支付金额',
    'transactionId' : '支付单号',
    'attach' : '支付备注',
    'create_time' : '支付时间',
    }
    column_searchable_list = ['tradeNo', 'attach']
    column_filters = column_searchable_list
    # column_details_list=['transactionId']
    # form_columns = ['tradeNo', 'totalFee','transactionId']
    def __init__(self, session, **kwargs):
        super(PayRecord_Admin, self).__init__(PayRecord, session, **kwargs)
class TO_DO_List_Admin(Common_Admin):

    can_delete = False
    can_export = True

    def is_accessible(self):
        return True
    column_searchable_list = ['title','tasktype','is_finish']
    column_filters = column_searchable_list

    column_list = ['title','tasktype', 'done_date','content','dealMethod','file_url','is_finish']
    column_labels = {
    'title': '任务标题',
    'tasktype':'任务类型',
    'done_date' : '预计完成时间',
    'content' : '任务内容',
    'dealMethod': '处理结果',
    'file_url' : '附件',
    'is_finish' : '是否完成'
    }
    form_columns = ['title','tasktype', 'done_date','content','dealMethod','file_url','is_finish']

    todo_types=[(todo_type.id, todo_type.type_name) for todo_type in (TO_DO_Type().query.filter(TO_DO_Type.is_use == True).all())]

    def query_factory():
        return [(todo_type.id) for todo_type in (TO_DO_Type().query.filter(TO_DO_Type.is_use == True).all())]

    def get_label(obj):
        return  TO_DO_Type().get(obj).type_name
    def get_pk(obj):
        # TO_DO_Type().get(obj).type_name
        # return obj[0]
        return obj
    form_extra_fields = {
        # 'tasktype':form.Select2Field('任务类别', choices =todo_types,coerce=int )
        'tasktype':QuerySelectField(label='任务类别', validators=[validators.required()], query_factory=query_factory, get_pk=get_pk,get_label=get_label)
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

    # def scaffold_sortable_columns(self):
    #     return {'is_finish':'is_finish'}

     #   if isinstance(attr, TO_DO_Type):

     #       return [MyEqualFilter(name, name)]
    # column_details_list=['transactionId']
    # form_columns = ['tradeNo', 'totalFee','transactionId']

    def __init__(self, session, **kwargs):

        super(TO_DO_List_Admin, self).__init__(TO_DO_List, session, **kwargs)
        self.column_choices["tasktype"]= [(todo_type.id, todo_type.type_name) for todo_type in (TO_DO_Type().query.filter(TO_DO_Type.is_use == True).all())]
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

class DictConfig_Admin(Common_Admin):
    can_delete = False
    def __init__(self, session, **kwargs):
        super(DictConfig_Admin,self).__init__(DictConfig, session, **kwargs)

class PYSHOP_CONSTANT_Admin(Common_Admin):
    can_delete = False
    columns = [
        ['key', '系统变量名', 'text'],
        ['value', '系统变量值', 'text'],
        ['des', '用途描述', 'text']
    ]
    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(PYSHOP_CONSTANT_Admin,self).__init__(PYSHOP_CONSTANT, session, **kwargs)

class WorkFlow_Admin(Common_Admin):
    column_exclude_list = ("update_time", "status")
    columns = [
        ['system', '流程所属系统', 'text'],
        [ 'workflowId', '流程ID', 'text'],
        [ 'flowName' , '流程名称', 'text'],
        ['remark', '备注', 'text'],
        ['canSync', '是否可同步', 'text']
    ]
    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(WorkFlow_Admin, self).__init__(PZHOA_WorkFlow, session, **kwargs)


