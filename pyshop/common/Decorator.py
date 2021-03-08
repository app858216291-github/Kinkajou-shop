from flask import session,current_app,jsonify,request
import functools
from model.modelBase import Jsonfy
from common.tools import IOUtil
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def is_login(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        # user = session.get('userid')
        token=request.headers.get('token')
        if token==None:
            return Jsonfy(code=-2, data="no login").__str__()
        userid=IOUtil.verifyToken(token)
        if userid==-1:
            return Jsonfy(code=-2, data="no login").__str__()
        return func(*args,**kwargs)
    return inner

