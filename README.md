# 商城+公众号+小程序+app+前后台代码开源，一键启动




#### 介绍
蜜熊电商， [ 微信 + 支付宝 + 百度 + 头条 ] 小程序 + APP + 公众号 + PC + H5 + 企业官网[支持移动端和PC端]，注重界面美感与用户体验，解决线上开店，企业宣传和私域营销的问题。 【企业网站 商城 微信支付 积分支付 电商源码 小程序直播 跨境电商系统 支持国际化】  


#### 案例： 先睹为快，合适直接使用  （微信公众号：高宅，微信小程序：高宅，企业网站：径里）
![公众号](https://images.gitee.com/uploads/images/2021/0507/161122_c3937c32_1442520.jpeg "公众号") 
![微信小程序](https://images.gitee.com/uploads/images/2021/0706/124012_01b22937_1442520.jpeg "微信小程序")
![企业网站](https://images.gitee.com/uploads/images/2021/0706/124034_3848fe07_1442520.png "企业网站")
  
 
#### 功能介绍
![官网业务及功能介绍](https://images.gitee.com/uploads/images/2021/0706/131021_c210f967_1442520.png "官网业务及功能介绍.png") 
![商城业务及功能介绍](https://images.gitee.com/uploads/images/2021/0706/131037_33c188c2_1442520.png "商城业务及功能介绍.png") 

#### 软件架构
整体架构：
	项目主要采用Python3.8+uni-app+mysql  
	采用前后端分离，python和前端交采用json,pythonh后台支持一键安装依赖包，一键启动，前端有编译后的部署包可直接使用，也可使用Xbuild自己编译，并根据自己的需求自定义修改代码。  
	python用到的技术:Flask处理http请求，Flask-SQLAlchemy做数据库ORM操作。  

	对外耦合：微信平台（支付，分享），阿里云短信  


#### 目录说明  
1、python目录为python目录，是商城，官网，小程序的后端代码，执行的时候得安装python环境，有提供requests.txt  
2、h5目录为商城前端代码，为VUE框架，可以使用XBuilder编译执行。


3、（重点，无需安装执行）installer为程序打包后的文件，后端代码app.EXE可直接执行。访问前端代码h5反向代理执行（py_nginx或者读者可用nginx，apahce）。  

项目还处于开发阶段，安装包稳定性不是很好，有问题可以加QQ群247813615，群主很乐意给大家解答疑问

#### 安装教程
window:
1.  git上下载源码包自己编译  
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

1.   项目后端的模块，无需配置。支持集群部署，横向解决性能问题，具有并发无限拓展性
2.  模块耦合低，各个模块出现问题，都可以通过简单的测试定位，保护程序员头发
3.  封装了统一样式后台管理，通过简单配置可以形成数据库的增删改查，代码极简模式
4.  UNI-APP通吃所有移动入口，一套代码，解决所有问题。
5.  开源团队项目,永久技术支持，可商用，团队为技术爱好者，永不收费，热心支持解答问题。

#### 团队介绍：http://site.heshihuan.cn/

###  联系我们（技术交流）
QQ群
![输入图片说明](https://images.gitee.com/uploads/images/2021/0804/131320_870f65e1_1442520.jpeg "qq.jpg")
微信群
![输入图片说明](https://images.gitee.com/uploads/images/2021/0804/131508_ae41801c_1442520.png "微信截图_20210804131210.png")