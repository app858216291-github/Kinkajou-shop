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
				providerList: []
			};
		},
		computed: {
		
		},
		onLoad(options) {
			
			// uni.setStorage({
			// key:"openid",
			// data:"oUrkV1R5f_Snab1jSmD7cYqhYQ3g"
			// })
			
			
			
			this.orderNo=options.orderNo
			this.mount=options.total
			if(options.total==undefined){
				this.mount=options.mount
			}
			this.orderId=options.orderid
		
		},

		methods: {
			
			
			//---------弹出支付---------------
			onBridgeReady() {
				
				// alert(this.payParam.timeStamp);
				// alert("支付0!");
				
				WeixinJSBridge.invoke(
				  'getBrandWCPayRequest',
				  {
					appId: this.payParam.data.appid,    //公众号名称，由商户传入
					timeStamp: this.payParam.data.timeStamp, //时间戳，自1970年以来的秒数
					nonceStr: this.payParam.data.nonceStr, //随机串
					package: "prepay_id="+this.payParam.data.prepay_id, //预支付id
					signType: "MD5", //微信签名方式
					paySign: this.payParam.data.sign   //微信签名
				  },
				  function (res) {
					//支付成功后返回 get_brand_wcpay_request:ok
					if (res.err_msg == "get_brand_wcpay_request:ok") {
					  // 跳转到支付成功的页面
					  alert("支付成功")
					  uni.redirectTo({
					  	url: '/pages/money/paySuccess'
					  })
					  
					} else if (res.err_msg == "get_brand_wcpay_request:cancel") {
					  alert("您已取消支付!");
					
					} else if (res.err_msg == "get_brand_wcpay_request:fail") {
					  $.each(res, function(key,value){
						// alert(value);
						});
					  alert("支付失败!");
					}
				  }
				);
			  },
			async openidAndOrder(){
				let _self=this;
				//这是临时支付方式，后续用微信支付宝支付请注解掉这些代码
				//---------------------------------------
				
				uni.showModal({
				    title: '提示',
				    content: '是否支付？',
				    success: function (res) {
				        if (res.confirm) {
				            console.log('用户点击确定');
							_self.$api.get(_self.$shop.prop().serviceUrl+"/order/pay?orderId="+_self.orderId,{});
							uni.redirectTo({
								url: '/pages/money/paySuccess?message=支付成功'
							})
							return true;
				        } else if (res.cancel) {
				            console.log('用户点击取消');
							uni.redirectTo({
								url: '/pages/money/paySuccess?message=支付失败'
							})
							return true;
				        }
				    }
				});
				return true;
				
				
				//------------------------------------------------
			
				this.openid_yuhui = await this.$api.get(this.$shop.prop().serviceUrl+"/common/pay/getOpenid/",{});

				/**uni.getStorage({
				key:"openid",
				success(e){
					// alert("openid="+e.data);
					if(e.data==undefined ||e.data=="undefined"||e.data.length<6 ){
						let url=window.location.href;
						let type="openid"
						uni.redirectTo({
							url: `../../pages/public/proxy?url=${url}&type=${type}`
						})
					}else{
						_self.openid=e.data;
					}
					
				},
				fail(e){
					
					alert("没有openid")
					let url=window.location.href;
					let type="openid"
					uni.redirectTo({
						// url: `../../pages/public/proxy?url=${url}&type=${type}`
						url:`http://127.0.0.1:5000/common/payjs2`
					})
				}
				})**/
				this.payParam=await _self.$api.get(_self.$shop.prop().serviceUrl+'/common/payjs?openid='+this.openid_yuhui+"&attach="+this.orderNo,{});
				// alert(JSON.stringify(this.payParam));
				
				// this.payParam=this.payParam.data;
				/**if(this.payParam.code==-1){
					uni.removeStorage({
					    key: 'openid',
					    success: function (res) {
							alert("成功删除openid")
					        console.log('success');
					    }
					});
				}
				**/
				

			},
			callpay() {
				this.openidAndOrder();
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
			
			//确认支付
			confirm: async function() {
				
				
				
				
				
				let data={"orderId":this.orderId}
				uni.request({  
					url: this.$shop.prop().serviceUrl+'/order/pay',  
					data: data,  
					success: (result) => {
						uni.$api.msg("支付成功") 
					},  
					fail: (e) => {  
						uni.$api.msg("支付失败")  
					}  
				})
				uni.redirectTo({
					url: '/pages/money/paySuccess'
				})
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
