<template>
	<view class="content">
		<view class="row b-b">
			<text class="tit">订单号：</text>
			<text >{{orderNo}}</text>
		</view>
		<view class="row b-b">
			<text class="tit">产品：</text>
			<text>{{orderName}}</text>
		</view>
		<view class="row b-b">
			<text class="tit">金额</text>
			<!--选择弹出地图 <text @click="chooseLocation" class="input">
				{{addressData.address}}{{addressData.addressName}}
			</text> -->
			<text>{{orderMount}}元</text>
			
		</view>
		<view class="row b-b"> 
			<text >支付时间：</text>
			<text>{{orderTime}}</text>
		</view>
		<view class="row b-b">
			<text >售后类型：</text>
			<picker @change="examinationType" :range="examinationTypeArray">
			              
			              <label class="">{{ examinationTypeArrayType }}</label>
			</picker>
		</view>
	
		<view class="row b-b">
			<text >售后描述：</text>
		</view>
		<view class="uni-textarea content" style="padding-left:25px">
			<textarea class="contente" v-model="desc" placeholder="填写售后原因,如:七天无理由"/>
		</view>
		<view class="row b-b" v-if="needhelp==1">
			<text >处理结果：</text>
			<text v-model="replay">已退款</text>
		</view>
		
		
		<button v-if="operate=='apply'" class="add-btn" @click="confirm">提交</button>
		<button v-if="operate=='cancel'" class="add-btn" @click="cancel">撤销</button>
		
	</view>
</template>

<script>
	import pickerAddress from '@/components/pickerAddress/pickerAddress.vue'
	export default {
		components:{
		            pickerAddress
		        },
		data() {
			return {
				needhelp:0,
				orderid:0,
				orderNo:'',
				orderTime:'',
				orderName:'',
				orderMount:0,
				replay: '',
				desc:'',
				examinationTypeArray:['---请选择---','仅退款','退款退货','投诉'],
				examinationTypeIndex:0,
				examinationTypeArrayType:'---请选择---',
				operate:'apply',
				
			}
		},
		async onLoad(option){
			let title = '售后申请查看';
			if(option.type==='edit'){
				title = '售后申请'
			}
			this.operate=option.operate;
			this.orderid=option.orderid;
			let orders=await this.$shop.getOrderList(this.$shop.prop().serviceUrl+'/order/orders?orderid='+this.orderid,{});
			let order=orders[0]
			this.orderNo=order.orderNo;
			this.orderTime=order.create_time;
		
			this.orderName=order.products[0].title;
			this.orderMount=order.mount;
			this.needhelp=order.needHelp;
			
			uni.setNavigationBarTitle({
				title
			})
		},
		methods: {
			examinationType(e) {
			    this.examinationTypeIndex = e.target.value;
			    this.examinationTypeArrayType=this.examinationTypeArray[this.examinationTypeIndex]
			   },
		   async cancel(){
			   let datatem=await this.$api.get(this.$shop.prop().serviceUrl+'/order/cancelHelp?orderid='+this.orderid,{});
			   setTimeout(()=>{
			   	uni.navigateBack()
			   }, 800)
			  },

			
			
			//提交
			async confirm(){
				
				let examinationTypeArrayType=this.examinationTypeArrayType;
				let desc=this.desc;
				
				if(!examinationTypeArrayType=='---请选择---'){
					this.$api.msg('请选择售后类型');
					return;
				}
				if(desc==''){
					this.$api.msg('请输入售后描述');
					return;
				}
				
				let data={
					'orderid':this.orderid,
					'type':this.examinationTypeArrayType,
					'desc':this.desc
				}
				let datatem=await this.$api.get(this.$shop.prop().serviceUrl+'/order/needhelp',data)
				
				// uni.request({  
				// 	url: this.$shop.prop().serviceUrl+'/user/addAddress',  
				// 	data: data,
				// 	success: (result) => {
				// 		this.$api.msg("地址添加成功") 
				// 	},  
				// 	fail: (e) => {  
				// 		this.$api.msg("地址添加失败")  
				// 	}  
				// })
				//this.$api.prePage()获取上一页实例，可直接调用上页所有数据和方法，在App.vue定义
				
				// this.$api.prePage().onLoad({});
				//this.$api.msg(`售后${this.manageType=='edit' ? '添加': '申请'}成功`);
				setTimeout(()=>{
					uni.navigateBack()
				}, 800)
			},
		}
	}
</script>

<style lang="scss">
	page{
		background: $page-color-base;
		padding-top: 16upx;
	}

	.row{
		display: flex;
		align-items: center;
		position: relative;
		padding:0 30upx;
		height: 110upx;
		background: #fff;
		
		.tit{
			flex-shrink: 0;
			width: 120upx;
			font-size: 30upx;
			color: $font-color-dark;
		}
		.input{
			flex: 1;
			font-size: 30upx;
			color: $font-color-dark;
		}
		.icon-shouhuodizhi{
			font-size: 36upx;
			color: $font-color-light;
		}
	}
	.default-row{
		margin-top: 16upx;
		.tit{
			flex: 1;
		}
		switch{
			transform: translateX(16upx) scale(.9);
		}
	}
	.add-btn{
		display: flex;
		align-items: center;
		justify-content: center;
		width: 690upx;
		height: 80upx;
		margin: 60upx auto;
		font-size: $font-lg;
		color: #fff;
		background-color: $base-color;
		border-radius: 10upx;
		box-shadow: 1px 2px 5px rgba(219, 63, 96, 0.4);
	}
</style>
