<template>
	<view class="content">
		<view class="row b-b">
			<text class="tit">联系人</text>
			<input class="input" type="text" v-model="addressData.receiver" placeholder="收货人姓名" placeholder-class="placeholder" />
		</view>
		<view class="row b-b">
			<text class="tit">手机号</text>
			<input class="input" type="number" v-model="addressData.mobile" placeholder="收货人手机号码" placeholder-class="placeholder" />
		</view>
		<view class="row b-b">
			<text class="tit">地址</text>
			<!--选择弹出地图 <text @click="chooseLocation" class="input">
				{{addressData.address}}{{addressData.addressName}}
			</text> -->
			<pickerAddress class="city" @change="change"><text class="input" placeholder="请选择收货地址">
				{{addressData.address}}
			</text>
			<text class="yticon icon-shouhuodizhi"></text></pickerAddress>
		</view>
		<view class="row b-b"> 
			<text class="tit">门牌号</text>
			<input class="input" type="text" v-model="addressData.area" placeholder="楼号、门牌" placeholder-class="placeholder" />
		</view>
		
		<view class="row default-row">
			
			<text class="tit">设为默认</text>
			<switch :checked="addressData.defaule" color="#fa436a" @change="switchChange" />
		</view>
		<button class="add-btn" @click="confirm">提交</button>
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
				city: '请选择收货地址',
				addressData: {
					receiver: '',
					mobile: '',
					addressName: '在地图选择',
					address: '点击选择收货地址',
					area: '',
					default: false,
					city: '请选择收货地址',
					title: 'Hello'
				}
			}
		},
		onLoad(option){
			
			
			// let a=this.addressData.city
			let title = '新增收货地址';
			if(option.type==='edit'){
				title = '编辑收货地址'
				
				this.addressData = JSON.parse(option.data)
			}
			this.manageType = option.type;
			uni.setNavigationBarTitle({
				title
			})
		},
		methods: {
			change(data) {
					this.city = data.data.join('')
					this.addressData.address=data.data.join('');
					console.log(data.data.join(''))
					console.log(this.addressData.address);	
			            },
			switchChange(e){
				this.addressData.default = e.detail.value;
				
			},
			
			//地图选择地址
			chooseLocation(){
				uni.chooseLocation({
					success: (data)=> {
						
						this.addressData.addressName = data.name;
						this.addressData.address = data.address;
					}
				})
			},
			
			//提交
			async confirm(){
				let data = this.addressData;
				if(!data.receiver){
					this.$api.msg('请填写收货人姓名');
					return;
				}
				if(!/(^1[3|4|5|7|8|9][0-9]{9}$)/.test(data.mobile)){
					this.$api.msg('请输入正确的手机号码');
					return;
				}
				if(!data.address){
					this.$api.msg('请在地图选择所在位置');
					return;
				}
				if(!data.area){
					this.$api.msg('请填写门牌号信息');
					return;
				}
				
				
				let datatem=await this.$api.get(this.$shop.prop().serviceUrl+'/user/addAddress',data)
				if(datatem.code==1){
					data.id=datatem.data.id
				}else{
					alert("地址添加失败");
				}
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
				this.$api.prePage().refreshList(data, this.manageType);
				// this.$api.prePage().onLoad({});
				this.$api.msg(`地址${this.manageType=='edit' ? '修改': '添加'}成功`);
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
