(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-product-list"],{"0d21":function(t,e,a){"use strict";var i=a("4ea4");a("99af"),a("4de4"),a("4160"),a("4e82"),a("159b"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0,a("96cf");var n=i(a("1da1")),o=i(a("a27b")),s={components:{uniLoadMore:o.default},data:function(){return{cateMaskState:0,headerPosition:"fixed",headerTop:"0px",loadingType:"more",filterIndex:0,cateId:0,fId:0,sId:0,priceOrder:0,cateList:[],goodsList:[],goodsData:{},page:1,pageSize:10,totle:0,has_next:!1,title:""}},onLoad:function(t){var e=this;setTimeout((function(){e.headerTop=document.getElementsByTagName("uni-page-head")[0].offsetHeight+"px"}),500),this.cateId=t.tid,this.sId=t.sid,this.fId=t.fid,this.title=t.title,this.loadCateList(t.fid,t.sid),this.loadData()},onPageScroll:function(t){t.scrollTop>=0?this.headerPosition="fixed":this.headerPosition="absolute"},onPullDownRefresh:function(){this.loadData("refresh")},onReachBottom:function(){this.loadData()},methods:{loadCateList:function(t,e){var a=this;return(0,n.default)(regeneratorRuntime.mark((function t(){var e,i;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,a.$shop.getCatogory("","");case 2:e=t.sent,i=e.filter((function(t){if(t.pid&&t.pid.length>1&&"f"==t.pid[0])return t})),i.forEach((function(t){var a=e.filter((function(e){return e.pid==t.id}));t.child=a})),a.cateList=i;case 6:case"end":return t.stop()}}),t)})))()},loadData:function(){var t=arguments,e=this;return(0,n.default)(regeneratorRuntime.mark((function a(){var i,n;return regeneratorRuntime.wrap((function(a){while(1)switch(a.prev=a.next){case 0:if(i=t.length>0&&void 0!==t[0]?t[0]:"add",n=t.length>1?t[1]:void 0,"add"!==i){a.next=8;break}if("nomore"!==e.loadingType){a.next=5;break}return a.abrupt("return");case 5:e.loadingType="loading",a.next=11;break;case 8:e.page=1,e.goodsList=[],e.loadingType="more";case 11:return void 0==e.sId&&(e.sId=0),void 0==e.title&&(e.title=""),a.next=15,e.$shop.getProductList(e.$shop.prop().serviceUrl+"/product/productList?page="+e.page+"&pageSize="+e.pageSize+"&category="+e.sId+"&title="+e.title,{});case 15:e.goodsData=a.sent,e.goodsList=e.goodsList.concat(e.goodsData.goodsList),e.page=e.page+1,e.has_next=e.goodsData.has_next,0==e.has_next&&(e.loadingType="nomore"),1===e.filterIndex&&e.goodsList.sort((function(t,e){return e.sales-t.sales})),2===e.filterIndex&&e.goodsList.sort((function(t,a){return 1==e.priceOrder?t.price-a.price:a.price-t.price})),"refresh"===i&&(1==n?uni.hideLoading():uni.stopPullDownRefresh());case 23:case"end":return a.stop()}}),a)})))()},tabClick:function(t){this.filterIndex===t&&2!==t||(this.filterIndex=t,this.priceOrder=2===t?1===this.priceOrder?2:1:0,uni.pageScrollTo({duration:300,scrollTop:0}),this.loadData("refresh",1),uni.showLoading({title:"正在加载"}))},toggleCateMask:function(t){var e=this,a="show"===t?10:300,i="show"===t?1:0;this.cateMaskState=2,setTimeout((function(){e.cateMaskState=i}),a)},changeCate:function(t){this.cateId=t.id,this.sId=t.cid,this.toggleCateMask(),uni.pageScrollTo({duration:300,scrollTop:800}),this.loadData("refresh",22)},navToDetailPage:function(t){var e=t.id;uni.navigateTo({url:"/pages/product/product?id=".concat(e)})},stopPrevent:function(){}}};e.default=s},5534:function(t,e,a){"use strict";a.r(e);var i=a("640b"),n=a("e5b8");for(var o in n)"default"!==o&&function(t){a.d(e,t,(function(){return n[t]}))}(o);a("ed4f");var s,c=a("f0c5"),r=Object(c["a"])(n["default"],i["b"],i["c"],!1,null,"1c67fca6",null,!1,i["a"],s);e["default"]=r.exports},"640b":function(t,e,a){"use strict";a.d(e,"b",(function(){return n})),a.d(e,"c",(function(){return o})),a.d(e,"a",(function(){return i}));var i={uniLoadMore:a("a27b").default},n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-uni-view",{staticClass:"content"},[a("v-uni-view",{staticClass:"navbar",style:{position:t.headerPosition,top:t.headerTop}},[a("v-uni-view",{staticClass:"nav-item",class:{current:0===t.filterIndex},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.tabClick(0)}}},[t._v("综合排序")]),a("v-uni-view",{staticClass:"nav-item",class:{current:1===t.filterIndex},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.tabClick(1)}}},[t._v("销量优先")]),a("v-uni-view",{staticClass:"nav-item",class:{current:2===t.filterIndex},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.tabClick(2)}}},[a("v-uni-text",[t._v("价格")]),a("v-uni-view",{staticClass:"p-box"},[a("v-uni-text",{staticClass:"yticon icon-shang",class:{active:1===t.priceOrder&&2===t.filterIndex}}),a("v-uni-text",{staticClass:"yticon icon-shang xia",class:{active:2===t.priceOrder&&2===t.filterIndex}})],1)],1),a("v-uni-text",{staticClass:"cate-item yticon icon-fenlei1",on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.toggleCateMask("show")}}})],1),a("v-uni-view",{staticClass:"goods-list"},t._l(t.goodsList,(function(e,i){return a("v-uni-view",{key:i,staticClass:"goods-item",on:{click:function(a){arguments[0]=a=t.$handleEvent(a),t.navToDetailPage(e)}}},[a("v-uni-view",{staticClass:"image-wrapper"},[a("v-uni-image",{attrs:{src:e.mainImg,mode:"aspectFill"}})],1),a("v-uni-text",{staticClass:"title clamp"},[t._v(t._s(e.title))]),a("v-uni-view",{staticClass:"price-box"},[a("v-uni-text",{staticClass:"price"},[t._v(t._s(e.price))]),a("v-uni-text",[t._v("已售 "+t._s(e.sales))])],1)],1)})),1),a("uni-load-more",{attrs:{status:t.loadingType}}),a("v-uni-view",{staticClass:"cate-mask",class:0===t.cateMaskState?"none":1===t.cateMaskState?"show":"",on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.toggleCateMask.apply(void 0,arguments)}}},[a("v-uni-view",{staticClass:"cate-content",on:{click:function(e){e.stopPropagation(),e.preventDefault(),arguments[0]=e=t.$handleEvent(e),t.stopPrevent.apply(void 0,arguments)},touchmove:function(e){e.stopPropagation(),e.preventDefault(),arguments[0]=e=t.$handleEvent(e),t.stopPrevent.apply(void 0,arguments)}}},[a("v-uni-scroll-view",{staticClass:"cate-list",attrs:{"scroll-y":!0}},t._l(t.cateList,(function(e){return a("v-uni-view",{key:e.id,staticClass:"cate-item b-b",class:{active:e.id==t.cateId},on:{click:function(a){arguments[0]=a=t.$handleEvent(a),t.changeCate(e)}}},[t._v(t._s(e.name))])})),1)],1)],1),"nomore"==t.loadingType?a("v-uni-view",{staticStyle:{"background-color":"#f5f5f5",color:"#bb7777","align-items":"center","justify-content":"center","text-align":"center"}},[a("v-uni-text",[t._v("&蜜熊科技支持")])],1):t._e()],1)},o=[]},8388:function(t,e,a){var i=a("cd1b");"string"===typeof i&&(i=[[t.i,i,""]]),i.locals&&(t.exports=i.locals);var n=a("4f06").default;n("1b769913",i,!0,{sourceMap:!1,shadowMode:!1})},cd1b:function(t,e,a){var i=a("24fb");e=i(!1),e.push([t.i,'@charset "UTF-8";\n/* 页面左右间距 */\n/* 文字尺寸 */\n/*文字颜色*/\n/* 边框颜色 */\n/* 图片加载中颜色 */\n/* 行为相关颜色 */uni-page-body[data-v-1c67fca6], .content[data-v-1c67fca6]{background:#f8f8f8}.content[data-v-1c67fca6]{padding-top:%?96?%}.navbar[data-v-1c67fca6]{position:fixed;left:0;top:var(--window-top);display:-webkit-box;display:-webkit-flex;display:flex;width:100%;height:%?80?%;background:#fff;box-shadow:0 %?2?% %?10?% rgba(0,0,0,.06);z-index:10}.navbar .nav-item[data-v-1c67fca6]{-webkit-box-flex:1;-webkit-flex:1;flex:1;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;align-items:center;height:100%;font-size:%?30?%;color:#303133;position:relative}.navbar .nav-item.current[data-v-1c67fca6]{color:#fa436a}.navbar .nav-item.current[data-v-1c67fca6]:after{content:"";position:absolute;left:50%;bottom:0;-webkit-transform:translateX(-50%);transform:translateX(-50%);width:%?120?%;height:0;border-bottom:%?4?% solid #fa436a}.navbar .p-box[data-v-1c67fca6]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;flex-direction:column}.navbar .p-box .yticon[data-v-1c67fca6]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;width:%?30?%;height:%?14?%;line-height:1;margin-left:%?4?%;font-size:%?26?%;color:#888}.navbar .p-box .yticon.active[data-v-1c67fca6]{color:#fa436a}.navbar .p-box .xia[data-v-1c67fca6]{-webkit-transform:scaleY(-1);transform:scaleY(-1)}.navbar .cate-item[data-v-1c67fca6]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;align-items:center;height:100%;width:%?80?%;position:relative;font-size:%?44?%}.navbar .cate-item[data-v-1c67fca6]:after{content:"";position:absolute;left:0;top:50%;-webkit-transform:translateY(-50%);transform:translateY(-50%);border-left:1px solid #ddd;width:0;height:%?36?%}\n/* 分类 */.cate-mask[data-v-1c67fca6]{position:fixed;left:0;top:var(--window-top);bottom:0;width:100%;background:transparent;z-index:95;-webkit-transition:.3s;transition:.3s}.cate-mask .cate-content[data-v-1c67fca6]{width:%?630?%;height:100%;background:#fff;float:right;-webkit-transform:translateX(100%);transform:translateX(100%);-webkit-transition:.3s;transition:.3s}.cate-mask.none[data-v-1c67fca6]{display:none}.cate-mask.show[data-v-1c67fca6]{background:rgba(0,0,0,.4)}.cate-mask.show .cate-content[data-v-1c67fca6]{-webkit-transform:translateX(0);transform:translateX(0)}.cate-list[data-v-1c67fca6]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;flex-direction:column;height:100%}.cate-list .cate-item[data-v-1c67fca6]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center;height:%?90?%;padding-left:%?30?%;font-size:%?28?%;color:#555;position:relative}.cate-list .two[data-v-1c67fca6]{height:%?64?%;color:#303133;font-size:%?30?%;background:#f8f8f8}.cate-list .active[data-v-1c67fca6]{color:#fa436a}\n/* 商品列表 */.goods-list[data-v-1c67fca6]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-flex-wrap:wrap;flex-wrap:wrap;padding:0 %?30?%;background:#fff}.goods-list .goods-item[data-v-1c67fca6]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;flex-direction:column;width:48%;padding-bottom:%?40?%}.goods-list .goods-item[data-v-1c67fca6]:nth-child(2n+1){margin-right:4%}.goods-list .image-wrapper[data-v-1c67fca6]{width:100%;height:%?330?%;border-radius:3px;overflow:hidden}.goods-list .image-wrapper uni-image[data-v-1c67fca6]{width:100%;height:100%;opacity:1}.goods-list .title[data-v-1c67fca6]{font-size:%?32?%;color:#303133;line-height:%?80?%}.goods-list .price-box[data-v-1c67fca6]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;padding-right:%?10?%;font-size:%?24?%;color:#909399}.goods-list .price[data-v-1c67fca6]{font-size:%?32?%;color:#fa436a;line-height:1}.goods-list .price[data-v-1c67fca6]:before{content:"￥";font-size:%?26?%}body.?%PAGE?%[data-v-1c67fca6]{background:#f8f8f8}',""]),t.exports=e},e5b8:function(t,e,a){"use strict";a.r(e);var i=a("0d21"),n=a.n(i);for(var o in i)"default"!==o&&function(t){a.d(e,t,(function(){return i[t]}))}(o);e["default"]=n.a},ed4f:function(t,e,a){"use strict";var i=a("8388"),n=a.n(i);n.a}}]);