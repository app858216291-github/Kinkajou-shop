###径里花盆
###应用参数
class FlaskConfig:
    ##数据库链接穿串
    SQLALCHEMY_DATABASE_URI="mysql://lanjie:Lj123456@rm-m5e86q52h5lpu678evo.mysql.rds.aliyuncs.com/gaozhai"
    #SQLALCHEMY_DATABASE_URI="sqlite:///sample_db.sqlite"
    ##cookie，session用的秘钥
    SECRET_KEY = '1234567'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    ##是否打印sql
    SQLALCHEMY_ECHO=False
    ##登录token秘钥
    TOKEN_KEY='djq%5cu#-jeq15abg$z9_i#_w=$o88m!*alpbedlbat8cr74s'
    ##图片服务器地址（该地址可以指向项目本身）
    FILESERVER='http://h5.huapen123.com/api/'
    WTF_CSRF_CHECK_DEFAULT=False
    SQLALCHEMY_BINDS = {
        'pzhtest': 'mysql://lanjie:Lj123456@rm-m5e86q52h5lpu678evo.mysql.rds.aliyuncs.com/shop'
    }
    key="149_160_163_94_102_150_169_91_93_160_"
    key_url="http://admin.huapen123.com/common/getTokenMonth/"
    domain="http://h5.huapen123.com"




##快递鸟
class KdApiConfig:
    # 请求url --正式地址
    ###免费版仅支持限500次/天（即时查询 支持四家 申通、圆通、百世、天天） 有效期半年  http://www.kdniao.com/
    Url = "https://api.kdniao.com/Ebusiness/EbusinessOrderHandle.aspx"
    # 电商加密私钥，快递鸟提供，注意保管，不要泄漏
    # 请登陆快递鸟用户管理后台查看：http://kdniao.com/UserCenter/UserHome.aspx
    AppKey = "19ef0f52-8d9c-4048-8052-50f1fc081056"
    # 电商ID
    EBusinessID = "1699162"  # 请登陆快递鸟用户管理后台查看：http://kdniao.com/UserCenter/UserHome.aspx
##微信自动回复机器人
class Tuling:
    unit_token = "24.1c29ead7573482e52e3fcde15787783f.2592000.1566399499.282335-15847392"
    unit_lanhua_botId = 15442
    unit_url='https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=x92bMFBxezirc4wWMcrzeYzg&client_secret=M7YgNvrMhgvyWMvsNNDpKUsy88z2F83Q'
##微信公众号 径里花盆
class WeinXin:
    APP_ID = "wx20f73b403b9b3b2f"  # 你公众账号上的appid
    MCH_ID = "1542612001"  # 你的商户号
    API_KEY = "ckiUP4CqKpJCYnqjkXBfV6wdnsfUT2nf"  # 微信商户平台(pay.weixin.qq.com) -->账户设置 -->API安全 -->密钥设置，设置完成后把密钥复制到这里
    APP_SECRECT = "dc3b62c86cd0af6bf957d3e3b867203c"
    UFDODER_URL = "https://api.mch.weixin.qq.com/pay/unifiedorder"  # 该url是微信下单api
    NOTIFY_URL = "http://120.24.221.15:5001/common/notify/"  # 微信支付结果回调接口，需要改为你的服务器上处理结果回调的方法路径
    CREATE_IP = '120.24.221.15'  # 你服务器的IP
    MP_APP_ID="wx404f3e7d6839135e" ##小程序appid
    MP_APP_SECRECT = "2448e179517e2966c3cd2ddc26a00f32"##小程序AppSecret
    MP_MCH_ID="1542612001"

class Aliyun:
    AccessKeyID='LTAIow0LIFQ8ZprF'
    AccessKeySecret='AiYBERNMriW85JBWoZPl62C9hMsago'
    Url='http://oss-cn-beijing.aliyuncs.com'
    bucketName='pyshop'
    ReadUrl='https://pyshop.oss-cn-beijing.aliyuncs.com/'

