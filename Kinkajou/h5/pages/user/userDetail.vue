<template>
	<view class="content">
		<view class="row b-b">
			<text class="nick">昵称：</text>
			<text class="nick">{{userInfo.nickname}}</text>
		</view>
		<view class="row b-b">
			<text class="age">年龄：</text>
			<text class="age">{{userInfo.age}}岁</text>
		</view>
		<view class="row b-b">
			<text class="name">姓名：</text>
			<text class="name">{{userInfo.name}}</text>
		</view>
		<view class="row b-b">
			<text class="age">手机号：</text>
			<text class="age">{{userInfo.mobile}}</text>
		</view>
		<!-- 
		
		<view class="row b-b">
			<text class="password">密码</text>
			<text class="password">******</text>
			
		</view>
		<view class="row b-b">
			<text class="address">地址</text>
			<text @click="chooseLocation" class="input">
				{{addressData.address}}{{addressData.addressName}}
			</text>
			<text class="yticon icon-shouhuodizhi"></text>
		</view>
		<view class="row b-b"> 
			<text class="tit">门牌号</text>
			<input class="input" type="text" v-model="addressData.area" placeholder="楼号、门牌" placeholder-class="placeholder" />
		</view> -->
		
		<button class="add-btn" @click="navTo('/pages/user/userDetailEdit')">编辑</button>
	</view>
</template>

<script>
	import {
		mapState
	} from 'vuex';
	export default {
		data() {
			return {
				// userInfoTemp:{}
				
			}
		},
		computed:{
			...mapState(['userInfo']),
			...mapState(['hasLogin'])
		},
		onLoad(option){
			// this.userInfoTemp=this.userInfo;
			
		},
		methods: {

			navTo(url){
				// let url="/pages/user/userDetailEdit"
				uni.navigateTo({  
					url
				})
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
