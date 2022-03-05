from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from wtforms import form, fields, validators
from flask_admin.contrib import sqla
import flask_login as login
from flask import Flask, url_for, redirect, render_template, request
from flask_admin import helpers, expose
from model.modelBase import db
from model.models import PayRecord, User
from werkzeug.security import generate_password_hash, check_password_hash


# Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    username = fields.StringField(label='用户名',validators=[validators.required()],description="请输入用户名",render_kw={"required":"required"})
    print(login)
    password = fields.PasswordField(label='密   码',validators=[validators.required()],description="请输入密码",render_kw={"required":"required"})
    print(password)
    def login_validate(self):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if user.password!=self.password.data:
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(username=self.username.data,password=self.password.data).first()

class RegistrationForm(form.Form):
    username = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate(self):
        if db.session.query(User).filter_by(username=self.username.data).count() > 0:
            raise validators.ValidationError('Duplicate username')



# Create customized index view class that handles login & registration
class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            if user==None:

                link = '<p>username or password is error</a></p>'
                self._template_args['form'] = form
                self._template_args['link'] = link
                return super(MyAdminIndexView, self).index()

            login.login_user(user)
        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if db.session.query(User).filter_by(username=form.username.data).count() == 0:
            user = User()

            form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            user.password = form.password.data

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))
    @expose('/skuedit')
    def skuEdit(self):
        if login.current_user.is_authenticated:
            if login.current_user.username=='admin':
                return self.render('sku-edit.html')
            return False
        return False
