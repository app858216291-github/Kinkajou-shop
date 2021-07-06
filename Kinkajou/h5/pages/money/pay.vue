<template>
	<view class="app">
		<view class="price-box">
			<text>支付金额</text>
			<text class="price">{{mount}}</text>
		</view>

		<view class="pay-type-list">

			<view class="type-item b-b" @click="changePayType(1)">
				<text class="icon yticon icon-weixinzhifu"></text>
				<view class="con">
					<text class="tit">微信支付</text>
					<text>推荐使用微信支付</text>
				</view>
			</view>
			
		</view>
		
		<view class="uni-btn-v uni-common-mt">
			
			<center><button style="width: 50%; background-color: #00aa00; color: #FFFFFF;" @click="callpay()">点击支付</button></center>
		</view>

		<!-- <text class="mix-btn" @click="confirm">确认支付</text> -->
	</view>
</template>

<script>
	var wx = require('@/components/weixin/index.js');
	export default {
		data() {
			return {
				payParam: {},
				openid:"",
				openid_yuhui:"",
				
				//------------
				title: 'request-payment',
				loading: false,
				price: 1,
				timer:{},
				providerList: [],
			};
		},
		computed: {
		
		},
		async onLoad(options) {
			
			let isLogin=this.$api.login_openid();
			if (!isLogin){
				let redirect_url=await this.$api.get(this.$shop.prop().serviceUrl+'/common/getOpenidUrl',{})
				window.location.href=redirect_url;
			}
			
			// uni.setStorage({
			// key:"openid",
			// data:"oUrkV1R5f_Snab1jSmD7cYqhYQ3g"
			// })
			// var payParam2={}
			
			//---if里面的为支付功能
		// 	if(options.openid!=undefined)
		// 	{
		// 		this.openid=options.openid;
		// 		this.orderNo=options.orderNo;
		// 		this.mount=options.total;
		// 		this.orderId=options.orderid
		// 		this.payParam=await this.$api.get(this.$shop.prop().serviceUrl+'/common/payjs?openid='+this.openid+"&orderNo="+this.orderNo,{});

		// 		// let kk=wx.chooseWXPay;
		// 		wx.chooseWXPay({
		// 		  timestamp: this.payParam.timeStamp, // 支付签名时间戳，注意微信jssdk中的所有使用timestamp字段均为小写。但最新版的支付后台生成签名使用的timeStamp字段名需大写其中的S字符
		// 		  nonceStr: this.payParam.nonceStr, // 支付签名随机串，不长于 32 位
		// 		  package: this.payParam.prepay_id, // 统一支付接口返回的prepay_id参数值，提交格式如：prepay_id=\*\*\*）
		// 		  signType: 'MD5', // 签名方式，默认为'SHA1'，使用新版支付需传入'MD5'
		// 		  paySign: this.payParam.sign, // 支付签名
		// 		  success: function (res) {
		// 			console.info("支付成功")
		// 			uni.redirectTo({
		// 				url: '/pages/money/paySuccess?message=支付成功'
		// 			})
		// 		  },
		// 		  // 支付取消回调函数
		// 		  cencel: function (res) {
		// 			uni.redirectTo({
		// 				url: '/pages/money/paySuccess?message=支付失败'
		// 			})
		// 		  },
		// 		  // 支付失败回调函数
		// 		  fail: function (res) {
		// 			uni.redirectTo({
		// 				url: '/pages/money/paySuccess?message=支付失败'
		// 			})
		// 		  }
		
		// 		});
				
		// 		// if (typeof WeixinJSBridge == "undefined") {
		// 		//   if (document.addEventListener) {
		// 		// 	document.addEventListener('WeixinJSBridgeReady', this.onBridgeReady, false);
		// 		//   } else if (document.attachEvent) {
					 
		// 		// 	document.attachEvent('WeixinJSBridgeReady', this.onBridgeReady);
		// 		// 	document.attachEvent('onWeixinJSBridgeReady', this.onBridgeReady);
		// 		//   }
		// 		// } else {
		// 		//   this.onBridgeReady();
		// 		// }
				
				
				
		// 		return
		// 	}
			
			this.orderNo=options.orderNo
			this.mount=options.total
			if(options.total==undefined){
				this.mount=options.mount
			}
			this.orderId=options.orderid
			
			this.timer= setInterval( () => {
				console.info("查询是否已支付")
				let url=this.$shop.prop().serviceUrl+'/common/model/queryById/?id='+this.orderId+'&modelName=Order';
				debugger
				uni.request({
					url:url ,  
					data: {}, 
					success: (result) => {  
						
						if(result.data.data.orderStatus==2){
							clearInterval(this.timer);
							uni.redirectTo({
									url: '/pages/money/paySuccess?message=支付成功'
								})
						}
					},  
					fail: (e) => {  
						console.info("系统异常")
						uni.redirectTo({
								url: '/pages/money/paySuccess?message=支付失败'
							})
						
						
					}  
				})
				
			}, 1000)
		
		},

		methods: {
		onBridgeReady() {
			// alert(this.payParam.timeStamp);
			// alert("支付0!");
		
			WeixinJSBridge.invoke(
			  'getBrandWCPayRequest',
			  {
				appId: this.payParam.appid,    //公众号名称，由商户传入
				timeStamp: this.payParam.timeStamp, //时间戳，自1970年以来的秒数
				nonceStr: this.payParam.nonceStr, //随机串
				package: "prepay_id="+this.payParam.prepay_id, //预支付id
				signType: "MD5", //微信签名方式
				paySign: this.payParam.sign   //微信签名
			  },
			  function (res) {
				//支付成功后返回 get_brand_wcpay_request:ok
				if (res.err_msg == "get_brand_wcpay_request:ok") {
				  // 跳转到支付成功的页面
				  
				} else if (res.err_msg == "get_brand_wcpay_request:cancel") {
				  alert("您已取消支付!");
				
				} else if (res.err_msg == "get_brand_wcpay_request:fail") {
				  $.each(res, function(key,value){
					alert(value);
					});
				  alert("支付失败!");
				}
			  }
			);
		  },
			async callpay() {
				let user=uni.getStorageSync('userInfo');
				this.openid=user.openid
				let param={"orderNo":this.orderNo,"orderid":this.orderId,"mount":this.mount}
				this.payParam=await this.$api.get(this.$shop.prop().serviceUrl+'/common/payjs?openid='+this.openid+"&orderNo="+this.orderNo,{});
				
				this.payParam=this.payParam.data;
				
				// let kk=wx.chooseWXPay;
				// wx.chooseWXPay({
				//   appId: this.payParam.appid,
				//   timestamp: this.payParam.timeStamp, // 支付签名时间戳，注意微信jssdk中的所有使用timestamp字段均为小写。但最新版的支付后台生成签名使用的timeStamp字段名需大写其中的S字符
				//   nonceStr: this.payParam.nonceStr, // 支付签名随机串，不长于 32 位
				//   package: this.payParam.prepay_id, // 统一支付接口返回的prepay_id参数值，提交格式如：prepay_id=\*\*\*）
				//   signType: 'MD5', // 签名方式，默认为'SHA1'，使用新版支付需传入'MD5'
				//   paySign: this.payParam.sign, // 支付签名
				//   success: function (res) {
				// 	console.info("支付成功")
				// 	uni.redirectTo({
				// 		url: '/pages/money/paySuccess?message=支付成功'
				// 	})
				//   },
				//   // 支付取消回调函数
				//   cencel: function (res) {
				// 	uni.redirectTo({
				// 		url: '/pages/money/paySuccess?message=支付失败'
				// 	})
				//   },
				//   // 支付失败回调函数
				//   fail: function (res) {
				// 	uni.redirectTo({
				// 		url: '/pages/money/paySuccess?message=支付失败'
				// 	})
				//   },
				//  })

			 //  },
			 if (typeof WeixinJSBridge == "undefined") {
			 
			   if (document.addEventListener) {
			 	 
			 	document.addEventListener('WeixinJSBridgeReady', this.onBridgeReady, false);
			   } else if (document.attachEvent) {
			 	 
			 	document.attachEvent('WeixinJSBridgeReady', this.onBridgeReady);
			 	document.attachEvent('onWeixinJSBridgeReady', this.onBridgeReady);
			   }
			 } else {
			 	
			   this.onBridgeReady();
			 }
			 },
			 
			 
			//-------------弹出支付---end-------------------
	
			//选择支付方式
			changePayType(type) {
				this.payType = type;
			},

		}
	}
</script>

<style lang='scss'>
	.app {
		width: 100%;
	}

	.price-box {
		background-color: #fff;
		height: 265upx;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		font-size: 28upx;
		color: #909399;

		.price{
			font-size: 50upx;
			color: #303133;
			margin-top: 12upx;
			&:before{
				content: '￥';
				font-size: 40upx;
			}
		}
	}

	.pay-type-list {
		margin-top: 20upx;
		background-color: #fff;
		padding-left: 60upx;
		
		.type-item{
			height: 120upx;
			padding: 20upx 0;
			display: flex;
			justify-content: space-between;
			align-items: center;
			padding-right: 60upx;
			font-size: 30upx;
			position:relative;
		}
		
		.icon{
			width: 100upx;
			font-size: 52upx;
		}
		.icon-erjiye-yucunkuan {
			color: #fe8e2e;
		}
		.icon-weixinzhifu {
			color: #36cb59;
		}
		.icon-alipay {
			color: #01aaef;
		}
		.tit{
			font-size: $font-lg;
			color: $font-color-dark;
			margin-bottom: 4upx;
		}
		.con{
			flex: 1;
			display: flex;
			flex-direction: column;
			font-size: $font-sm;
			color: $font-color-light;
		}
	}
	.mix-btn {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 630upx;
		height: 80upx;
		margin: 80upx auto 30upx;
		font-size: $font-lg;
		color: #fff;
		background-color: $base-color;
		border-radius: 10upx;
		box-shadow: 1px 2px 5px rgba(219, 63, 96, 0.4);
	}

</style>
