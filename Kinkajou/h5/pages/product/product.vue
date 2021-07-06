<template>
	<view class="container">
		<view class="carousel">
			<swiper indicator-dots circular=true duration="400">
				<swiper-item class="swiper-item" v-for="(item,index) in imgList" :key="index">
					<view class="image-wrapper">
						<image
							:src="item"
							class="loaded"
							mode="aspectFill"
						></image>
					</view>
				</swiper-item>
			</swiper>

		</view>
		
		<view class="introduce-section">
			<text class="title">{{product.title}}</text>
			<view class="price-box">
				<text class="price-tip">¥</text>
				<text class="price">{{skuPrice}}</text>
				<text class="m-price">¥{{skuPrice*2}}</text>
				<text class="coupon-tip">5折</text>
			</view>
			<view class="bot-row">
				<text>销量: {{product.sales}}</text>
				<text>库存: {{product.store}}</text>
				<text>浏览量: {{product.skim}}</text>
			</view>
		</view>
		
		<!--  分享 -->
<!-- 		<view class="share-section" @click="share">
			<view class="share-icon">
				<text class="yticon icon-xingxing"></text>
				 返
			</view>
			<text class="tit">该商品分享可领49减10红包</text>
			<text class="yticon icon-bangzhu1"></text>
			<view class="share-btn">
				立即分享
				<text class="yticon icon-you"></text>
			</view>
			
		</view> -->
		
		<view class="c-list">
			<view class="c-row b-b" @click="toggleSpec">
				<text class="tit">购买类型</text>
				<view class="con">
					<text class="selected-text" v-for="(sItem, sIndex) in specSelected" :key="sIndex">
						{{sItem.name}}
					</text>
				</view>
				<text class="yticon icon-you"></text>
			</view>
			<!-- <view class="c-row b-b">
				<text class="tit">优惠券</text>
				<text class="con t-r red">领取优惠券</text>
				<text class="yticon icon-you"></text>
			</view> -->
			<!-- <view class="c-row b-b">
				<text class="tit">促销活动</text>
				<view class="con-list">
					<text>新人首单送20元无门槛代金券</text>
					<text>订单满50减10</text>
					<text>订单满100减30</text>
					<text>单笔购买满两件免邮费</text>
				</view>
			</view> -->
			<view class="c-row b-b">
				<text class="tit">服务</text>
				<view class="bz-list con">
					<text>7天无理由退换货 ·</text>
					<text>假一赔十 ·</text>
				</view>
			</view>
		</view>
		
		<!-- 评价 -->
		<view class="eva-section" v-if="rateShow">
			<view class="e-header">
				<text class="tit">评价</text>
				<text @click="navToDetailPage()">(86)</text>
				<text class="empty"></text>
				<text class="tip" @click="navToDetailPage()">好评率 100%</text>
				<text class="yticon icon-you" @click="navToDetailPage()"></text>
			</view> 
			<view class="eva-box">
				<image class="portrait" src="http://img3.imgtn.bdimg.com/it/u=1150341365,1327279810&fm=26&gp=0.jpg" mode="aspectFill"></image>
				<view class="right">
					<text class="name">{{rate.nickname}}</text>
					<text class="con">{{rate.evaluate}}</text>
					<view class="bot">
						<text class="attr">购买类型：{{rate.basename}} {{rate.funame}}</text>
						<text class="time">2019-04-01 19:21</text>
					</view>
				</view>
			</view>
		</view>
		
		<view class="detail-desc">
			<view class="d-header">
				<text>图文详情</text>
			</view>
			<rich-text :nodes="desc"></rich-text>
		</view>
		
		<!-- 底部操作菜单 -->
		<view class="page-bottom">
			<navigator url="/pages/index/index" open-type="switchTab" class="p-b-btn">
				<text class="yticon icon-xiatubiao--copy"></text>
				<text>首页</text>
			</navigator>
			
			<view class="p-b-btn" :class="{active: favorite}" @click="toFavorite()">
				<text class="yticon icon-shoucang"></text>
				<text>收藏</text>
			</view>
			
			<view class="action-btn-group">
				<button type="primary" class=" action-btn no-border buy-now-btn" @click="toggleSpec('buy')">立即购买</button>
				<button type="primary" class=" action-btn no-border add-cart-btn"  @click="toggleSpec('addCar')">加入购物车</button>
			</view>
		</view>
		
		
		<!-- 规格-模态层弹窗 -->
		<view v-if="isskuNull==false" 
			class="popup spec" 
			:class="specClass"
			@touchmove.stop.prevent="stopPrevent"
			@click="toggleSpec"
		>
			<!-- 遮罩层 -->
			<view class="mask"></view>
			<view class="layer attr-content" @click.stop="stopPrevent">
				<view class="a-t">
					<image :src="imgList[0]"></image>
					<view class="right">
						<text class="price">¥{{skuPrice}}</text>
						<text class="stock">库存：{{skuStore}}件</text>
						<view class="selected">
							已选：
							<text class="selected-text" v-for="(sItem, sIndex) in specSelected" :key="sIndex">
								{{sItem.name}}
							</text>
						</view>
					</view>
				</view>
				<view v-for="(item,index) in specList" :key="index" class="attr-list">
					<text>{{item.name}}</text>
					<view class="item-list">
						<text 
							v-for="(childItem, childIndex) in specChildList" 
							v-if="childItem.pid === item.id"
							:key="childIndex" class="tit"
							:class="{selected: childItem.selected}"
							@click="selectSpec(childIndex, childItem.pid)"
						>
							{{childItem.name}}
						</text>
					</view>
				</view>
				<button v-if="buystatus" class="btn" @click="buy">下一步</button>
				<button v-if="carstatus" class="btn" @click="addCar">加入购物车</button>
			</view>
		</view>
		<!-- 分享 
		<share 
			ref="share" 
			:contentHeight="580"
			:shareList="shareList"
		></share>-->
	</view>
</template>

<script>
	// var wx = require('@/components/weixin/jweixin-1.6.0.js');
	import share from '@/components/share';
	var wx = require('jweixin-module')
	import {
		mapState
	} from 'vuex';
	export default{
		components: {
			share
		},
		computed:{
			...mapState(['userInfo']),
			...mapState(['hasLogin'])
		},
		onNavigationBarButtonTap(e) {  
				
				if (e.index == 0) {  
					this.$refs.share.toggleMask();	
					 
				} else if (e.index == 1) {  
					uni.navigateTo({  
						url: "/pages/cart/cart2"  
					});   
				}  
		
			} ,
		data() {
			return {
				buystatus:true,
				carstatus:false,
				skuThird:[],
				isskuNull:false,
				baseid:0,
				fuid:0,
				skuPrice:100,
				skuStore:0,
				prop:{},
				productid:0,
				specClass: 'none',
				specSelected:[],
				product:{},
				rate:{},
				rateShow:false,
				favorite: false,
				shareList: [{
								type: 1,
								icon: '/static/temp/share_wechat.png',
								text: '微信好友'
							},
							{
								type: 2,
								icon: '/static/temp/share_moment.png',
								text: '朋友圈'
							},
							{
								type: 3,
								icon: '/static/temp/share_qq.png',
								text: 'QQ好友'
							},
							{
								type: 4,
								icon: '/static/temp/share_qqzone.png',
								text: 'QQ空间'
							}
						],
				imgList: [],
				desc:"",
			
				specList: [
					{
						id: 1,
						name: '尺寸',
					},
					{	
						id: 2,
						name: '颜色',
					},
				],
				specChildList: [
					{
						id: 1,
						pid: 1,
						name: 'XS',
					},
					{
						id: 2,
						pid: 1,
						name: 'S',
					},
					{
						id: 3,
						pid: 1,
						name: 'M',
					},
					{
						id: 4,
						pid: 1,
						name: 'L',
					},
					{
						id: 5,
						pid: 1,
						name: 'XL',
					},
					{
						id: 6,
						pid: 1,
						name: 'XXL',
					},
					{
						id: 7,
						pid: 2,
						name: '白色',
					},
					{
						id: 8,
						pid: 2,
						name: '珊瑚粉',
					},
					{
						id: 9,
						pid: 2,
						name: '草木绿',
					},
				]
			};
		},
		
		async onLoad(options){
			let isLogin=this.$api.login_openid();
			if (!isLogin){
				let redirect_url=await this.$api.get(this.$shop.prop().serviceUrl+'/common/getOpenidUrl',{})
				window.location.href=redirect_url;
			}
			

			
			
			//    document.addEventListener('WeixinJSBridgeReady', function onBridgeReady() {// 
			  
			//               //发送给好友
			//               WeixinJSBridge.on('menu:share:appmessage', function (argv) {
			//                   this.shareFriend();
			//               });
			//               //分享到朋友圈
			//               WeixinJSBridge.on('menu:share:timeline', function (argv) {
			//                   this.shareTimeline();
			//               });
			  
			//           }, false);

			
			//---end分享-
			
			//接收传值,id里面放的是标题，因为测试数据并没写id 
			let id = options.id;
			this.productid=id;
			if(id){
				// this.$api.msg(`点击了${id}`);
				//添加浏览记录
				
				// console.info(this.$shop.prop().serviceUrl)
				//数据库添加浏览记录
				await this.$api.get(this.$shop.prop().serviceUrl+'/user/addhis?productid='+id,{})
				//本地添加浏览记录
				this.$api.setStoreHis(id)
				
				
			}
			let skufirst,skufirst2
			// sku级联关系
			let skus=await this.$api.get(this.$shop.prop().serviceUrl+'/product/skuview?productid='+this.productid,{})
			if(skus.data.skufirst==null){
				this.isskuNull=true;
				skus=await this.$api.get(this.$shop.prop().serviceUrl+'/product/skuview?productid=0',{})
				
			
			}
			
			skufirst=skus.data.skufirst;
			skufirst2=[{"id": skufirst.baseid,"name": skufirst.basename},{"id": skufirst.fuid,"name": skufirst.funame}]
			this.specList=skufirst2;
			this.specChildList=skus.data.skusecond;
			this.skuThird=skus.data.skuthird;
			
			console.info(this.skuPrice)
			// console.info(this.skuPrice)
			console.info(this.skuThird[0].price)
			console.info(this.skuThird[0].store)
			this.skuPrice=this.skuThird[0].price;
			this.skuStore=this.skuThird[0].store;
			
			for(let i=0;i<this.specChildList.length;i++){
				
				this.specChildList[i].id=this.specChildList[i].propertyid;
				this.specChildList[i].name=this.specChildList[i].propertyname;
				this.specChildList[i].pid=this.specChildList[i].firstid;
			}
			
			//规格 默认选中第一条
			this.specList.forEach(item=>{
				for(let cItem of this.specChildList){
					if(cItem.pid === item.id){
						this.$set(cItem, 'selected', true);
						this.specSelected.push(cItem);
						break; //forEach不能使用break
					}
				}
			})
			
			
			
			for(let third of this.skuThird){
				if (this.specSelected.length!=2){
					console.info("已选属性不是2个，有问题")
					break
				}
				if(this.specSelected[0].id==third.baseid && this.specSelected[1].id==third.fuid){
					this.skuPrice=third.price
					this.skuStore=third.store
					this.prop=third
					break
				}else if(this.specSelected[1].id==third.baseid && this.specSelected[0].id==third.fuid){
					this.skuPrice=third.price
					this.skuStore=third.store
					this.prop=third
					break
				}
			}
			
			this.product=await this.$shop.getProduct(this.$shop.prop().serviceUrl+'/product/productDetail?id='+id,{})
			
			//-------------分享---start-
			//判断是否微信登陆

			var ua = window.navigator.userAgent.toLowerCase();
			console.log(ua);//mozilla/5.0 (iphone; cpu iphone os 9_1 like mac os x) applewebkit/601.1.46 (khtml, like gecko)version/9.0 mobile/13b143 safari/601.1
			if (ua.match(/MicroMessenger/i) == 'micromessenger') {
				let _self=this
				let config=await this.$api.get(this.$shop.prop().serviceUrl+'/wx/index',{})
				wx.config({
					//debug: true, // 开启调试模式,调用的所有api的返回值会在客户端alert出来，若要查看传入的参数，可以在pc端打开，参数信息会通过log打出，仅在pc端时才会打印。
					appId: config.data.appid, // 必填，公众号的唯一标识
					timestamp: config.data.timestamp, // 必填，生成签名的时间戳
					nonceStr: config.data.nonceStr, // 必填，生成签名的随机串
					signature: config.data.signature, // 必填，签名，见微信开发文档附录1
					jsApiList: ['updateAppMessageShareData', 'updateTimelineShareData', 'onMenuShareAppMessage']
				});
				
				wx.ready(function() {
					// alert(_self.product.title)
					// alert(_self.product.main_image)
					// config信息验证后会执行ready方法，所有接口调用都必须在config接口获得结果之后，config是一个客户端的异步操作，所以如果需要在页面加载时就调用相关接口，则须把相关接口放在ready函数中调用来确保正确执行。对于用户触发时才调用的接口，则可以直接调用，不需要放在ready函数中。
					//分享至微信好友				
					wx.updateAppMessageShareData({
						title: _self.product.title, // 分享标题
						desc: _self.product.title, // 分享描述
						link: 'http://www.heshihuan.cn/#/pages/product/product?id=6', // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
						imgUrl: _self.$shop.getYunImage(_self.product.main_image), // 分享图标
						success: function() {
							// alert("分享朋友成功")
							// 用户点击了分享后执行的回调函数
							console.info("分享成功")
						},
					});
					//分享朋友圈
					
					wx.updateTimelineShareData({
						title: _self.product.title,
						link: 'http://www.heshihuan.cn/#/pages/product/product?id=6', // 分享链接，该链接域名或路径必须与当前页面对应的公众号JS安全域名一致
						imgUrl: _self.$shop.getYunImage(_self.product.main_image), // 分享图标
						success: function() {
								// alert("分享朋友圈成功")
						// 用户确认分享后执行的回调函数
						console.log('进入分享');
						},
						cancel: function() {
						// 用户取消分享后执行的回调函数
						console.log('取消分享');
						}
					});
				
				
				});
				wx.error(function(res){
					debugger
					alert(res)
				    console.log(res);
				});
			} else {
				console.info("普通浏览器")// 普通浏览器中打开
				
			}

			
			//---分享end
			
			
			
			
			
			let mainImgs=this.product.main_image
			if(mainImgs[0]==','){
				mainImgs=mainImgs.substring(1,mainImgs.length)
			}
			if(mainImgs!=undefined && mainImgs!=""){
				this.imgList.push(this.$shop.getYunImage(mainImgs))
			}
			if(this.product.image800!=undefined && this.product.image800!=""){
				this.imgList.push(this.$shop.getYunImage(this.product.image800))
			}
			if(this.product.image400!=undefined && this.product.image400!=""){
				this.imgList.push(this.$shop.getYunImage(this.product.image400))
			}
			if(this.product.image200!=undefined && this.product.image200!=""){
				this.imgList.push(this.$shop.getYunImage(this.product.image200))
			}
			if(this.product.image100!=undefined && this.product.image100!=""){
				this.imgList.push(this.$shop.getYunImage(this.product.image100))
			}
			

			// let detailImgs=this.product.detail_image
			// if(detailImgs[0]==','){
			// 	detailImgs=detailImgs.substring(1,detailImgs.length)
			// }
			// let arrayImages=detailImgs.split(',')
			// let d='<div style="width:100%">'
			// for(var i=0;i<arrayImages.length;i++){
			// 	d=d+'<img style="width:100%;display:block;" src="'+arrayImages[i]+'?x-oss-process=image/resize,h_400" />';
			// }
			// d=d+'</div>';
			let detailImgs=this.product.detail_image.replace(/\<img/gi, '<img style="max-width:100%;height:auto" ')
			
			this.desc=detailImgs;
			
			//查看是否有收藏						
			let iscollected=await this.$api.get(this.$shop.prop().serviceUrl+'/user/collectList',{"productid":id})
			this.favorite=iscollected.data
			
			let rates=await this.$api.get(this.$shop.prop().serviceUrl+'/product/rateList?productid='+this.productid,{})
			if (rates.data.length>0)
			{
				this.rateShow=true
				this.rate=rates.data[0]
			}
			// this.rate=rates.data[0]
			
	
		},
		methods:{
			// shareFriend(){
				
			//     WeixinJSBridge.invoke('sendAppMessage', {
			//         "appid": 'wx30969916c8d408fc',
			//         "img_url": 'https://pyshop.oss-cn-beijing.aliyuncs.com/product/202104131305028758.jpg?x-oss-process=image/resize,h_400',
			//         "img_width": "200",
			//         "img_height": "200",
			//         "link": 'www.heshihuan.cn',
			//         "desc": '产品分享',
			//         "title": '产品分享2'
			//     }, function (res) {
			//         //_report('send_msg', res.err_msg);
			//     })
			// },
			// //分享到朋友圈
			// shareTimeline() {
			//     WeixinJSBridge.invoke('shareTimeline', {//
			//         "img_url": 'https://pyshop.oss-cn-beijing.aliyuncs.com/product/202104131305028758.jpg?x-oss-process=image/resize,h_400',
			//         "img_width": "200",
			//         "img_height": "200",
			//         "link":  'www.heshihuan.cn',
			//         "desc": '产品分享3',
			//         "title": '产品分享4'
			//     }, function (res) {
			//         //_report('timeline', res.err_msg);
			//     });
			// },
			//规格弹窗开关
			toggleSpec(param) {
				
				
				
				if(param=="buy"){
					if(this.isskuNull){
						this.prop.id=0
						this.buy()
						return
					}
					this.buystatus=true;
					this.carstatus=false;
				}else if(param=="addCar"){
					if(this.isskuNull){
						this.prop.id=0
						this.addCar()
						return
					}
					this.buystatus=false;
					this.carstatus=true;
				}
				if(this.specClass === 'show'){
					this.specClass = 'hide';
					setTimeout(() => {
						this.specClass = 'none';
					}, 250);
				}else if(this.specClass === 'none'){
					this.specClass = 'show';
				}
			},
			navToDetailPage(item){
				//测试数据没有写id，用title代替
				// let id = item.title;
				// let id = item.id;
				let pid=this.productid
				uni.navigateTo({
					url: `/pages/product/rateList?productid=${pid}`
				})
			},
			
			navTo(url){
				
				uni.navigateTo({  
					url
				})  
			}, 
			//选择规格
			selectSpec(index, pid){
					console.info("22")
				
				let list = this.specChildList;
				list.forEach(item=>{
					if(item.pid === pid){
						this.$set(item, 'selected', false);
					}
				})

				this.$set(list[index], 'selected', true);
				//存储已选择
				/**
				 * 修复选择规格存储错误
				 * 将这几行代码替换即可
				 * 选择的规格存放在specSelected中
				 */
				this.specSelected = []; 
				list.forEach(item=>{ 
					if(item.selected === true){ 
						this.specSelected.push(item); 
					} 
				})
							//商品价格，库存查询
				for(let third of this.skuThird){
					if (this.specSelected.length!=2){
						console.info("已选属性不是2个，有问题")
						break
					}
					if(this.specSelected[0].id==third.baseid && this.specSelected[1].id==third.fuid){
						this.skuPrice=third.price
						this.skuStore=third.store
						this.prop=third
						break
					}else if(this.specSelected[1].id==third.baseid && this.specSelected[0].id==third.fuid){
						this.skuPrice=third.price
						this.skuStore=third.store
						this.prop=third
						break
					}
				}
				
			},
			//分享
			share(){
				
				this.$refs.share.toggleMask();	
			},
			
			//收藏
			toFavorite(){
				this.$api.get(this.$shop.prop().serviceUrl+'/user/addcollect?productid='+this.productid,{});
				this.favorite=!this.favorite
				// let iscollected=this.$api.get(this.$shop.prop().serviceUrl+'/user/collectList',{"productid":this.productid})
				// this.favorite=iscollected.data
				
			},
			buy(){
				// let a=this.prop;
				// this.toggleSpec("buy");
			
				uni.navigateTo({
					url: `/pages/order/createOrder?productid=${this.product.id}&prop=${this.prop.id}`
				})
			},
			 async addCar(){
				// this.toggleSpec("addCar")
				let r=await this.$api.get(this.$shop.prop().serviceUrl+"/product/addCar?productid="+this.product.id+"&propid="+this.prop.id,"")
				if(r.code==-2){
					uni.navigateTo({
						url: '/pages/public/login'
					})
					
				}
				
				this.$api.msg("购物车加入成功");
				this.toggleSpec()
			},
			stopPrevent(){},
			
		},

	}
</script>

<style lang='scss'>
	page{
		background: $page-color-base;
		padding-bottom: 160upx;
	}
	
	#buy{
		
	}
	#addCar{
		display:none
	}
	.icon-you{
		font-size: $font-base + 2upx;
		color: #888;
	}
	.carousel {
		height: 722upx;
		position:relative;
		swiper{
			height: 100%;
		}
		.image-wrapper{
			width: 100%;
			height: 100%;
		}
		.swiper-item {
			display: flex;
			justify-content: center;
			align-content: center;
			height: 750upx;
			overflow: hidden;
			image {
				width: 100%;
				height: 100%;
			}
		}
		
	}
	
	/* 标题简介 */
	.introduce-section{
		background: #fff;
		padding: 20upx 30upx;
		
		.title{
			font-size: 32upx;
			color: $font-color-dark;
			height: 50upx;
			line-height: 50upx;
		}
		.price-box{
			display:flex;
			align-items:baseline;
			height: 64upx;
			padding: 10upx 0;
			font-size: 26upx;
			color:$uni-color-primary;
		}
		.price{
			font-size: $font-lg + 2upx;
		}
		.m-price{
			margin:0 12upx;
			color: $font-color-light;
			text-decoration: line-through;
		}
		.coupon-tip{
			align-items: center;
			padding: 4upx 10upx;
			background: $uni-color-primary;
			font-size: $font-sm;
			color: #fff;
			border-radius: 6upx;
			line-height: 1;
			transform: translateY(-4upx); 
		}
		.bot-row{
			display:flex;
			align-items:center;
			height: 50upx;
			font-size: $font-sm;
			color: $font-color-light;
			text{
				flex: 1;
			}
		}
	}
	/* 分享 */
	.share-section{
		display:flex;
		align-items:center;
		color: $font-color-base;
		background: linear-gradient(left, #fdf5f6, #fbebf6);
		padding: 12upx 30upx;
		.share-icon{
			display:flex;
			align-items:center;
			width: 70upx;
			height: 30upx;
			line-height: 1;
			border: 1px solid $uni-color-primary;
			border-radius: 4upx;
			position:relative;
			overflow: hidden;
			font-size: 22upx;
			color: $uni-color-primary;
			&:after{
				content: '';
				width: 50upx;
				height: 50upx;
				border-radius: 50%;
				left: -20upx;
				top: -12upx;
				position:absolute;
				background: $uni-color-primary;
			}
		}
		.icon-xingxing{
			position:relative;
			z-index: 1;
			font-size: 24upx;
			margin-left: 2upx;
			margin-right: 10upx;
			color: #fff;
			line-height: 1;
		}
		.tit{
			font-size: $font-base;
			margin-left:10upx;
		}
		.icon-bangzhu1{
			padding: 10upx;
			font-size: 30upx;
			line-height: 1;
		}
		.share-btn{
			flex: 1;
			text-align:right;
			font-size: $font-sm;
			color: $uni-color-primary;
		}
		.icon-you{
			font-size: $font-sm;
			margin-left: 4upx;
			color: $uni-color-primary;
		}
	}
	
	.c-list{
		font-size: $font-sm + 2upx;
		color: $font-color-base;
		background: #fff;
		.c-row{
			display:flex;
			align-items:center;
			padding: 20upx 30upx;
			position:relative;
		}
		.tit{
			width: 140upx;
		}
		.con{
			flex: 1;
			color: $font-color-dark;
			.selected-text{
				margin-right: 10upx;
			}
		}
		.bz-list{
			height: 40upx;
			font-size: $font-sm+2upx;
			color: $font-color-dark;
			text{
				display: inline-block;
				margin-right: 30upx;
			}
		}
		.con-list{
			flex: 1;
			display:flex;
			flex-direction: column;
			color: $font-color-dark;
			line-height: 40upx;
		}
		.red{
			color: $uni-color-primary;
		}
	}
	
	/* 评价 */
	.eva-section{
		display: flex;
		flex-direction: column;
		padding: 20upx 30upx;
		background: #fff;
		margin-top: 16upx;
		.e-header{
			display: flex;
			align-items: center;
			height: 70upx;
			font-size: $font-sm + 2upx;
			color: $font-color-light;
			.tit{
				font-size: $font-base + 2upx;
				color: $font-color-dark;
				margin-right: 4upx;
			}
			.empty{
				
				flex: 1;
				/* width: 100upx; */
				text-align: right;
			}
			.tip{
				/* flex: 1; */
				/* width: 100upx; */
				text-align: right;
			}
			.icon-you{
				margin-left: 10upx;
			}
		}
	}
	.eva-box{
		display: flex;
		padding: 20upx 0;
		.portrait{
			flex-shrink: 0;
			width: 80upx;
			height: 80upx;
			border-radius: 100px;
		}
		.right{
			flex: 1;
			display: flex;
			flex-direction: column;
			font-size: $font-base;
			color: $font-color-base;
			padding-left: 26upx;
			.con{
				font-size: $font-base;
				color: $font-color-dark;
				padding: 20upx 0;
			}
			.bot{
				display: flex;
				justify-content: space-between;
				font-size: $font-sm;
				color:$font-color-light;
			}
		}
	}
	/*  详情 */
	.detail-desc{
		background: #fff;
		margin-top: 16upx;
		.d-header{
			display: flex;
			justify-content: center;
			align-items: center;
			height: 80upx;
			font-size: $font-base + 2upx;
			color: $font-color-dark;
			position: relative;
				
			text{
				padding: 0 20upx;
				background: #fff;
				position: relative;
				z-index: 1;
			}
			&:after{
				position: absolute;
				left: 50%;
				top: 50%;
				transform: translateX(-50%);
				width: 300upx;
				height: 0;
				content: '';
				border-bottom: 1px solid #ccc; 
			}
		}
	}
	
	/* 规格选择弹窗 */
	.attr-content{
		padding: 10upx 30upx;
		.a-t{
			display: flex;
			image{
				width: 170upx;
				height: 170upx;
				flex-shrink: 0;
				margin-top: -40upx;
				border-radius: 8upx;;
			}
			.right{
				display: flex;
				flex-direction: column;
				padding-left: 24upx;
				font-size: $font-sm + 2upx;
				color: $font-color-base;
				line-height: 42upx;
				.price{
					font-size: $font-lg;
					color: $uni-color-primary;
					margin-bottom: 10upx;
				}
				.selected-text{
					margin-right: 10upx;
				}
			}
		}
		.attr-list{
			display: flex;
			flex-direction: column;
			font-size: $font-base + 2upx;
			color: $font-color-base;
			padding-top: 30upx;
			padding-left: 10upx;
		}
		.item-list{
			padding: 20upx 0 0;
			display: flex;
			flex-wrap: wrap;
			text{
				display: flex;
				align-items: center;
				justify-content: center;
				background: #eee;
				margin-right: 20upx;
				margin-bottom: 20upx;
				border-radius: 100upx;
				min-width: 60upx;
				height: 60upx;
				padding: 0 20upx;
				font-size: $font-base;
				color: $font-color-dark;
			}
			.selected{
				background: #fbebee;
				color: $uni-color-primary;
			}
		}
	}
	
	/*  弹出层 */
	.popup {
		position: fixed;
		left: 0;
		top: 0;
		right: 0;
		bottom: 0;
		z-index: 99;
		
		&.show {
			display: block;
			.mask{
				animation: showPopup 0.2s linear both;
			}
			.layer {
				animation: showLayer 0.2s linear both;
			}
		}
		&.hide {
			.mask{
				animation: hidePopup 0.2s linear both;
			}
			.layer {
				animation: hideLayer 0.2s linear both;
			}
		}
		&.none {
			display: none;
		}
		.mask{
			position: fixed;
			top: 0;
			width: 100%;
			height: 100%;
			z-index: 1;
			background-color: rgba(0, 0, 0, 0.4);
		}
		.layer {
			position: fixed;
			z-index: 99;
			bottom: 0;
			width: 100%;
			min-height: 40vh;
			border-radius: 10upx 10upx 0 0;
			background-color: #fff;
			.btn{
				height: 66upx;
				line-height: 66upx;
				border-radius: 100upx;
				background: $uni-color-primary;
				font-size: $font-base + 2upx;
				color: #fff;
				margin: 30upx auto 20upx;
			}
		}
		@keyframes showPopup {
			0% {
				opacity: 0;
			}
			100% {
				opacity: 1;
			}
		}
		@keyframes hidePopup {
			0% {
				opacity: 1;
			}
			100% {
				opacity: 0;
			}
		}
		@keyframes showLayer {
			0% {
				transform: translateY(120%);
			}
			100% {
				transform: translateY(0%);
			}
		}
		@keyframes hideLayer {
			0% {
				transform: translateY(0);
			}
			100% {
				transform: translateY(120%);
			}
		}
	}
	
	/* 底部操作菜单 */
	.page-bottom{
		position:fixed;
		left: 30upx;
		bottom:30upx;
		z-index: 95;
		display: flex;
		justify-content: center;
		align-items: center;
		width: 690upx;
		height: 100upx;
		background: rgba(255,255,255,.9);
		box-shadow: 0 0 20upx 0 rgba(0,0,0,.5);
		border-radius: 16upx;
		
		.p-b-btn{
			display:flex;
			flex-direction: column;
			align-items: center;
			justify-content: center;
			font-size: $font-sm;
			color: $font-color-base;
			width: 96upx;
			height: 80upx;
			.yticon{
				font-size: 40upx;
				line-height: 48upx;
				color: $font-color-light;
			}
			&.active, &.active .yticon{
				color: $uni-color-primary;
			}
			.icon-fenxiang2{
				font-size: 42upx;
				transform: translateY(-2upx);
			}
			.icon-shoucang{
				font-size: 46upx;
			}
		}
		.action-btn-group{
			display: flex;
			height: 76upx;
			border-radius: 100px;
			overflow: hidden;
			box-shadow: 0 20upx 40upx -16upx #fa436a;
			box-shadow: 1px 2px 5px rgba(219, 63, 96, 0.4);
			background: linear-gradient(to right, #ffac30,#fa436a,#F56C6C);
			margin-left: 20upx;
			position:relative;
			&:after{
				content: '';
				position:absolute;
				top: 50%;
				right: 50%;
				transform: translateY(-50%);
				height: 28upx;
				width: 0;
				border-right: 1px solid rgba(255,255,255,.5);
			}
			.action-btn{
				display:flex;
				align-items: center;
				justify-content: center;
				width: 180upx;
				height: 100%;
				font-size: $font-base ;
				padding: 0;
				border-radius: 0;
				background: transparent;
			}
		}
	}
	
</style>
