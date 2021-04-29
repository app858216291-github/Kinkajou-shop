from admin.upload import FileUploadField, ImageUploadField
from flask_babelex import Babel
from flask_admin._compat import urljoin
from flask import redirect
from flask_admin._compat import quote
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import Admin, BaseView, expose
from flask_admin.babel import gettext, lazy_gettext
from flask import flash, redirect, abort, request, send_file
from flask_admin import form, helpers
import os.path as op
import flask_login as login
from wtforms.widgets import html_params

from common import aliyun
allowed_file = lambda filename: '.' in filename and filename.rsplit('.', 1)[1] in set(
            ['png', 'jpg', 'jpeg', 'gif', 'bmp'])
def uploadFile(f):
    if f and allowed_file(f.filename):
        return aliyun.upload(f,'product')
    else:
        return "filename is null"
class MXFileAdmin(FileAdmin):
    def is_accessible(self):
        if login.current_user.is_authenticated:
            if login.current_user.username=='admin':
                return True
            return False
        return False
    def _save_form_files(self, directory, path, form):

        super()
        filename = self._separator.join([directory, form.upload.data.filename])

        if self.storage.path_exists(filename):
            secure_name = self._separator.join([path, form.upload.data.filename])
            raise Exception(gettext('File "%(name)s" already exists.',
                                    name=secure_name))
        else:
            self.save_file(filename, form.upload.data)
            self.on_file_upload(directory, path, filename)

    @expose('/download/<path:path>')
    def download(self, path=None):
        """
            Download view method.
            :param path:
                File path.
        """
        if not self.can_download:
            abort(404)

        base_path, directory, path = self._normalize_path(path)

        # backward compatibility with base_url
        base_url = self.get_base_url()
        if base_url:
            base_url = urljoin(self.get_url('.index_view'), base_url)
            path=path.replace('\\', '/')
            print("------1------")
            print(base_url)
            print(path)
            return redirect(urljoin(quote(base_url), quote(path)))
        directory=directory.replace('\\', '/')
        print("-------2-----")
        print(directory)
        return self.storage.send_file(directory)

    @expose('/rename/', methods=('GET', 'POST'))
    def rename(self):

        """
            Rename view method
        """
        form = self.name_form()

        path = form.path.data
        if path:
            base_path, full_path, path = self._normalize_path(path)

            return_url = self._get_dir_url('.index_view', op.dirname(path))
        else:
            return redirect(self.get_url('.index_view'))

        if not self.can_rename:
            flash(gettext('Renaming is disabled.'), 'error')
            return redirect(return_url)

        if not self.is_accessible_path(path):
            flash(gettext('Permission denied.'), 'error')
            return redirect(self._get_dir_url('.index_view'))

        if not self.storage.path_exists(full_path):
            flash(gettext('Path does not exist.'), 'error')
            return redirect(return_url)

        if self.validate_form(form):
            try:
                dir_base = op.dirname(full_path)
                filename = form.name.data
                # print(fi)
                self.storage.rename_path(full_path, self._separator.join([dir_base, filename]))
                self.on_rename(full_path, dir_base, filename)
                flash(gettext('Successfully renamed "%(src)s" to "%(dst)s"',
                              src=op.basename(path),
                              dst=filename), 'success')
            except Exception as ex:
                flash(gettext('Failed to rename: %(error)s', error=ex), 'error')

            return redirect(return_url)
        else:
            helpers.flash_errors(form, message='Failed to rename: %(error)s')

        if self.rename_modal and request.args.get('modal'):
            template = self.rename_modal_template
        else:
            template = self.rename_template

        return self.render(template, form=form, path=op.dirname(path),
                           name=op.basename(path), dir_url=return_url,
                           header_text=gettext('Rename %(name)s',
                                               name=op.basename(path)))
from flask_admin.helpers import get_url
from flask_admin._compat import string_types, urljoin
class MxImageUploadField(ImageUploadField):

    def _save_file(self, data, filename):

        path = self._get_path(filename)
        data.seek(0)
        filename=uploadFile(data)
        return filename
    # def __call__(self, field, **kwargs):
    #     kwargs.setdefault('id', field.id)
    #     kwargs.setdefault('name', field.name)
    #
    #     args = {
    #         'text': html_params(type='hidden',
    #                             value=field.data,
    #                             name=field.name),
    #         'file': html_params(type='file',
    #                             **kwargs),
    #         'marker': '_%s-delete' % field.name
    #     }
    #
    #     if field.data and isinstance(field.data, string_types):
    #         url = self.get_url(field)
    #         args['image'] = html_params(src=url)
    #
    #         template = self.data_template
    #     else:
    #         template = self.empty_template
    #     print(template % args)
    #     return Markup(template % args)
    def get_url(self, field):
        if field.thumbnail_size:
            filename = field.thumbnail_fn(field.data)
        else:
            filename = field.data

        if field.url_relative_path:
            filename = urljoin(field.url_relative_path, filename)

        return get_url(field.endpoint, filename=filename)
