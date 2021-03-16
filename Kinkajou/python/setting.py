###应用参数
class FlaskConfig:
    ##数据库链接穿串
    SQLALCHEMY_DATABASE_URI=
    ##cookie，session用的秘钥
    SECRET_KEY = 
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    ##是否打印sql
    SQLALCHEMY_ECHO=False
    ##登录token秘钥
    TOKEN_KEY='djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr4s'
    ##图片服务器地址（该地址可以指向项目本身）
    FILESERVER=

##快递鸟
class KdApiConfig:
    # 请求url --正式地址
    ###免费版仅支持限500次/天（即时查询 支持四家 申通、圆通、百世、天天） 有效期半年  http://www.kdniao.com/
    Url = "https://api.kdniao.com/Ebusiness/EbusinessOrderHandle.aspx"
    # 电商加密私钥，快递鸟提供，注意保管，不要泄漏
    # 请登陆快递鸟用户管理后台查看：http://kdniao.com/UserCenter/UserHome.aspx
    AppKey = 
    # 电商ID
    EBusinessID =  # 请登陆快递鸟用户管理后台查看：http://kdniao.com/UserCenter/UserHome.aspx
##微信自动回复机器人
class Tuling:
    unit_token =
    unit_lanhua_botId =
    unit_url=
##微信公众号
class WeinXin:
    APP_ID =   # 你公众账号上的appid
    MCH_ID =  # 你的商户号
    API_KEY = ""  # 微信商户平台(pay.weixin.qq.com) -->账户设置 -->API安全 -->密钥设置，设置完成后把密钥复制到这里
    APP_SECRECT = 
    UFDODER_URL =   # 该url是微信下单api
    NOTIFY_URL =  # 微信支付结果回调接口，需要改为你的服务器上处理结果回调的方法路径
    CREATE_IP =  # 你服务器的IP

class Aliyun:
    AccessKeyID=
    AccessKeySecret=
    Url=
    bucketName=
    ReadUrl=
