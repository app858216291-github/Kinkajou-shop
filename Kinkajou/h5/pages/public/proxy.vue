<template>
	<view class="container">

		<view class="wrapper">
			<view class="welcome">
				数据看板{{str1}}+{{str2}}+{{str3}}
			</view>
			<view class="forget-section">
				按钮
			</view>
		</view>
		
	</view>
</template>

<script>
	export default{
		data(){
			return {
				mobile: '',
				str1:"1",
				str2:"2",
				str3:"3",
				openid:"",
				payInfo:""
				
			}
		},
		onLoad(options){
			this.payInfo=options;
			
			if(options.type="openid"){
				this.link=window.location.href;
				if(((this.link.split('?')).length-1)==2){
					let first=this.link.split('#')[0]
					let first_first=first.split('?')[1]
					let result=first.split('?')[0]+"#"+this.link.split('#')[1]+"&"+first_first
					alert(result)
					window.location.href=result;
					return
				}
				this.getOpenid(options);
				
			}
			
		},
	
		methods: {
			async getOpenid(options){
				
				if(options.getInfo!="yes"){
					let redirect_url=await this.$api.get(this.$shop.prop().serviceUrl+'/common/payGetOpenid',{})
					window.location.href = redirect_url;
				}else{
					this.openid=await this.$api.get(this.$shop.prop().serviceUrl+'/common/payGetOpenid',this.payInfo)
					alert(JSON.stringify(this.openid))
					uni.setStorage({
					key:"openid",
					data:JSON.stringify(this.openid.data)
					})
					window.location.href='http://h5.heshihuan.cn/#/pages/money/pay';
					
				}
				
				
				
				// alert(this.payParam.appid);
			},
		},

	}
</script>


