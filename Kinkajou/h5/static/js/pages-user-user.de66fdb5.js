(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-user-user"],{"068d":function(t,e,n){var i=n("24fb");e=i(!1),e.push([t.i,'@charset "UTF-8";\n/* 页面左右间距 */\n/* 文字尺寸 */\n/*文字颜色*/\n/* 边框颜色 */\n/* 图片加载中颜色 */\n/* 行为相关颜色 */.icon .mix-list-cell.b-b[data-v-4a25f54b]:after{left:%?90?%}.mix-list-cell[data-v-4a25f54b]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:baseline;-webkit-align-items:baseline;align-items:baseline;padding:%?20?% %?30?%;line-height:%?60?%;position:relative}.mix-list-cell.cell-hover[data-v-4a25f54b]{background:#fafafa}.mix-list-cell.b-b[data-v-4a25f54b]:after{left:%?30?%}.mix-list-cell .cell-icon[data-v-4a25f54b]{-webkit-align-self:center;align-self:center;width:%?56?%;max-height:%?60?%;font-size:%?38?%}.mix-list-cell .cell-more[data-v-4a25f54b]{-webkit-align-self:center;align-self:center;font-size:%?30?%;color:#606266;margin-left:10px}.mix-list-cell .cell-tit[data-v-4a25f54b]{-webkit-box-flex:1;-webkit-flex:1;flex:1;font-size:%?28?%;color:#303133;margin-right:%?10?%}.mix-list-cell .cell-tip[data-v-4a25f54b]{font-size:%?26?%;color:#909399}',""]),t.exports=e},"159f":function(t,e,n){var i=n("3c9d");"string"===typeof i&&(i=[[t.i,i,""]]),i.locals&&(t.exports=i.locals);var r=n("4f06").default;r("5e471de3",i,!0,{sourceMap:!1,shadowMode:!1})},"1da1":function(t,e,n){"use strict";function i(t,e,n,i,r,o,a){try{var c=t[o](a),s=c.value}catch(l){return void n(l)}c.done?e(s):Promise.resolve(s).then(i,r)}function r(t){return function(){var e=this,n=arguments;return new Promise((function(r,o){var a=t.apply(e,n);function c(t){i(a,r,o,c,s,"next",t)}function s(t){i(a,r,o,c,s,"throw",t)}c(void 0)}))}}n("d3b7"),Object.defineProperty(e,"__esModule",{value:!0}),e.default=r},"2e1b":function(t,e,n){"use strict";var i;n.d(e,"b",(function(){return r})),n.d(e,"c",(function(){return o})),n.d(e,"a",(function(){return i}));var r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-uni-view",{staticClass:"container"},[n("v-uni-view",{staticClass:"user-section"},[n("v-uni-image",{staticClass:"bg",attrs:{src:"/static/user-bg.jpg"}}),n("v-uni-view",{staticClass:"user-info-box"},[n("v-uni-view",{staticClass:"portrait-box"},[n("v-uni-image",{staticClass:"portrait",attrs:{src:t.userInfo.portrait||"/static/lanhua.jpg"},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.navToLogin.apply(void 0,arguments)}}})],1),n("v-uni-view",{staticClass:"info-box",on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.navToLogin.apply(void 0,arguments)}}},[n("v-uni-text",{staticClass:"username"},[t._v(t._s(t.nickname||"游客"))])],1)],1),n("v-uni-view",{staticClass:"vip-card-box"},[n("v-uni-image",{staticClass:"card-bg",attrs:{src:"/static/vip-card-bg.png",mode:""}}),n("v-uni-view",{staticClass:"tit"},[n("v-uni-text",{staticClass:"yticon icon-iLinkapp-"}),t._v("保证正品，客户至上")],1)],1)],1),n("v-uni-view",{staticClass:"cover-container",style:[{transform:t.coverTransform,transition:t.coverTransition}],on:{touchstart:function(e){arguments[0]=e=t.$handleEvent(e),t.coverTouchstart.apply(void 0,arguments)},touchmove:function(e){arguments[0]=e=t.$handleEvent(e),t.coverTouchmove.apply(void 0,arguments)},touchend:function(e){arguments[0]=e=t.$handleEvent(e),t.coverTouchend.apply(void 0,arguments)}}},[n("v-uni-image",{staticClass:"arc",attrs:{src:"/static/arc.png"}}),n("v-uni-view",{staticClass:"tj-sction"},[n("v-uni-view",{staticClass:"tj-item"},[n("v-uni-text",{staticClass:"num"},[t._v("0")]),n("v-uni-text",[t._v("余额")])],1),n("v-uni-view",{staticClass:"tj-item"},[n("v-uni-text",{staticClass:"num"},[t._v("0")]),n("v-uni-text",[t._v("优惠券")])],1),n("v-uni-view",{staticClass:"tj-item"},[n("v-uni-text",{staticClass:"num"},[t._v(t._s(t.credit))]),n("v-uni-text",[t._v("积分")])],1)],1),n("v-uni-view",{staticClass:"order-section"},[n("v-uni-view",{staticClass:"order-item",attrs:{"hover-class":"common-hover","hover-stay-time":50},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.navTo("/pages/order/order?state=0")}}},[n("v-uni-text",{staticClass:"yticon icon-shouye"}),n("v-uni-text",[t._v("全部订单")])],1),n("v-uni-view",{staticClass:"order-item",attrs:{"hover-class":"common-hover","hover-stay-time":50},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.navTo("/pages/order/order?state=1")}}},[n("v-uni-text",{staticClass:"yticon icon-daifukuan"}),n("v-uni-text",[t._v("待付款")])],1),n("v-uni-view",{staticClass:"order-item",attrs:{"hover-class":"common-hover","hover-stay-time":50},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.navTo("/pages/order/order?state=2")}}},[n("v-uni-text",{staticClass:"yticon icon-yishouhuo"}),n("v-uni-text",[t._v("待收货")])],1),n("v-uni-view",{staticClass:"order-item",attrs:{"hover-class":"common-hover","hover-stay-time":50},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.navTo("/pages/order/order?state=4")}}},[n("v-uni-text",{staticClass:"yticon icon-shouhoutuikuan"}),n("v-uni-text",[t._v("退款/售后")])],1)],1),n("v-uni-view",{staticClass:"history-section icon"},[n("v-uni-view",{staticClass:"sec-header"},[n("v-uni-text",{staticClass:"yticon icon-lishijilu"}),n("v-uni-text",[t._v("浏览历史")])],1),n("v-uni-scroll-view",{staticClass:"h-list",attrs:{"scroll-x":!0}},t._l(t.goodsList,(function(e,i){return n("v-uni-image",{key:i,attrs:{src:e.mainImg,mode:"aspectFill"},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.navTo("/pages/product/his")}}})})),1),n("list-cell",{attrs:{icon:"icon-dizhi",iconColor:"#5fcda2",title:"地址管理"},on:{eventClick:function(e){arguments[0]=e=t.$handleEvent(e),t.navTo("/pages/address/address")}}}),n("list-cell",{attrs:{icon:"icon-shoucang_xuanzhongzhuangtai",iconColor:"#54b4ef",title:"我的收藏"},on:{eventClick:function(e){arguments[0]=e=t.$handleEvent(e),t.navTo("/pages/user/collect")}}}),n("list-cell",{attrs:{icon:"icon-shezhi1",iconColor:"#e07472",title:"设置",border:""},on:{eventClick:function(e){arguments[0]=e=t.$handleEvent(e),t.navTo("/pages/set/set")}}}),n("list-cell",{attrs:{icon:"icon-iLinkapp-",iconColor:"#90a3e0",title:"商家信息",border:""},on:{eventClick:function(e){arguments[0]=e=t.$handleEvent(e),t.navTo("/pages/user/bussinessInfo")}}})],1)],1),n("v-uni-view",{staticStyle:{"background-color":"#f5f5f5",color:"#bb7777","align-items":"center","justify-content":"center","text-align":"center"}},[n("v-uni-text",[n("a",{attrs:{href:"http://site.heshihuan.cn"}},[t._v("&蜜熊科技支持")])])],1)],1)},o=[]},"350e":function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var i={data:function(){return{typeList:{left:"icon-zuo",right:"icon-you",up:"icon-shang",down:"icon-xia"}}},props:{icon:{type:String,default:""},title:{type:String,default:"标题"},tips:{type:String,default:""},navigateType:{type:String,default:"right"},border:{type:String,default:"b-b"},hoverClass:{type:String,default:"cell-hover"},iconColor:{type:String,default:"#333"}},methods:{eventClick:function(){this.$emit("eventClick")}}};e.default=i},"3c9d":function(t,e,n){var i=n("24fb");e=i(!1),e.push([t.i,'@charset "UTF-8";\n/* 页面左右间距 */\n/* 文字尺寸 */\n/*文字颜色*/\n/* 边框颜色 */\n/* 图片加载中颜色 */\n/* 行为相关颜色 */.tj-sction .tj-item[data-v-76a58fc9], .order-section .order-item[data-v-76a58fc9]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;flex-direction:column;-webkit-box-pack:center;-webkit-justify-content:center;justify-content:center;-webkit-box-align:center;-webkit-align-items:center;align-items:center}.tj-sction[data-v-76a58fc9], .order-section[data-v-76a58fc9]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-justify-content:space-around;justify-content:space-around;-webkit-align-content:center;align-content:center;background:#fff;border-radius:%?10?%}.user-section[data-v-76a58fc9]{height:%?520?%;padding:%?100?% %?30?% 0;position:relative}.user-section .bg[data-v-76a58fc9]{position:absolute;left:0;top:0;width:100%;height:100%;-webkit-filter:blur(1px);filter:blur(1px);opacity:.7}.user-info-box[data-v-76a58fc9]{height:%?180?%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center;position:relative;z-index:1}.user-info-box .portrait[data-v-76a58fc9]{width:%?130?%;height:%?130?%;border:%?5?% solid #fff;border-radius:50%}.user-info-box .username[data-v-76a58fc9]{font-size:%?38?%;color:#303133;margin-left:%?20?%}.vip-card-box[data-v-76a58fc9]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;flex-direction:column;color:#f7d680;height:%?240?%;background:-webkit-linear-gradient(left,rgba(0,0,0,.7),rgba(0,0,0,.8));background:linear-gradient(left,rgba(0,0,0,.7),rgba(0,0,0,.8));border-radius:%?16?% %?16?% 0 0;overflow:hidden;position:relative;padding:%?20?% %?24?%}.vip-card-box .card-bg[data-v-76a58fc9]{position:absolute;top:%?20?%;right:0;width:%?380?%;height:%?260?%}.vip-card-box .b-btn[data-v-76a58fc9]{position:absolute;right:%?20?%;top:%?16?%;width:%?132?%;height:%?40?%;text-align:center;line-height:%?40?%;font-size:%?22?%;color:#36343c;border-radius:20px;background:-webkit-linear-gradient(left,#f9e6af,#ffd465);background:linear-gradient(left,#f9e6af,#ffd465);z-index:1}.vip-card-box .tit[data-v-76a58fc9]{font-size:%?30?%;color:#f7d680;margin-bottom:%?28?%}.vip-card-box .tit .yticon[data-v-76a58fc9]{color:#f6e5a3;margin-right:%?16?%}.vip-card-box .e-b[data-v-76a58fc9]{font-size:%?24?%;color:#d8cba9;margin-top:%?10?%}.cover-container[data-v-76a58fc9]{background:#f8f8f8;margin-top:%?-150?%;padding:0 %?30?%;position:relative;background:#f5f5f5;padding-bottom:%?20?%}.cover-container .arc[data-v-76a58fc9]{position:absolute;left:0;top:%?-34?%;width:100%;height:%?36?%}.tj-sction .tj-item[data-v-76a58fc9]{-webkit-box-orient:vertical;-webkit-box-direction:normal;-webkit-flex-direction:column;flex-direction:column;height:%?140?%;font-size:%?24?%;color:#75787d}.tj-sction .num[data-v-76a58fc9]{font-size:%?32?%;color:#303133;margin-bottom:%?8?%}.order-section[data-v-76a58fc9]{padding:%?28?% 0;margin-top:%?20?%}.order-section .order-item[data-v-76a58fc9]{width:%?120?%;height:%?120?%;border-radius:%?10?%;font-size:%?24?%;color:#303133}.order-section .yticon[data-v-76a58fc9]{font-size:%?48?%;margin-bottom:%?18?%;color:#fa436a}.order-section .icon-shouhoutuikuan[data-v-76a58fc9]{font-size:%?44?%}.history-section[data-v-76a58fc9]{padding:%?30?% 0 0;margin-top:%?20?%;background:#fff;border-radius:%?10?%}.history-section .sec-header[data-v-76a58fc9]{display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-align:center;-webkit-align-items:center;align-items:center;font-size:%?28?%;color:#303133;line-height:%?40?%;margin-left:%?30?%}.history-section .sec-header .yticon[data-v-76a58fc9]{font-size:%?44?%;color:#5eba8f;margin-right:%?16?%;line-height:%?40?%}.history-section .h-list[data-v-76a58fc9]{white-space:nowrap;padding:%?30?% %?30?% 0}.history-section .h-list uni-image[data-v-76a58fc9]{display:inline-block;width:%?160?%;height:%?160?%;margin-right:%?20?%;border-radius:%?10?%}',""]),t.exports=e},"44eb":function(t,e,n){"use strict";n.r(e);var i=n("fc14"),r=n("94fd");for(var o in r)"default"!==o&&function(t){n.d(e,t,(function(){return r[t]}))}(o);n("f1cd");var a,c=n("f0c5"),s=Object(c["a"])(r["default"],i["b"],i["c"],!1,null,"4a25f54b",null,!1,i["a"],a);e["default"]=s.exports},"688f":function(t,e,n){"use strict";n.r(e);var i=n("2e1b"),r=n("7342");for(var o in r)"default"!==o&&function(t){n.d(e,t,(function(){return r[t]}))}(o);n("e6ae");var a,c=n("f0c5"),s=Object(c["a"])(r["default"],i["b"],i["c"],!1,null,"76a58fc9",null,!1,i["a"],a);e["default"]=s.exports},7342:function(t,e,n){"use strict";n.r(e);var i=n("f576"),r=n.n(i);for(var o in i)"default"!==o&&function(t){n.d(e,t,(function(){return i[t]}))}(o);e["default"]=r.a},"94fd":function(t,e,n){"use strict";n.r(e);var i=n("350e"),r=n.n(i);for(var o in i)"default"!==o&&function(t){n.d(e,t,(function(){return i[t]}))}(o);e["default"]=r.a},"96cf":function(t,e){!function(e){"use strict";var n,i=Object.prototype,r=i.hasOwnProperty,o="function"===typeof Symbol?Symbol:{},a=o.iterator||"@@iterator",c=o.asyncIterator||"@@asyncIterator",s=o.toStringTag||"@@toStringTag",l="object"===typeof t,u=e.regeneratorRuntime;if(u)l&&(t.exports=u);else{u=e.regeneratorRuntime=l?t.exports:{},u.wrap=w;var f="suspendedStart",d="suspendedYield",v="executing",h="completed",p={},g={};g[a]=function(){return this};var b=Object.getPrototypeOf,m=b&&b(b(O([])));m&&m!==i&&r.call(m,a)&&(g=m);var y=_.prototype=k.prototype=Object.create(g);C.prototype=y.constructor=_,_.constructor=C,_[s]=C.displayName="GeneratorFunction",u.isGeneratorFunction=function(t){var e="function"===typeof t&&t.constructor;return!!e&&(e===C||"GeneratorFunction"===(e.displayName||e.name))},u.mark=function(t){return Object.setPrototypeOf?Object.setPrototypeOf(t,_):(t.__proto__=_,s in t||(t[s]="GeneratorFunction")),t.prototype=Object.create(y),t},u.awrap=function(t){return{__await:t}},L(T.prototype),T.prototype[c]=function(){return this},u.AsyncIterator=T,u.async=function(t,e,n,i){var r=new T(w(t,e,n,i));return u.isGeneratorFunction(e)?r:r.next().then((function(t){return t.done?t.value:r.next()}))},L(y),y[s]="Generator",y[a]=function(){return this},y.toString=function(){return"[object Generator]"},u.keys=function(t){var e=[];for(var n in t)e.push(n);return e.reverse(),function n(){while(e.length){var i=e.pop();if(i in t)return n.value=i,n.done=!1,n}return n.done=!0,n}},u.values=O,S.prototype={constructor:S,reset:function(t){if(this.prev=0,this.next=0,this.sent=this._sent=n,this.done=!1,this.delegate=null,this.method="next",this.arg=n,this.tryEntries.forEach(z),!t)for(var e in this)"t"===e.charAt(0)&&r.call(this,e)&&!isNaN(+e.slice(1))&&(this[e]=n)},stop:function(){this.done=!0;var t=this.tryEntries[0],e=t.completion;if("throw"===e.type)throw e.arg;return this.rval},dispatchException:function(t){if(this.done)throw t;var e=this;function i(i,r){return c.type="throw",c.arg=t,e.next=i,r&&(e.method="next",e.arg=n),!!r}for(var o=this.tryEntries.length-1;o>=0;--o){var a=this.tryEntries[o],c=a.completion;if("root"===a.tryLoc)return i("end");if(a.tryLoc<=this.prev){var s=r.call(a,"catchLoc"),l=r.call(a,"finallyLoc");if(s&&l){if(this.prev<a.catchLoc)return i(a.catchLoc,!0);if(this.prev<a.finallyLoc)return i(a.finallyLoc)}else if(s){if(this.prev<a.catchLoc)return i(a.catchLoc,!0)}else{if(!l)throw new Error("try statement without catch or finally");if(this.prev<a.finallyLoc)return i(a.finallyLoc)}}}},abrupt:function(t,e){for(var n=this.tryEntries.length-1;n>=0;--n){var i=this.tryEntries[n];if(i.tryLoc<=this.prev&&r.call(i,"finallyLoc")&&this.prev<i.finallyLoc){var o=i;break}}o&&("break"===t||"continue"===t)&&o.tryLoc<=e&&e<=o.finallyLoc&&(o=null);var a=o?o.completion:{};return a.type=t,a.arg=e,o?(this.method="next",this.next=o.finallyLoc,p):this.complete(a)},complete:function(t,e){if("throw"===t.type)throw t.arg;return"break"===t.type||"continue"===t.type?this.next=t.arg:"return"===t.type?(this.rval=this.arg=t.arg,this.method="return",this.next="end"):"normal"===t.type&&e&&(this.next=e),p},finish:function(t){for(var e=this.tryEntries.length-1;e>=0;--e){var n=this.tryEntries[e];if(n.finallyLoc===t)return this.complete(n.completion,n.afterLoc),z(n),p}},catch:function(t){for(var e=this.tryEntries.length-1;e>=0;--e){var n=this.tryEntries[e];if(n.tryLoc===t){var i=n.completion;if("throw"===i.type){var r=i.arg;z(n)}return r}}throw new Error("illegal catch attempt")},delegateYield:function(t,e,i){return this.delegate={iterator:O(t),resultName:e,nextLoc:i},"next"===this.method&&(this.arg=n),p}}}function w(t,e,n,i){var r=e&&e.prototype instanceof k?e:k,o=Object.create(r.prototype),a=new S(i||[]);return o._invoke=E(t,n,a),o}function x(t,e,n){try{return{type:"normal",arg:t.call(e,n)}}catch(i){return{type:"throw",arg:i}}}function k(){}function C(){}function _(){}function L(t){["next","throw","return"].forEach((function(e){t[e]=function(t){return this._invoke(e,t)}}))}function T(t){function e(n,i,o,a){var c=x(t[n],t,i);if("throw"!==c.type){var s=c.arg,l=s.value;return l&&"object"===typeof l&&r.call(l,"__await")?Promise.resolve(l.__await).then((function(t){e("next",t,o,a)}),(function(t){e("throw",t,o,a)})):Promise.resolve(l).then((function(t){s.value=t,o(s)}),(function(t){return e("throw",t,o,a)}))}a(c.arg)}var n;function i(t,i){function r(){return new Promise((function(n,r){e(t,i,n,r)}))}return n=n?n.then(r,r):r()}this._invoke=i}function E(t,e,n){var i=f;return function(r,o){if(i===v)throw new Error("Generator is already running");if(i===h){if("throw"===r)throw o;return P()}n.method=r,n.arg=o;while(1){var a=n.delegate;if(a){var c=j(a,n);if(c){if(c===p)continue;return c}}if("next"===n.method)n.sent=n._sent=n.arg;else if("throw"===n.method){if(i===f)throw i=h,n.arg;n.dispatchException(n.arg)}else"return"===n.method&&n.abrupt("return",n.arg);i=v;var s=x(t,e,n);if("normal"===s.type){if(i=n.done?h:d,s.arg===p)continue;return{value:s.arg,done:n.done}}"throw"===s.type&&(i=h,n.method="throw",n.arg=s.arg)}}}function j(t,e){var i=t.iterator[e.method];if(i===n){if(e.delegate=null,"throw"===e.method){if(t.iterator.return&&(e.method="return",e.arg=n,j(t,e),"throw"===e.method))return p;e.method="throw",e.arg=new TypeError("The iterator does not provide a 'throw' method")}return p}var r=x(i,t.iterator,e.arg);if("throw"===r.type)return e.method="throw",e.arg=r.arg,e.delegate=null,p;var o=r.arg;return o?o.done?(e[t.resultName]=o.value,e.next=t.nextLoc,"return"!==e.method&&(e.method="next",e.arg=n),e.delegate=null,p):o:(e.method="throw",e.arg=new TypeError("iterator result is not an object"),e.delegate=null,p)}function $(t){var e={tryLoc:t[0]};1 in t&&(e.catchLoc=t[1]),2 in t&&(e.finallyLoc=t[2],e.afterLoc=t[3]),this.tryEntries.push(e)}function z(t){var e=t.completion||{};e.type="normal",delete e.arg,t.completion=e}function S(t){this.tryEntries=[{tryLoc:"root"}],t.forEach($,this),this.reset(!0)}function O(t){if(t){var e=t[a];if(e)return e.call(t);if("function"===typeof t.next)return t;if(!isNaN(t.length)){var i=-1,o=function e(){while(++i<t.length)if(r.call(t,i))return e.value=t[i],e.done=!1,e;return e.value=n,e.done=!0,e};return o.next=o}}return{next:P}}function P(){return{value:n,done:!0}}}(function(){return this||"object"===typeof self&&self}()||Function("return this")())},d0d8:function(t,e,n){var i=n("068d");"string"===typeof i&&(i=[[t.i,i,""]]),i.locals&&(t.exports=i.locals);var r=n("4f06").default;r("28b84f2e",i,!0,{sourceMap:!1,shadowMode:!1})},e6ae:function(t,e,n){"use strict";var i=n("159f"),r=n.n(i);r.a},f1cd:function(t,e,n){"use strict";var i=n("d0d8"),r=n.n(i);r.a},f576:function(t,e,n){"use strict";var i=n("4ea4");Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var r=i(n("5530"));n("96cf");var o=i(n("1da1")),a=i(n("44eb")),c=n("2f62"),s=0,l=0,u=!0,f={components:{listCell:a.default},data:function(){return{coverTransform:"translateY(0px)",coverTransition:"0s",moving:!1,goodsList:{},loadingType:"more",nickname:"游客",credit:0}},onShow:function(){var t=this;return(0,o.default)(regeneratorRuntime.mark((function e(){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,t.$api.get(t.$shop.prop().serviceUrl+"/user/getUser",{});case 2:n=e.sent,t.nickname=n.data.nickname,t.credit=n.data.credit;case 5:case"end":return e.stop()}}),e)})))()},onLoad:function(){this.userInfo.portrait="/static/lanhua.jpg",this.loadData()},onNavigationBarButtonTap:function(t){var e=t.index;0===e?this.navTo("/pages/set/set"):1===e&&uni.navigateTo({url:"/pages/notice/notice"})},computed:(0,r.default)({},(0,c.mapState)(["hasLogin","userInfo"])),methods:{navTo:function(t){var e=uni.getStorageSync("userInfo");void 0==e.id&&(t="/pages/public/login?url=../user/user"),uni.navigateTo({url:t})},navToLogin:function(){this.hasLogin?uni.navigateTo({url:"/pages/user/userDetail"}):uni.navigateTo({url:"/pages/public/login"})},member:function(){this.$api.msg("尚未开放，敬请期待")},loadData:function(){var t=this;return(0,o.default)(regeneratorRuntime.mark((function e(){var n,i;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return console.info(t.$shop.prop()),n=uni.getStorageSync("historyids")||" ",i={products:n},e.next=5,t.$shop.getProductList(t.$shop.prop().serviceUrl+"/user/his",i);case 5:t.goodsList=e.sent,t.goodsList=t.goodsList.goodsList,console.info("abc");case 8:case"end":return e.stop()}}),e)})))()},coverTouchstart:function(t){!1!==u&&(this.coverTransition="transform .1s linear",s=t.touches[0].clientY)},coverTouchmove:function(t){l=t.touches[0].clientY;var e=l-s;e<0?this.moving=!1:(this.moving=!0,e>=80&&e<100&&(e=80),e>0&&e<=80&&(this.coverTransform="translateY(".concat(e,"px)")))},coverTouchend:function(){!1!==this.moving&&(this.moving=!1,this.coverTransition="transform 0.3s cubic-bezier(.21,1.93,.53,.64)",this.coverTransform="translateY(0px)")},onPullDownRefresh:function(){console.info("aa"),this.loadingType},onReachBottom:function(){console.info("aa")}}};e.default=f},fc14:function(t,e,n){"use strict";var i;n.d(e,"b",(function(){return r})),n.d(e,"c",(function(){return o})),n.d(e,"a",(function(){return i}));var r=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("v-uni-view",{staticClass:"content"},[n("v-uni-view",{staticClass:"mix-list-cell",class:t.border,attrs:{"hover-class":"cell-hover","hover-stay-time":50},on:{click:function(e){arguments[0]=e=t.$handleEvent(e),t.eventClick.apply(void 0,arguments)}}},[t.icon?n("v-uni-text",{staticClass:"cell-icon yticon",class:t.icon,style:[{color:t.iconColor}]}):t._e(),n("v-uni-text",{staticClass:"cell-tit clamp"},[t._v(t._s(t.title))]),t.tips?n("v-uni-text",{staticClass:"cell-tip"},[t._v(t._s(t.tips))]):t._e(),n("v-uni-text",{staticClass:"cell-more yticon",class:t.typeList[t.navigateType]})],1)],1)},o=[]}}]);