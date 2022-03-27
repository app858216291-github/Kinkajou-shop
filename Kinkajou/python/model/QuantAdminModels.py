from flask_admin.contrib.sqla.fields import QuerySelectField
from flask_ckeditor import CKEditor, CKEditorField
from admin.opencode import MxImageUploadField
from model.models import *
from model.netModels import *
import os.path as op
import  os
from jinja2 import Markup
from model.adminModels import Common_Admin as BaseAdmin
from model.quantModels import *
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
            if login.current_user.username=='quant':
                return True
            return False
        return False

#推荐
class Quant_Recommend_Admin(Common_Admin):
    # return super(MyView, self).get_query().filter(User.username == current_user.username)
    columns = [
        ['code', '股票编码', 'text'],
        ['codeName' , '股票名称', 'text'],
        ['date' ,'日期',  'text'],
        ['roa' , '市净率','text'],
        ['PER', '市盈率', 'text'],
        ['size', '购买股数', 'text'],
        ['price', '当前价格', 'text'],
        ['nextday', '第二天价格', 'text'],
        ['nextday2', '第三天价格', 'text'],
        ['nextday3', '第四天价格', 'text'],
        ['price_now', '当前价格', 'text'],
        ['is_buy', '是否持仓', 'text'],
        ['kd', 'KD值', 'text'],
        ['macd', 'macd值', 'text'],
    ]
    column_searchable_list = ['code', 'codeName', 'date', 'roa', 'PER', 'price']
    column_filters = column_searchable_list
    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(Quant_Recommend_Admin, self).__init__(Quant_RecommendStock, session, **kwargs)
##实盘买卖
class Quant_Order_Admin(Common_Admin):
    # return super(MyView, self).get_query().filter(User.username == current_user.username)
    columns = [
        ['code', '股票编码', 'text'],
        ['codeName', '股票名称', 'text'],
        ['position' , '持仓', 'text'],
        ['buyNow' ,'急买',  'text'],
        ['sellNow' , '急卖','text'],
        ['buyAfter', '委托买', 'text'],
        ['sellAfter', '委托卖', 'text'],
        ['monut', '数量', 'text'],
        ['status', '状态', 'Select2Field',[(0, '初始状态'),(1, '待交易'), (2, '已处理'), (3, '作废')]],
    ]
    column_searchable_list = ['code', 'codeName', 'position', 'status']
    column_filters = column_searchable_list
    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(Quant_Order_Admin, self).__init__(Quant_Order, session, **kwargs)

##股票池
class Quants_Admin(Common_Admin):
    can_export = True
    # return super(MyView, self).get_query().filter(User.username == current_user.username)
    columns = [
        ['code', '股票编码', 'text'],
        ['codeName', '股票名称', 'text'],
        ['roe', '净资产收益率', 'text'],
        ['pe', '市盈率', 'text'],
        ['shizhi', '市值', 'text'],
        ['attrFloat1', '价格', 'text'],
        ['des', '描述', 'text'],
        ['refresTime', '数据更新时间', 'text'],
        ['isBuy', '是否可购买', 'text']
    ]
    column_editable_list = ['des','isBuy']
    column_searchable_list = ['code', 'codeName', 'roe', 'pe','shizhi','isBuy','des']
    column_filters = column_searchable_list
    def __init__(self, session, **kwargs):
        self.net_init(self.columns)
        super(Quants_Admin, self).__init__(Quants, session, **kwargs)



