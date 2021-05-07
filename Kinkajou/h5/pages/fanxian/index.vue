<template>
	<view>
	  <!-- <image src="/static/temp/c8.png" @click="upload()"></image> -->
	</view>
</template>

<script>
	export default {
		data() {
			return {

			}
		},
		methods: {
			
			upload(){
				uni.chooseImage({
					success: (chooseImageRes) => {
						const tempFilePaths = chooseImageRes.tempFilePaths;
						const uploadTask = uni.uploadFile({
							url: 'https://127.0.0.1:5000/common/upload/?dir=product', //仅为示例，非真实的接口地址
							filePath: tempFilePaths[0],
							name: 'file',
							formData: {
								'user': 'test'
							},
							success: (uploadFileRes) => {
								console.log(uploadFileRes.data);
							}
						});
				
						uploadTask.onProgressUpdate((res) => {
							console.log('上传进度' + res.progress);
							console.log('已经上传的数据长度' + res.totalBytesSent);
							console.log('预期需要上传的数据总长度' + res.totalBytesExpectedToSend);
				
							// 测试条件，取消上传任务。
							if (res.progress > 50) {
								uploadTask.abort();
							}
						});
					}
				});
			}
			
			
			
		}
	}
</script>

<style>
page{
		background: $page-color-base;
		background-image: url(/static/fanxian/index.jpg);
		background-repeat:no-repeat;
        background-size:100% 100%;
                -moz-background-size:100% 100%;
	}
</style>
