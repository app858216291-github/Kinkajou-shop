<template>
	<view class="content">
		<view class="row b-b" style="justify-content:center">
			<!-- <text class="nick">商家信息：</text> -->
			<text class="nick">南靖兰花</text>
		</view>
		<view class="row b-b"  style="justify-content:center">
			<text class="age">联系人：</text>
			<text class="age">方先生</text>
		</view>
		<view class="row b-b"  style="justify-content:center">
			<text class="age">咨询 微信/手机号：</text>
			<text class="age">18050627580</text>
		</view>
		
		<view class="row b-b"  style="justify-content:center">
			<text class="age">投诉电话：</text>
			<text class="age">13774514086</text>
		</view>

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
		
		
		methods: {

			
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
