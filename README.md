# 商城+公众号+小程序+app+前后台代码开源，一键启动

#### 介绍
蜜熊电商， [ 微信 + 支付宝 + 百度 + 头条 ] 小程序 + APP + 公众号 + PC + H5，企业官网[支持移动端和PC端]，注重界面美感与用户体验，解决线上开店，企业宣传和私域营销的问题。 【企业网站 商城 微信支付 积分支付 电商源码 小程序直播 跨境电商系统 支持国际化】

#### 软件架构
整体架构：
	项目主要采用Python3.8+uni-app+mysql
	采用前后端分离，python和前端交采用json,pythonh后台支持一键安装依赖包，一键启动，前端有编译后的部署包可直接使用，也可使用Xbuild自己编译，并根据自己的需求自定义修改代码。
	python用到的技术:Flask处理http请求，Flask-SQLAlchemy做数据库ORM操作。

	对外耦合：微信平台（支付，分享），阿里云短信

#### 安装教程
window:
1.  下载安装包（可git上下载源码包自己编译）
2.  安装商城前端代码
3.  安装官网
4.  安装后台管理系统

#### 使用说明

1.  商城可支持微信支付


#### 参与贡献

项目搭建过程中，碰到问题可加QQ群：247813615
提供免费mysql数据库供支持者使用。
提供免费文件服务器，供支持者使用。


###  项目截图
![首页](https://images.gitee.com/uploads/images/2021/0220/125859_7188eab7_1442520.png "首页.png")
![分类](https://images.gitee.com/uploads/images/2021/0220/125918_47d8cc7d_1442520.png "分类.png")
![商品详情](https://images.gitee.com/uploads/images/2021/0220/125932_e8a83e3b_1442520.png "商品详情.png")
![购物车](https://images.gitee.com/uploads/images/2021/0220/125942_036bfc74_1442520.png "购物车.png")
![个人中心](https://images.gitee.com/uploads/images/2021/0220/125957_70f230bb_1442520.png "个人中心.png")

#### 特技

1.   项目后端的模块，支持.exe直接启动，无需配置。支持集群部署，横向解决性能问题，具有并发无限拓展性
2.  模块耦合低，各个模块出现问题，都可以通过简单的测试定位，保护程序员头发
3.  封装了统一样式后台管理，通过简单配置可以形成数据库的增删改查，代码极简模式
4.  UNI-APP通吃所有移动入口，一套代码，解决所有问题。
5.  开源团队项目，可商用，团队为技术爱好者，永不收费，热心支持解答问题。
