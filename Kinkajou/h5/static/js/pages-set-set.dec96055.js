(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-set-set"],{"06df":function(t,e,a){var n=a("24fb");e=n(!1),e.push([t.i,'@charset "UTF-8";\n/* 页面左右间距 */\n/* 文字尺寸 */\n/*文字颜色*/\n/* 边框颜色 */\n/* 图片加载中颜色 */\n/* 行为相关颜色 */uni-page-body[data-v-74f1e5a6]{background:#f8f8f8}.list-cell[data-v-74f1e5a6]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:baseline;-webkit-align-items:baseline;align-items:baseline;padding:%?20?% %?30?%;line-height:%?60?%;position:relative;background:#fff;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center}.list-cell.log-out-btn[data-v-74f1e5a6]{margin-top:%?40?%}.list-cell.log-out-btn .cell-tit[data-v-74f1e5a6]{color:#fa436a;text-align:center;margin-right:0}.list-cell.cell-hover[data-v-74f1e5a6]{background:#fafafa}.list-cell.b-b[data-v-74f1e5a6]:after{left:%?30?%}.list-cell.m-t[data-v-74f1e5a6]{margin-top:%?16?%}.list-cell .cell-more[data-v-74f1e5a6]{-webkit-align-self:baseline;align-self:baseline;font-size:%?32?%;color:#909399;margin-left:%?10?%}.list-cell .cell-tit[data-v-74f1e5a6]{-webkit-box-flex:1;-webkit-flex:1;flex:1;font-size:%?30?%;color:#303133;margin-right:%?10?%}.list-cell .cell-tip[data-v-74f1e5a6]{font-size:%?28?%;color:#909399}.list-cell uni-switch[data-v-74f1e5a6]{-webkit-transform:translateX(%?16?%) scale(.84);transform:translateX(%?16?%) scale(.84)}body.?%PAGE?%[data-v-74f1e5a6]{background:#f8f8f8}',""]),t.exports=e},"165d":function(t,e,a){"use strict";var n=a("4ea4");Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var i=n(a("5530")),l=a("2f62"),s={data:function(){return{}},methods:(0,i.default)((0,i.default)({},(0,l.mapMutations)(["logout"])),{},{navTo:function(t){uni.navigateTo({url:t})},toLogout:function(){var t=this;uni.showModal({content:"确定要退出登录么",success:function(e){e.confirm&&(t.logout(),setTimeout((function(){uni.navigateBack()}),200))}})},switchChange:function(t){var e=t.detail.value?"打开":"关闭";this.$api.msg("".concat(e,"消息推送"))}})};e.default=s},"2c28":function(t,e,a){var n=a("06df");"string"===typeof n&&(n=[[t.i,n,""]]),n.locals&&(t.exports=n.locals);var i=a("4f06").default;i("22eabd1c",n,!0,{sourceMap:!1,shadowMode:!1})},"3cb3":function(t,e,a){"use strict";var n;a.d(e,"b",(function(){return i})),a.d(e,"c",(function(){return l})),a.d(e,"a",(function(){return n}));var i=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-uni-view",{staticClass:"container"},[a("v-uni-view",{staticClass:"list-cell b-b m-t",attrs:{"hover-class":"cell-hover","hover-stay-time":50},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.navTo("/pages/user/userDetail")}}},[a("v-uni-text",{staticClass:"cell-tit"},[t._v("个人资料")]),a("v-uni-text",{staticClass:"cell-more yticon icon-you"})],1),a("v-uni-view",{staticClass:"list-cell b-b",attrs:{"hover-class":"cell-hover","hover-stay-time":50},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.navTo("/pages/address/address")}}},[a("v-uni-text",{staticClass:"cell-tit"},[t._v("收货地址")]),a("v-uni-text",{staticClass:"cell-more yticon icon-you"})],1),a("v-uni-view",{staticClass:"list-cell log-out-btn",on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.toLogout.apply(void 0,arguments)}}},[a("v-uni-text",{staticClass:"cell-tit"},[t._v("退出登录")])],1)],1)},l=[]},4064:function(t,e,a){"use strict";a.r(e);var n=a("165d"),i=a.n(n);for(var l in n)"default"!==l&&function(t){a.d(e,t,(function(){return n[t]}))}(l);e["default"]=i.a},"733d":function(t,e,a){"use strict";a.r(e);var n=a("3cb3"),i=a("4064");for(var l in i)"default"!==l&&function(t){a.d(e,t,(function(){return i[t]}))}(l);a("8734");var s,c=a("f0c5"),o=Object(c["a"])(i["default"],n["b"],n["c"],!1,null,"74f1e5a6",null,!1,n["a"],s);e["default"]=o.exports},8734:function(t,e,a){"use strict";var n=a("2c28"),i=a.n(n);i.a}}]);