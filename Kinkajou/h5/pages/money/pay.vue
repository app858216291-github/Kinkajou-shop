<template>
	<view class="app">
		<view class="price-box">
			<text>支付金额</text>
			<text class="price">{{mount}}</text>
		</view>

		<view class="pay-type-list">

			<view class="type-item b-b" @click="changePayType(1)">
				
				<view class="con" style="flex-direction:row; justify-content:center;display:flex;width: 50%;">
					<text class="icon yticon icon-weixinzhifu"></text><text class="tit" style="padding-top:5px">微信支付</text>
					<!-- <view style="flex-direction:row; justify-content:center;display:flex;"><text>推荐使用微信支付</text></view> -->
				</view>
			</view>
			
		</view>
		
		<view class="uni-btn-v uni-common-mt"  style="flex-direction:row; justify-content:center;display:flex;">
			
			<button style="width: 50%; background-color: #00aa00; color: #FFFFFF;" @click="callpay()">点击支付</button>
		</view>

		<!-- <text class="mix-btn" @click="confirm">确认支付</text> -->
	</view>
</template>

<script>
	// #ifdef H5
	var wx = require('@/components/weixin/index.js');
	// #endif
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
			let _self=this
			// #ifdef MP
			//小程序的代码写这里
			uni.login({
			  provider: 'weixin',
			  success: function (res) {
				 uni.request({
				 	url: _self.$shop.prop().serviceUrl+"/wx/mpOpenId?code="+res.code,
				 	success: (result) => {
				 		
				 		res=result.data.data;
						debugger
						_self.openid=res
				 		console.info(_self.openid);
				 		 _self.orderNo=options.orderNo
				 		 _self.mount=options.total
				 		 if(options.total==undefined){
				 		 	_self.mount=options.mount
				 		 }
				 		 _self.orderId=options.orderid
				 		 
				 		 _self.timer= setInterval( () => {
				 		 	console.info("查询是否已支付")
				 		 	let url=_self.$shop.prop().serviceUrl+'/common/model/queryById/?id='+_self.orderId+'&modelName=Order';
				 		 	
				 		 	uni.request({
				 		 		url:url ,  
				 		 		data: {}, 
				 		 		success: (result) => {  
				 		 			
				 		 			if(result.data.data.orderStatus==2){
				 		 				clearInterval(_self.timer);
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
				 		
				 		}
				 		
				 	}) 
			    
			  }
			});
			
			
			// #endif
			
			// #ifdef H5
			let isLogin=this.$api.login_openid();
			if (!isLogin){
				let redirect_url=await this.$api.get(this.$shop.prop().serviceUrl+'/common/getOpenidUrl',{})
				
				window.location.href=redirect_url;
				
			}
			
			this.orderNo=options.orderNo
			this.mount=options.total
			if(options.total==undefined){
				this.mount=options.mount
			}
			this.orderId=options.orderid
			
			this.timer= setInterval( () => {
				console.info("查询是否已支付")
				let url=this.$shop.prop().serviceUrl+'/common/model/queryById/?id='+this.orderId+'&modelName=Order';
				
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
			// #endif
		
		},

		methods: {
			// #ifdef MP
			async callpay() {
				
				
				let _self=this;
				let k=_self.openid;
				debugger
				//支付参数
				uni.request({
					
					url: _self.$shop.prop().serviceUrl+"/common/payjs_mp?openid="+_self.openid+"&orderNo="+_self.orderNo,
					success: (result) => {
						
						
						var payParam=result.data.data;
						
						// wx.requestPayment({
						// 			  appId: "wx404f3e7d6839135e",
						//               timeStamp: "1625068015",
						//               nonceStr: "JGn8Q3Qd4keZjuUu",
						//               package: "prepay_id=wx3023465493110999e74910afe12bcb0000",
						//               signType: 'MD5',
						//               paySign: "6451FEE2FAD6F3A6EADDB21630C920A1",
						// 			  "fail":function(res){
						// 				  debugger
						// 				  console.info(res)
						// 			  },
						//             });
						
						//支付验证签名失败，可参考https://pay.weixin.qq.com/wiki/doc/api/micropay.php?chapter=20_1 ，自己拼接获取加密串
						wx.requestPayment({
									  appId: payParam.appid,
						              timeStamp: payParam.timeStamp,
						              nonceStr: payParam.nonceStr,
						              package: payParam.package,
						              signType: 'MD5',
						              paySign: payParam.sign,
									  "fail":function(res){
										  debugger
										  console.info(res)
									  },
						            });
						          
					
					}	 
				}) 
			}
			
			
			//#endif
			// #ifdef H5
		onBridgeReady() {
		
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
			// #endif
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
