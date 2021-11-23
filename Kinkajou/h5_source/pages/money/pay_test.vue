<template>
	<view class="app">
		<view class="price-box">
			<text>支付金额</text>
			<text class="price">{{mount}}</text>
		</view>

		<view style="text-align:center">
			<img style="width:400upx" :src=qrcode />
			<br>{{str1}}+<br>{{str2}}+<br>+{{str3}}++<br>{{link}}
			*长按识别二维码,完成支付
		</view>
		<view class="uni-btn-v uni-common-mt">
			
			<template>支付
				<button @click="callpay()">支付</button>
				<button @click="openidAndOrder()">获取openid并生成订单</button>
			</template>
			
		</view>

		<!-- <text class="mix-btn" @click="confirm">确认支付</text> -->
	</view>
</template>

<script>

	export default {
		data() {
			return {
				payType: 1,
				orderInfo: {},
				orderId:0,
				mount:0,
				qrcode:"",
				timer:"",
				str1:"str12",
				str2:"str22",
				str3:"str32",
				link:"",
				
				//------------
				title: 'request-payment',
				loading: false,
				price: 1,
				providerList: [],
				payParam:{},
				payInfo:{},
			};
		},
		computed: {
		
		},
		onLoad(options) {
			
			
			// alert(options);
			this.payInfo=options;
			this.link=window.location.href;
			this.str1=this.payInfo.toString();
			this.str2=JSON.stringify(this.payInfo);
			if(((this.link.split('?')).length-1)==2){
				let first=this.link.split('#')[0]
				let first_first=first.split('?')[1]
				let result=first.split('?')[0]+"#"+this.link.split('#')[1]+"&"+first_first
				alert(result)
				window.location.href=result;
			}
			//----------------------弹出支付----------------
			
		//--------------------------弹出支付---end----------------------
			
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
			async openidAndOrder(){
				
				if(this.payInfo.getInfo!="yes"){
					let a=await this.$api.get(this.$shop.prop().serviceUrl+'/common/payjs',{})
					
					// alert(a);
					window.location.href = a;
					// let b=await this.$api.get(a,{})
					// this.payParam=b.data;
				}else{
					let b=await this.$api.get(this.$shop.prop().serviceUrl+'/common/payjs',this.payInfo)
					
					alert(b);
					this.payParam = b;
					this.str1=JSON.stringify(this.payParam);
					this.str2=JSON.stringify(this.payParam.data)
					this.str3=JSON.stringify(this.payParam.data.timeStamp)
					// this.payParam=this.payParam.data;
					// this.payParam=b.data;
					// alert(tpyeof this.payParam);
					// alert("00")
					// alert(this.payParam);
					// alert("1");
					// var str = JSON.stringify(this.payParam);
					// this.payParam = JSON.parse(this.payParam);
					// alert(this.payParams.timeStamp);
					alert("2");
				}
				
				
				
				// alert(this.payParam.appid);
			},
			callpay() {
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
			  }
			//-------------弹出支付---end-------------------
			
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
