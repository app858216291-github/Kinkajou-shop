<template>
	<view class="page">
		
		<view class="example">
			<view  v-for="(item,index) in products" :key="index">
				<view class="goods-box-single">
					<image class="goods-img" :src="item.mainImg" mode="aspectFill"></image>
					<view class="right">
						<text class="clamp title"> {{item.title}}</text>
						<text class="attr-box"> 属性：{{item.color}},{{item.size}}</text>
						<!-- <text class="attr-box">{{item.color}}</text> -->
						
					</view>
				</view>
			</view>
			<view class="example-title">客官，请给我们的服务打分！</view>
			<view class="example-body">
				描述：<uni-rate :value=describeRate @change="onChange1" />
			</view>
			<view class="example-body">
				物流：<uni-rate :value=logisticsRate @change="onChange2" />
			</view>
			<view class="example-body">
				服务：<uni-rate :value=serviceRate @change="onChange3" />
			</view>
		</view>

		<view class="example-title">评价内容：</view>
		<view class="uni-textarea content">
			<textarea class="contente" v-model="evaluate"  placeholder="例如:我对本次的购物体验非常好,下次还会再来."/>
		</view>
	
		<view class="button-sp-area">
			<button type="primary" class="btn" @click="submit" plain="true">提交</button>
		</view>
	</view>
</template>

<script>
	import uniRate from '@/components/uni-rate/uni-rate.vue'

	export default {
		components: {
			uniRate,
		},
		data() {
			return {
				describeRate:5,
				logisticsRate:5,
				serviceRate:5,
				evaluate:"",
				products:{},
				orderId:0,
				order:{}
			}
		},
		onLoad(options){
			
				console.info(options.orderid)
				this.orderId=options.orderid
				this.loadData()
		},
		methods: {
			async loadData(source){
				
				this.order=await this.$shop.getOrderList(this.$shop.prop().serviceUrl+'/order/orders?orderid='+this.orderId,{});
				this.products=this.order[0].products
				
				let a=3;
			},
			onChange1(e) {
				console.log('describeRate发生改变:' + JSON.stringify(e))
				let a2=JSON.stringify(e);
				this.describeRate=e.value;
			},
			onChange2(e) {
				console.log('logisticsRate发生改变:' + JSON.stringify(e))
				this.logisticsRate=e.value;
			},
			onChange3(e) {
				console.log('serviceRate发生改变:' + JSON.stringify(e))
				this.serviceRate=e.value;
			},
			submit(data) {
				
				let a=this.describeRate;
				let b=this.logisticsRate;
				let c=this.serviceRate;
				let d=this.evaluate;
				
				let param={
					"describeRate":this.describeRate,
					"logisticsRate":this.logisticsRate,
					"serviceRate":this.serviceRate,
					"evaluate":this.evaluate,
					"orderid":this.orderId
					
				}
				let e=this.$api.get(this.$shop.prop().serviceUrl+'/product/addRate',param)
				uni.reLaunch({
							url: '/pages/user/user'
						});
				// uni.navigateTo({  
				// 	url: `/pages/user/user`
				// }) 
				console.log('rate发生改变:' + JSON.stringify(e))
			}
		}
	}
</script>

<style>
	page {
		display: flex;
		flex-direction: column;
		box-sizing: border-box;
		background-color: #fff
	}
	
	

	view {
		font-size: 28upx;
		line-height: inherit
	}
	
	.goods-box-single{
		display: flex;
		padding: 20upx 0;
		
	}
	.goods-img{
		display: block;
		width: 120upx;
		height: 120upx;
	}
	.title{
		padding-top: 20upx;
		padding-left: 20upx;
		padding-bottom: 10upx;
		font-size: 40upx;
		color: $font-color-dark;
		line-height: 1;
	}
	.attr-box{
		font-size: $font-sm + 8upx;
		/* color: $font-color-light; */
		color: #777;
		padding: 10upx 12upx;
		/* padding-top: 20upx; */
		padding-left: 30upx;
	}
	.content{
		padding-left:30upx;
		
	}
	.contente{
		background-color:#eeeeee
	}

	.example {
		padding: 0 30upx 30upx
	}

	.example-title {
		font-size: 32upx;
		line-height: 32upx;
		color: #777;
		margin: 40upx 25upx;
		position: relative
	}

	.example .example-title {
		margin: 40upx 0
	}

	.example-body {
		padding: 0 40upx
	}	
	button {
		margin-top: 30upx;
		margin-bottom: 30upx;
		
	}
	.btn{
		background-color:#3d6ed3 !important;
		color: #ffffff !important;
	}

	.button-sp-area {
		margin: 0 auto;
		width: 60%;
	}
	.example-body {
		/* #ifndef APP-NVUE */
		display: flex;
		/* #endif */
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: center;
		padding: 0;
		font-size: 14px;
		background-color: #ffffff;
	}
	
	
	
</style>