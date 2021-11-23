<template>
	<!-- <view> -->
	<view class="container">
		<view v-if="isempty || empty===true" class="empty">
			<image src="/static/emptyCart.jpg" mode="aspectFit"></image>
			<view class="empty-tips">
				该宝贝还没有评价，您可以
				<view class="navigator" @click="navToLogin">先下单抢一楼></view>
			</view>
			
		</view>
		<view class="uni-padding-wrap"  >
			
			<!-- 评论区 start -->
			<view class="uni-comment"  v-for="(item, index) in rateList" :key="index">
				<view class="uni-comment-list">
					<view class="uni-comment-face"><image src="https://img-cdn-qiniu.dcloud.net.cn/uniapp/images/uni@2x.png" mode="widthFix"></image></view>
					<view class="uni-comment-body">
						<view class="uni-comment-top">
							<text>{{item.nickname}}</text>
						</view>
						<view class="uni-comment-content">{{item.evaluate}}</view>
						<view class="uni-comment-date">
							<text>08/10 08:12</text>
						</view>
					</view>
				</view>
			
				<!-- <view class="uni-comment-list">
					<view class="uni-comment-face"><image src="https://img-cdn-qiniu.dcloud.net.cn/uniapp/images/uni@2x.png" mode="widthFix"></image></view>
					<view class="uni-comment-body">
						<view class="uni-comment-top">
							<text>网友</text>
						</view>
						<view class="uni-comment-date">
							<text>08/10 08:12</text>
						</view>
						<view class="uni-comment-content">很酷的HBuilderX和uni-app，开发一次既能生成小程序，又能生成App</view>
					</view>
				</view>
				<view class="uni-comment-list">
					<view class="uni-comment-face"><image src="https://img-cdn-qiniu.dcloud.net.cn/uniapp/images/uni@2x.png" mode="widthFix"></image></view>
					<view class="uni-comment-body">
						<view class="uni-comment-top">
							<text>马克一天</text>
						</view>
						<view class="uni-comment-content">很强大，厉害了我的uni-app!</view>
					</view>
				</view>
				<view class="uni-comment-list">
					<view class="uni-comment-face"><image src="https://img-cdn-qiniu.dcloud.net.cn/uniapp/images/uni@2x.png" mode="widthFix"></image></view>
					<view class="uni-comment-body">
						<view class="uni-comment-top">
							<text>今生缘</text>
						</view>
						<view class="uni-comment-content">好牛逼的感觉，是不是小程序、App、移动端都互通了？</view>
						<view class="uni-comment-date">
							<text>08/10 07:55</text>
						</view>
					</view>
				</view>
				<view class="uni-comment-list">
					<view class="uni-comment-face"><image src="https://img-cdn-qiniu.dcloud.net.cn/uniapp/images/uni@2x.png" mode="widthFix"></image></view>
					<view class="uni-comment-body">
						<view class="uni-comment-top">
							<text>小猫咪</text>
						</view>
						<view class="uni-comment-content">支持国产，支持DCloud!</view>
						<view class="uni-comment-date">
							<view>2天前</view><view class="uni-comment-replay-btn">5回复</view>
						</view>
					</view>
				</view>
				<view class="uni-comment-list">
					<view class="uni-comment-face"><image src="https://img-cdn-qiniu.dcloud.net.cn/uniapp/images/uni@2x.png" mode="widthFix"></image></view>
					<view class="uni-comment-body">
						<view class="uni-comment-top">
							<text>兰花爱好者</text>
						</view>
						<view class="uni-comment-content">花很好</view>
						<view class="uni-comment-date">
							<text>08/10 08:12</text>
						</view>
					</view>
				</view> -->
			</view>
			<!-- 评论区 end -->
			
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			title:"评论界面",
			rateList:[],
			isempty:false,
			productid:0,
		}
	},
	async onLoad(options){
		//接收传值,id里面放的是标题，因为测试数据并没写id 
		this.productid = options.productid;
		let rates=await this.$api.get(this.$shop.prop().serviceUrl+'/product/rateList?productid='+this.productid,{})
		this.rateList=rates.data
		if (this.rateList.length==0){
			this.isempty=true;
		}
		
		let a="22";
		
		},
		methods: {
			navToLogin(){
				// alert("a")
				let id=this.productid;
				uni.navigateTo({
					url: `/pages/product/product?id=${id}`
				})
				
			}
			
		},
		
		
}
</script>

<style lang='scss'>
	
.container{
		padding-bottom: 134upx;
		/* 空白页 */
		.empty{
			position:fixed;
			left: 0;
			top:0;
			width: 100%;
			height: 100vh;
			padding-bottom:100upx;
			display:flex;
			justify-content: center;
			flex-direction: column;
			align-items:center;
			background: #fff;
			image{
				width: 240upx;
				height: 160upx;
				margin-bottom:30upx;
			}
			.empty-tips{
				display:flex;
				font-size: $font-sm+2upx;
				color: $font-color-disabled;
				.navigator{
					color: $uni-color-primary;
					margin-left: 16upx;
				}
			}
			
		}
		
	}
</style>
