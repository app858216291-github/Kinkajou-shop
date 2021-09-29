import threading

from common.tools import eMailUtil
from model.models import User, Order, Product, PayRecord, Product_Order, Skuthird, PYSHOP_CONSTANT, Address, requestLog

orderlock=threading.RLock()##订单锁

class ShopService:
    ##是否可以支付
    def isPayMethod(orderNum):
        code=1
        result=""
        print("进入公共支付方法")
        order = Order().query.filter(Order.orderNo == orderNum,).first()
        if order==None:
            code = -1
            result = "订单不存在"

        user = User.query.filter(User.id == order.userId).first()
        if user==None:
            code = -1
            result = "用户不存在"

        productOrders = Product_Order().query.filter(Product_Order.orderid == order.id).all()
        ##根据订单信息，对应产品减少库存
        for productOrder in productOrders:
            if productOrder.propid == 0:  ##没有sku直接操作产品库存
                product = Product().get(productOrder.productid)
                # 库存不足，先不处理，用负数填充
                if product.store<productOrder.mount:
                    code = -1
                    result = str(product.title)+":产品库存不足，支付失败"
                    order.updateOrAdd()
                    break
            else:  ##有sku，操作sku库存
                skuthird = Skuthird().get(productOrder.propid)
                if skuthird == None:
                    print(productOrder.propid)
                    code = -1
                    result = str(productOrder.propid)+"该sku不存在"
                    break
                if skuthird.store<productOrder.mount:
                    code=7
                    result=str(skuthird.title)+"产品库存不足，支付失败"
                    order.updateOrAdd()
                    break
        return code,result

    ##订单支付接口
    def payMethod(orderNum, money):
        print("进入公共支付方法")
        result = "支付成功"
        code = 1
        orderlock.acquire()
        try:
            order = Order().query.filter(Order.orderNo == orderNum).first()
            order.mount = money
            order.orderStatus = 2

            user = User.query.filter(User.id == order.userId).first()
            user.credit += money

            productOrders = Product_Order().query.filter(Product_Order.orderid == order.id).all()
            ##根据订单信息，对应产品减少库存
            for productOrder in productOrders:
                if productOrder.propid == 0:  ##没有sku直接操作产品库存
                    product = Product().get(productOrder.productid)
                    # 库存不足，先不处理，用负数填充
                    # if product.store<productOrder.mount:
                    #     code = 7
                    #     result = "产品库存不足，支付失败"
                    #     order.updateOrAdd()
                    #     break
                    # else :
                    #     product.store=product.store-productOrder.mount
                    #     product.updateOrAdd()
                    product.store = product.store - productOrder.mount
                    product.updateOrAdd()
                else:  ##有sku，操作sku库存
                    skuthird = Skuthird().get(productOrder.propid)
                    if skuthird == None:
                        print(productOrder.propid)
                        print("该sku不存在")
                        break
                    # if skuthird.store<productOrder.mount:
                    #     code=7
                    #     result="产品库存不足，支付失败"
                    #     order.updateOrAdd()
                    #     break
                    # else :
                    #     skuthird.store=skuthird.store-productOrder.mount
                    #     skuthird.updateOrAdd()
                    if skuthird.store == None:
                        skuthird.store = 0
                    skuthird.store = skuthird.store - productOrder.mount
                    skuthird.updateOrAdd()
                ##异常则保存并返回
                # if code==7:
                #     order.orderStatus=7
                #     order.remark=result
                #     order.updateOrAdd()
                #     return

            order.updateOrAdd()
            user.updateOrAdd()
            address=Address().get(order.addressId)
            orderStr = "订单号：" + str(
                order.orderNo) + "，收货人：" + address.receiver + "，收货地址：" + address.address + ",订单金额" + str(
                order.mount) + "，下单时间：" + str(order.create_time)
            ShopService.sys_notify(content=orderStr, title="订单支付")
            # ShopService.sys_notify(content="订单支付成功，订单内容:" + order.tojson())
        except BaseException:
            pass
        finally:
            orderlock.release()
    def getSysConfig(key):
        config=PYSHOP_CONSTANT().query.filter(PYSHOP_CONSTANT.key == key).first()
        if config!=None:
            return config.value

        else:
            return ""
        return PYSHOP_CONSTANT().query.filter(PYSHOP_CONSTANT.key == key).one()
    ##系统消息提醒接口
    def sys_notify(content,title="kinkajou提醒邮件"):
        cons=ShopService.getSysConfig("notify_email")
        tag=ShopService.getSysConfig("isSendEmail")

        address=cons.split(',')
        to_addr = address

        ##记录发送日志
        log=requestLog()
        log.type=1
        log.ip=address
        log.key=title
        log.content=content
        log.add()
        if str(tag)!="0":
            eMailUtil.sendMail(to_addr=[to_addr], title=title,content=content)

    ##系统消息提醒接口
    def sys_notify_add(content, address="370377860@qq.com",title="kinkajou提醒邮件"):

        tag = ShopService.getSysConfig("isSendEmail")
        to_addr = address

        ##记录发送日志
        log = requestLog()
        log.type = 1
        log.ip = address
        log.key = title
        log.content = content
        log.add()
        if str(tag) != "0":
            eMailUtil.sendMail(to_addr=[to_addr], title=title, content=content)


