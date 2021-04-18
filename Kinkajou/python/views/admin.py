from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
class MyView(BaseView):
    @expose('/cc')
    def index(self):
        return self.render('index.html')
    @expose('/cc')
    def default(self):
        return self.render('index.html')
class MyAdminIndexView(AdminIndexView):
    @expose('/skuedit')
    def skuEdit(self):
        return self.render('sku-edit.html')
    @expose('/')
    def default(self):
        return self.render('index.html')
