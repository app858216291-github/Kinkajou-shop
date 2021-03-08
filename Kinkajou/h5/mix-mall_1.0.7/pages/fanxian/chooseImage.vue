<template>
	<view>
		<button type="primary" @click="img">button</button>
		<button type="primary" @tap="info">info</button>
	</view>
</template>

<script>
export default {
	data() {
		return {};
	},
	methods: {
		// img:function(){
		//     uni.chooseImage({
		//         // count:  允许上传的照片数量
		//         count:5,
		//         // sizeType:  original 原图，compressed 压缩图，默认二者都有
		//         sizeType: "original",
		//         success: function(res){
		//             console.log(res)
		//         }
		//     });
		// },
		img() {
			uni.chooseImage({
				// count:  允许上传的照片数量
				count: 5,
				sizeType: ['original', 'compressed'], //原图，compressed 压缩图，默认二者都有

				success(res) {
					const tempFilePaths = res.tempFilePaths;
					const uploadTask = uni.uploadFile({
						url: 'http://120.24.221.15:5000/common/upload/?dir=product',
						filePath: tempFilePaths[0],
						name: 'file',
						formData: {
							user: 'test'
						},
						success: function(uploadFileRes) {
							
							console.log(uploadFileRes.data);
						}
					});
					
					console.log(res);
					uni.previewImage({
						// 对选中的图片进行预览
						urls: res.tempFilePaths
						// urls:['','']  图片的地址 是数组形式
					});
				}
			});
		},
		info() {
			uni.getImageInfo({
				src: 'http://img-cdn-qiniu.dcloud.net.cn/uploads/answer/20190316/6a6ab954272d4fdee479c9a4d56b8bb7.jpeg',
				success(res) {
					console.log(res);
				}
			});
		}
		// info:function(){
		//     uni.getImageInfo({
		//         src:'http://static.hcoder.net/public/images/logo.png',
		//         success: function(res){
		//             console.log(res)
		//         }
		//     })
		// }
	}
};
</script>

<style></style>
