<template>
	<view>
		<view class="header">
			<view class="input-view">
				
				<input v-model="word" confirm-type="search" class="input" type="text" placeholder="输入搜索关键词" @confirm="confirm">
			</view>
			<button class="mini-btn btnsize" type="primary" size="mini"  @click="search">搜索</button>
			<!-- <button> 搜索</button> -->
		</view>
		
	</view>
</template>
<script>
	import uniIcon from '@/components/uni-icon/uni-icon-search.vue'


	export default {
		components: {
			uniIcon
		},
		data() {
			return {
				word:"",
				showRigth: false,
				showLeft: false
			}
		},
		methods: {
			show(e) {
				if (e === 'left') {
					this.showLeft = true
				} else {
					this.showRigth = true
				}
			},
			hide() {
				this.showLeft = false
				this.showRigth = false
			},
			closeDrawer(e) {
				if (e === 'left') {
					this.showLeft = false
				} else {
					this.showRigth = false
				}
			},
			search(){
				
				uni.redirectTo({
					url: `/pages/product/list?title=`+this.word
				})
			}
		},
		
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

	.header {
		display: flex;
		flex-direction: row;
		padding: 10px 15px;
		align-items: center;
	}

	.input-view {
		display: flex;
		align-items: center;
		flex-direction: row;
		background-color: #e7e7e7;
		height: 30px;
		border-radius: 15px;
		padding: 0 10px;
		flex: 1;
	}

	.uni-padding-wrap {
		padding: 0 15px;
		line-height: 1.8;
	}

	.input {
		flex: 1;
		padding: 0 5px;
		height: 24px;
		line-height: 24px;
		font-size: 16px;
	}

	.close {
		padding: 30upx;
	}
	.btnsize{
		height: 30px;
	}
</style>