from flask import session,current_app,jsonify,request
import functools
from model.modelBase import Jsonfy
from common.tools import IOUtil
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def is_login(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        # user = session.get('userid')
        admin=request.args.get('admin')
        if admin!= None:
            return func(*args, **kwargs)
        token=request.headers.get('token')
        if token==None:
            return Jsonfy(code=-2, data="no login").__str__()
        userid=IOUtil.verifyToken(token)
        if userid==-1:
            return Jsonfy(code=-2, data="no login").__str__()
        return func(*args,**kwargs)
    return inner

def is_login_commonpath(func):
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

def isTokenUse(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        # user = session.get('userid')
        token=request.headers.get('token')
        if token==None:
            return Jsonfy(code=-2, data="no token be accese,please take your token in header").__str__()
        tokenTime=int(IOUtil.dectry(token))
        import time
        t = time.time()
        t = int(t)
        if tokenTime<t:
            return Jsonfy(code=-2, data="token is timeout,the token is useless").__str__()
        return func(*args,**kwargs)
    return inner

def monitor(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        # user = session.get('userid')

        token=request.args.get('token')
        ip = request.remote_addr
        if token==None:
            return Jsonfy(code=-2, data="no token be accese,please take your token in header").__str__()
        token=IOUtil.dectry(token)

        return func(*args,**kwargs)
    return inner

