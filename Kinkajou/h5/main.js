import Vue from 'vue'
import store from './store'
import App from './App'

import Json from './Json' //测试用数据
/**
 *  因工具函数属于公司资产, 所以直接在Vue实例挂载几个常用的函数
 *  所有测试用数据均存放于根目录json.js
 *  
 *  css部分使用了App.vue下的全局样式和iconfont图标，有需要图标库的可以留言。
 *  示例使用了uni.scss下的变量, 除变量外已尽量移除特有语法,可直接替换为其他预处理器使用
 */
const msg = (title, duration=1500, mask=false, icon='none')=>{
	//统一提示方便全局修改
	if(Boolean(title) === false){
		return;
	}
	uni.showToast({
		title,
		duration,
		mask,
		icon
	});
}

const msgModal = (content="是否确认支付",title="提示", showCancel=true, cancelText='取消按钮文字')=>{
	uni.showModal({
	    title: '提示',
	    content: '弹出一个临时窗口',
	    success: function (res) {
	        if (res.confirm) {
	            console.log('用户点击确定');
				return true;
	        } else if (res.cancel) {
	            console.log('用户点击取消');
				return false;
	        }
	    }
	});
}
const json = type=>{
	//模拟异步请求数据
	return new Promise(resolve=>{
		setTimeout(()=>{
			resolve(Json[type]);
		}, 100)
	})
}

const setStoreHis = (value)=>{
	let historyids = uni.getStorageSync('historyids') || ' '
	historyids=historyids.replace(value+',', "")
	historyids=historyids+value+","
	console.info("浏览记录："+historyids)
	// historyids=""
	uni.setStorage({
		key: 'historyids',
		data: historyids  
	});
}

const get = (url,obj)=>{
	//模拟异步请求数据
	return new Promise((resolve, reject) => {
		let u=uni.getStorageSync('userInfo');
		let token=""
		if(u!=undefined){
			token=uni.getStorageSync('userInfo').token;
		}
		
		// token="150_158_157_86_107_148_171_86_93_157_152_166_104_"
		uni.request({  
			url: url,  
			data: obj, 
			header:{
			 		'token':token,
			 		},
			success: (result) => {  
				resolve(result.data);  
			},  
			fail: (e) => {  
				reject(e);  
			}  
		})  
	})  
}

const post = (url,obj)=>{
	//模拟异步请求数据
	return new Promise((resolve, reject) => {
		let cc=document.cookie;
		let name="csrf_token";
		var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
		let value= r ? r[1] : undefined;
		console.info("----------cookie------------------")
		console.info(value)
		debugger
		// let aa=getCookie("csrf_token")
		// token="150_158_157_86_107_148_171_86_93_157_152_166_104_"
		uni.request({  
			url: url,  
			data: obj, 
			method:'POST',
			header:{
			 		'Content-Type': 'application/x-www-form-urlencoded' ,
					// "X-CSRFToken": value
			 		},
			dataType:'json',
			success: (result) => { 
				debugger
				resolve(result.data);  
			},  
			fail: (e) => {  
				reject(e);  
			}  
		})  
	})  
}


const prePage = ()=>{
	let pages = getCurrentPages();
	let prePage = pages[pages.length - 2];
	// #ifdef H5
	return prePage;
	// #endif
	return prePage.$vm;
}


//-------------商城封装工具函数start-------------------------


const login_openid=()=>{
	
	var ua = window.navigator.userAgent.toLowerCase();
	console.log(ua);//mozilla/5.0 (iphone; cpu iphone os 9_1 like mac os x) applewebkit/601.1.46 (khtml, like gecko)version/9.0 mobile/13b143 safari/601.1
	if (ua.match(/MicroMessenger/i) == 'micromessenger') {
	    console.info("微信浏览器") // 微信中打开
		let openid;
		let user=uni.getStorageSync('userInfo');
		if(user!=undefined){
			openid=user.openid;
		}else{
			openid=undefined;
		}
		
		if(openid==undefined ||openid.length<5){
			return false;
		}
		return true;
	} else {
	    console.info("普通浏览器")// 普通浏览器中打开
		return true;
	}
	
	
	

}
const prop=()=>{
	// if (getApp().globalData.serviceUrl=="fail get data"){
	// 	var startTime = new Date().getTime() + parseInt(1000, 10);
	//     while(new Date().getTime() < startTime) {
	// 		console.info("wait")
	// 	}
	// 	}
	let serviceUrl=uni.getStorageSync('serviceUrl');
	
	// return {"serviceUrl":getApp().globalData.serviceUrl}
	return {"serviceUrl":serviceUrl}
	
	// return {
	// 	// "serviceIp":ip,
	// 	// "serviceUrl":"http://h5.heshihuan.cn/api",
	// 	"serviceUrl":"http://127.0.0.1:5000",
	// 	// "payUrl":"http://"+payIp+":"+port,
	// 	// "payUrl":"http://h5.heshihuan.cn/api",
		
	// 	}
	/**
	// let ip="127.0.0.1";
	//let ip="120.24.221.15";
	// let payIp="120.24.221.15"
	// let port="5000";
	return {
		// "serviceIp":ip,
		// "serviceUrl":"http://h5.heshihuan.cn/api",
		"serviceUrl":"http://127.0.0.1:5000",
		// "payUrl":"http://"+payIp+":"+port,
		// "payUrl":"http://h5.heshihuan.cn/api",
		
		}
		**/
}  

//获取产品
const getProduct = (url,obj)=>{
	//模拟异步请求数据
	return new Promise((resolve, reject) => {  
		if(!url){url=prop().serviceUrl+'/product/productDetail?id=1';} 
		if(!obj){obj={};}
		uni.request({  
			url: url,  
			data: obj,  
			success: (result) => {
				
				let data=result.data.data
				let mainImgs=data.main_image
				if(mainImgs[0]==','){
					mainImgs=mainImgs.substring(1,mainImgs.length)
				}
				let arrayImages=mainImgs.split(',')
				data.mainImg=getYunImage(data.main_image,200)
				resolve(data);  
			},  
			fail: (e) => {  
				reject(e);  
			}  
		})  
	})  
}
//获取产品列表
const getProductList = (url,obj)=>{
	//模拟异步请求数据
	return new Promise((resolve, reject) => {  
		let u=uni.getStorageSync('userInfo');
		let token=""
		if(u!=undefined){
			token=uni.getStorageSync('userInfo').token;
		}
		
		// token="150_158_157_86_107_148_171_86_93_157_152_166_104_"

		if(!url){url=prop().serviceUrl+'/product/productList';} 
		if(!obj){obj={};} 
		uni.request({  
			url: url,  
			data: obj,  
			header:{
			 		'token':token,
			 		},
			success: (result) => {
				let goodsList=result.data
				// if(goodsList)
				goodsList=result.data.data
				// for(let i=0;i<goodsList.length;i++){
				// 	let p=goodsList[i];
				// 	// let p3=eval("("+p+")");
				// 	goodsList[i]=p3;
				// }
				for(let i=0;i<goodsList.length;i++){
					// let p=;
					
					let mainImgs=goodsList[i].main_image
					if(!mainImgs){
						continue
					}
				
					if(mainImgs[0]==','){
						mainImgs=mainImgs.substring(1,mainImgs.length)
					}
					let arrayImages=mainImgs.split(',')
					
					goodsList[i].mainImg=getYunImage(mainImgs)
					goodsList[i].lowmainImg=getYunImage(mainImgs,10)
				}
				
				result.data.goodsList=goodsList;
				resolve(result.data);  
			},  
			fail: (e) => {  
				reject(e);  
			}  
		})  
	})  
}

const getAddressList = (url,obj)=>{
	//模拟异步请求数据
	return new Promise((resolve, reject) => { 
		let token=uni.getStorageSync('userInfo').token;
		if(!url){url=prop().serviceUrl+'/user/addressList';} 
		if(!obj){obj={};}
		uni.request({  
			url: url,  
			data: obj, 
			header:{
			 	'token':token,
			 	 },
			success: (result) => {
				let addressList=result.data.data
				for(let i=0;i<addressList.length;i++){
					let p=addressList[i];
					// let p3=eval("("+p+")");
					addressList[i]=p;
				}
				resolve(addressList);  
			},  
			fail: (e) => {  
				reject(e);  
			}  
		})  
	})  
}

const getAddress = (url,obj)=>{
	//模拟异步请求数据
	return new Promise((resolve, reject) => { 
		let token=uni.getStorageSync('userInfo').token;
		if(!url){url=prop().serviceUrl+'/user/address';} 
		if(!obj){obj={};}
		uni.request({  
			url: url,  
			data: obj,
			header:{
				'token':token,
				 },
			success: (result) => {
				let address=result.data.data
				// address=eval("("+address+")");
				resolve(address);  
			},  
			fail: (e) => {  
				reject(e);  
			}  
		})  
	})  
}


const addOrder = (url,obj)=>{
	
	//模拟异步请求数据
	return new Promise((resolve, reject) => {  
		let token=uni.getStorageSync('userInfo').token;
		if(!url){url=prop().serviceUrl+'/order/addorder';} 
		if(!obj){obj={};}
		uni.request({  
			url: url,  
			data: obj,  
			header:{
			 		'token':token,
			 		},
			success: (result) => {
				debugger
				if(result.data.code==-2){
					resolve(result.data);
				}
				let data=result.data.data
				resolve(data);  
			},  
			fail: (e) => {  
				reject(e);  
			}  
		})  
	})  
}

const getCatogory = (url,obj)=>{
	//模拟异步请求数据
	return new Promise((resolve, reject) => {
		
		//---start-
		
		if(!url){url=prop().serviceUrl+'/common/model/queryAll/?modelName=Category&page=1&pageSize=50';} 
		if(!obj){obj={};}
		uni.request({  
			url: url,  
			data: obj,  
			success: (result) => {
				let list=result.data.data;
				url=prop().serviceUrl+'/product/productList?page=1&pageSize=10';
				if(!obj){obj={};}
				uni.request({  
					url: url,  
					data: {},  
					success: (result) => {
						
						let tProductList=result.data.data;
						// let tProductList=this.tProductList.data;
						for(let t=0;t<tProductList.length;t++){
							let titem={};
							
							titem.id=tProductList[t].id;
							titem.cid="t"+tProductList[t].id;
							titem.pid=tProductList[t].category;
							titem.name=tProductList[t].title;
							titem.picture=tProductList[t].mainImg;
							titem.isProduct=1;
							list.push(titem);
						}
					
						resolve(list);  
					},  
					fail: (e) => {  
						reject(e);  
					}  
				})
				
				
				// resolve(data);  
			},  
			fail: (e) => {  
				reject(e);  
			}  
		})
		

	})  
}

const getYunImage = (filename,size=400)=>{
	//模拟异步请求数据
	return "https://pyshop.oss-cn-beijing.aliyuncs.com/product/"+filename+"?x-oss-process=image/resize,h_"+size
}
const getOrderList = (url,obj)=>{
	//模拟异步请求数据
	return new Promise((resolve, reject) => {  
		let token=uni.getStorageSync('userInfo').token;
		if(!url){url=prop().serviceUrl+'/order/orders';} 
		if(!obj){obj={};}
		uni.request({  
			url: url,  
			data: obj,
			header:{
			   		'token':token,
					},
			success: (result) => {
				let orders=result.data;
				if(orders.code==-2){
					orders=[];
					orders.code=-2;
					resolve(orders);
					
					return
				}
				orders=result.data.data;
				// for(let i=0;i<orders.length;i++){
				// 	let p=orders[i];
				// 	// let p3=eval("("+p+")");
				// 	orders[i]=p3;
				// }
				
				// orders.forEach(item=>{
				// 	products=getProductList();
				// 	orders.products=products;
				// });
				
				for(let i=0;i<orders.length;i++){
					let products=orders[i].products;
					for(let j=0;j<products.length;j++){
						let mainImgs=products[j].main_image
						if(!mainImgs){
							continue
						}
						if(mainImgs[0]==','){
							mainImgs=mainImgs.substring(1,mainImgs.length)
						}
						let arrayImages=mainImgs.split(',')
						products[j].mainImg="https://pyshop.oss-cn-beijing.aliyuncs.com/product/"+mainImgs+"?x-oss-process=image/resize,h_800"
					
					}
					
				}
				orders.code=1
				resolve(orders); 
			},  
			fail: (e) => {  
				reject(e);  
			}  
		})  
	})  
}

Vue.prototype.$shop = {getProduct,getProductList,getAddressList,getAddress,addOrder,getOrderList,prop,getCatogory,getYunImage};
//-------------商城封装工具函数end-------------------------




Vue.config.productionTip = false
Vue.prototype.$fire = new Vue();
Vue.prototype.$store = store;
Vue.prototype.$api = {msg, json, prePage,get,post,msgModal,setStoreHis,login_openid};


App.mpType = 'app'

const app = new Vue({
    ...App
})
app.$mount()