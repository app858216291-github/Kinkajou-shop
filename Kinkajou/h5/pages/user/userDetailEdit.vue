<template>
	<view class="content">
		<view class="row b-b">
			<text class="tit">昵称</text>
			<input class="input" type="text" v-model="nickname" placeholder="昵称" placeholder-class="placeholder" />
		</view>
		<view class="row b-b">
			<text class="tit">年龄</text>
			<input class="input" type="number" v-model="age" placeholder="25岁请输入:25" placeholder-class="placeholder" />
		</view>
		<view class="row b-b">
			<text class="tit">姓名</text>
			<input class="input" type="text" v-model="name" placeholder=" 陈先生" placeholder-class="placeholder" />
		</view>
		<view class="row b-b">
			<text class="tit">手机号</text>
			<input class="input" type="text" v-model="mobile" placeholder="收货人手机号码" placeholder-class="placeholder" />
		</view>
		
		<button class="add-btn" @click="confirm">提交</button>
	</view>
</template>

<script>
	import {
		mapState,
		mapMutations
	} from 'vuex';
	export default {
		
		data() {
			return {
				mobile:"",
				nickname:"",
				name:"",
				age:"",
				user:{},
				manageType:'edit'
			}
		},
		computed:{
			...mapState(['userInfo']),
			...mapState(['hasLogin'])
		},
		 async onLoad(option){
			let result=await this.$api.get(this.$shop.prop().serviceUrl+'/user/getUser',"");
			let kk=this.userInfo
			this.name=result.data.name
			this.nickname=result.data.nickname
			this.mobile=result.data.mobile
			this.age=result.data.age
			
			this.user.name="陈先生"
			this.user.nickname=this.userInfo.nickname
			this.user.mobile=this.userInfo.mobile
			this.user.age=this.userInfo.age
			
			
		},
		// watch: {
		// 			mobile(newValue, oldValue) {
		// 				console.log("mobile",newValue,oldValue)
		// 			},
					
		// 		},
		methods: {
			...mapMutations(['login']),
			//提交
			async confirm(){
				let data = {};
				// this.user.mobile="asdg222"
				debugger
				if(!this.nickname){
					this.$api.msg('请填写昵称');
					return;
				}
				if(!/(^1[3|4|5|7|8|9][0-9]{9}$)/.test(this.mobile)){
					this.$api.msg('请输入正确的手机号码');
					return;
				}
				
				if(!this.name){
					this.$api.msg('请填写真实姓名');
					return;
				}
				if(!this.age){
					this.$api.msg('请填写真实年龄');
					return;
				}
				data.nickname=this.nickname
				data.mobile=this.mobile
				data.name=this.name
				data.age=this.age
				let result=await this.$api.get(this.$shop.prop().serviceUrl+'/user/editUser',data);
				// this.$api.prePage()获取上一页实例，可直接调用上页所有数据和方法，在App.vue定义
				// this.$api.prePage().prePage();
				// this.login(result.data)
				uni.setStorage({//缓存用户登陆状态
				    key: 'userInfo',  
				    data: result.data  
				}) 
				
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
