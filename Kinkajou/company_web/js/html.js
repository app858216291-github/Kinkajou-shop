const html_header=function(obj){
	var htmlStr=""
	var contact=getJson('/common/model/queryByFilter/?modelName=Net_Contact');
	contact=contact.items[0]

	htmlStr+='\
	    <div class="header-top">\
	        <div class="container">\
	            <div class="row">\
	                <div class="col-md-6 col-xs-12 col-sm-6 ">\
	                    <p><i class="fa fa-phone"> </i> '+contact.phone+'</p>\
	                </div>\
	                <div class="col-md-6 col-xs-12 col-sm-6 text-right">\
	                    <form class="navbar-form text-right" role="search">\
	                        <div class="form-group">\
	                            <input type="text" class="form-control" placeholder="带侧孔">\
	                            <i class="fa fa-search"></i>\
	                        </div>\
	                        <button type="submit" href="products.html" class="btn btn-default">搜索</button>\
	                    </form>\
	                </div>\
	            </div>\
	        </div>\
	    </div>\
	    <nav class="navbar" role="navigation">\
	        <div class="container">\
	            <!-- Brand and toggle get grouped for better mobile display -->\
	            <div class="navbar-header">\
	                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"\
	                        data-target="#bs-example-navbar-collapse-1">\
	                    <span class="sr-only">Toggle navigation</span>\
	                    <span class="icon-bar"></span>\
	                    <span class="icon-bar"></span>\
	                    <span class="icon-bar"></span>\
	                </button>\
	                <a class="logo" href="index.html" style="font-size:20px;color:black">\
	                    <B>福建径里农业开发有限公司<B>\
	                    <h1>径里花盆</h1>\
	                </a>\
	            </div>\
	            <!-- Collect the nav links, forms, and other content for toggling -->\
	            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\
	                <ul class="nav navbar-nav navbar-right">\
	                    <li><a class="{{1}}" href="index.html">首页</a></li>\
	                    <li><a class="{{2}}" href="profuile.html">公司介绍</a></li>\
	                    <li><a class="{{3}}" href="products.html">产品展示</a></li>\
	                    <li><a class="{{4}}" href="news.html">新闻动态</a></li>\
	                    <li><a class="{{5}}" href="join.html">品牌招商</a></li>\
	                    <li><a class="{{6}}" href="about.html">联系我们</a></li>\
	                </ul>\
	            </div><!-- /.navbar-collapse -->\
	        </div><!-- /.container-fluid -->\
	    </nav>';
	
	var page=pageName();
	debugger
	switch(page) {
     case "index.html":
        htmlStr=htmlStr.replace('{{1}}',"active");
        break;
     case "profuile.html":
        htmlStr=htmlStr.replace('{{2}}',"active");
        break;
	case "products.html":
        htmlStr=htmlStr.replace('{{3}}',"active");
        break;
	case "products_detail.html":
	    htmlStr=htmlStr.replace('{{3}}',"active");
	    break;
	case "news.html":
        htmlStr=htmlStr.replace('{{4}}',"active");
        break;
	case "new_detail.html":
	    htmlStr=htmlStr.replace('{{4}}',"active");
	    break;
	case "join.html":
        htmlStr=htmlStr.replace('{{5}}',"active");
        break;
	case "about.html":
        htmlStr=htmlStr.replace('{{6}}',"active");
        break;
     default:
        htmlStr=htmlStr.replace('{{1}}',"active");
	} 

	obj.getElementById("header").innerHTML=htmlStr;	
};
const html_footer=function(obj){
	
	var htmlStr=""
	htmlStr+='\
	<div class="footer-top link">\
	    <!--友情链接-->\
	    <div class="container">\
	        友情链接：\
	        <a href="http://www.jomoo.com.cn/">马克森英文网</a>\
	        <a href="http://www.jieju.cn/">智能家居</a>\
	        <a href="http://www.chinaweiyu.com/">中华橱柜网</a>\
	        <a href="http://www.wyw.cn/">中厨网</a>\
	        <a href="http://www.wyw.cn/">优信二手车</a>\
	        <a href="http://www.wyw.cn/">落阳地产</a>\
	        <a href="http://www.hegii.com/">汽车之家</a>\
	        <a href="https://shop68294732.taobao.com/?spm=a230r.7195193.1997079397.204.cYt8e7">马克森天猫商城</a>\
	    </div>\
	</div>\
	<!--备案号-->\
	<div class="footer-button">\
	    <div class="container">\
	        <p>服务热线：13774514086 在线QQ：370377860</p>\
	        <p>增值电信业务经营许可证：湘B2-20100052 福建径里农业发展公司 | 闽ICP备15045692号 | 售后服务热线: 13774514086</p>\
	        <!--百度分享-->\
	        <div class="bdsharebuttonbox">\
	            <a href="#" class="bds_more" data-cmd="more"></a>\
	            <a href="#" class="bds_qzone" data-cmd="qzone" title="分享到QQ空间"></a>\
	            <a href="#" class="bds_tsina" data-cmd="tsina" title="分享到新浪微博"></a><a\
	                href="#" class="bds_tqq" data-cmd="tqq" title="分享到腾讯微博"></a>\
	            <a href="#" class="bds_renren" data-cmd="renren" title="分享到人人网"></a>\
	            <a href="#" class="bds_weixin" data-cmd="weixin" title="分享到微信"></a>\
	        </div>\
	    </div>\
	</div>'
	var netIndex=getJson('/common/model/queryByFilter/?modelName=Net_Index');
	netIndex=netIndex.items[0]
	debugger
	obj.getElementById("footer").innerHTML=netIndex.footer;	
}
html_qqmodel=function(obj){
	var contact=getJson('/common/model/queryByFilter/?modelName=Net_Contact');
	contact=contact.items[0]
	var htmlStr="";
	htmlStr+='\
	<div class="izl-rmenu">\
	    <a class="consult" target="_blank">\
	        <div class="phone" style="display:none;">'+contact.kf_phone+'</div>\
	    </a>\
	    <a class="cart">\
	        <div class="pic" style="background: url(images/weixin.jpg); background-repeat:no-repeat;"></div>\
	    </a>\
	    <a href="javascript:void(0)" class="btn_top" style="display: block;"></a>\
	</div>\
	<a target="_blank" href="http://wpa.qq.com/msgrd?v=3&uin=370377860&site=qq&menu=yes" id="udesk-feedback-tab"\
	   class="udesk-feedback-tab-left" style="display: block; background-color: black;"></a>'
	obj.getElementById("qqmodel").innerHTML=htmlStr;	
}





