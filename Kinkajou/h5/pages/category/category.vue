<template>
	<view class="content">
		<scroll-view scroll-y class="left-aside">
			<view v-for="item in flist" :key="item.cid" class="f-item b-b" :class="{active: item.cid == currentId}" @click="tabtap(item)">
				{{item.name}}
			</view>
		</scroll-view>
		<scroll-view scroll-with-animation scroll-y class="right-aside" @scroll="asideScroll" :scroll-top="tabScrollTop">
			<view @click="navToList(item.cid)" v-for="item in slist" :key="item.cid" class="s-list" :id="'main-'+item.cid">
				<text class="s-item">{{item.name}}</text>
				<view class="t-list">
					<view @click="navToList(item.cid, titem.cid)" v-if="titem.pid == item.cid" class="t-item" v-for="titem in tlist" :key="titem.cid">
						<image :src="titem.picture"></image>
						<text>{{titem.name}}</text>
					</view>
				</view>
			</view>
		</scroll-view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				sizeCalcState: false,
				tabScrollTop: 0,
				currentId: 1,
				flist: [],
				slist: [],
				tlist: [],
			}
		},
		onLoad(){
			this.loadData();
		},
		methods: {
			async loadData(){
				// let list = await this.$api.json('cateList');
				let list = await this.$api.get(this.$shop.prop().serviceUrl+'/common/model/queryAll/?modelName=Category&page=1&pageSize=50',{});
				list=list.data;
				
				this.tProductList=await this.$shop.getProductList(this.$shop.prop().serviceUrl+'/product/productList?page=1&pageSize=10',{})
				let a=this.tProductList;
				this.tProductList=this.tProductList.data;
				for(let t=0;t<this.tProductList.length;t++){
					let titem={};
					
					titem.id=this.tProductList[t].id;
					titem.cid="t"+this.tProductList[t].id;
					titem.pid=this.tProductList[t].category;
					titem.name=this.tProductList[t].title;
					titem.picture=this.tProductList[t].mainImg;
					list.push(titem);
				}
				
				
				// list.forEach(item=>{
				// 	if(!item.pid){
				// 		this.flist.push(item);  //pid为父级id, 没有pid或者pid=0是一级分类
				// 	}else if(!item.picture){
				// 		this.slist.push(item); //没有图的是2级分类
				// 	}else{
				// 		this.tlist.push(item); //3级分类
				// 	}
				// }) 
				list.forEach(item=>{
					if(item.cid.indexOf("f") != -1){
						// let list2324 = item.slice(0);
						let fitem={};
						fitem=Object.assign(fitem,item);
						this.flist.push(fitem);  //pid为父级id, 没有pid或者pid=0是一级分类
					}else if(item.cid.indexOf("s") != -1){
						let sitem={};
						sitem=Object.assign(sitem,item);
						// let flist1=
						this.slist.push(sitem); //没有图的是2级分类
					}else if(item.cid.indexOf("t") != -1){
						let titem={};
						titem=Object.assign(titem,item);
						// let flist1=Object.assign(flist1,item);
						this.tlist.push(titem); //3级分类
					}
				})
				
			},
			//一级分类点击
			tabtap(item){
				if(!this.sizeCalcState){
					this.calcSize();
				}
				
				this.currentId = item.cid;
				let index = this.slist.findIndex(sitem=>sitem.pid === item.cid);
				let a=this.slist;
				let b=this.flist;
				let c=this.tlist;
				
				this.tabScrollTop = this.slist[index].top;
			},
			//右侧栏滚动
			asideScroll(e){
				if(!this.sizeCalcState){
					this.calcSize();
				}
				let scrollTop = e.detail.scrollTop;
				let tabs = this.slist.filter(item=>item.top <= scrollTop).reverse();
				if(tabs.length > 0){
					this.currentId = tabs[0].pid;
				}
			},
			//计算右侧栏每个tab的高度等信息
			calcSize(){
				let h = 0;
				this.slist.forEach(item=>{
					let view = uni.createSelectorQuery().select("#main-" + item.cid);
					view.fields({
						size: true
					}, data => {
						item.top = h;
						h += data.height;
						item.bottom = h;
					}).exec();
				})
				this.sizeCalcState = true;
			},
			navToList(sid, tid){
				
				uni.navigateTo({
					url: `/pages/product/list?fid=${this.currentId}&sid=${sid}&tid=${tid}`
				})
			},
			navToDetail(sid, tid){
				
				uni.navigateTo({
					url: `/pages/product/product?id=6`
				})
			}
		}
	}
</script>

<style lang='scss'>
	page,
	.content {
		height: 100%;
		background-color: #f8f8f8;
	}

	.content {
		display: flex;
	}
	.left-aside {
		flex-shrink: 0;
		width: 200upx;
		height: 100%;
		background-color: #fff;
	}
	.f-item {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 100upx;
		font-size: 28upx;
		color: $font-color-base;
		position: relative;
		&.active{
			color: $base-color;
			background: #f8f8f8;
			&:before{
				content: '';
				position: absolute;
				left: 0;
				top: 50%;
				transform: translateY(-50%);
				height: 36upx;
				width: 8upx;
				background-color: $base-color;
				border-radius: 0 4px 4px 0;
				opacity: .8;
			}
		}
	}

	.right-aside{
		flex: 1;
		overflow: hidden;
		padding-left: 20upx;
	}
	.s-item{
		display: flex;
		align-items: center;
		height: 70upx;
		padding-top: 8upx;
		font-size: 28upx;
		color: $font-color-dark;
	}
	.t-list{
		display: flex;
		flex-wrap: wrap;
		width: 100%;
		background: #fff;
		padding-top: 12upx;
		&:after{
			content: '';
			flex: 99;
			height: 0;
		}
	}
	.t-item{
		flex-shrink: 0;
		display: flex;
		justify-content: center;
		align-items: center;
		flex-direction: column;
		width: 176upx;
		font-size: 26upx;
		color: #666;
		padding-bottom: 20upx;
		
		image{
			width: 140upx;
			height: 140upx;
		}
	}
</style>
