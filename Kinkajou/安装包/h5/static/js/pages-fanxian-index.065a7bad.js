(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-fanxian-index"],{"0e89":function(a,e,n){var t=n("3923");"string"===typeof t&&(t=[[a.i,t,""]]),t.locals&&(a.exports=t.locals);var o=n("4f06").default;o("4805a2b0",t,!0,{sourceMap:!1,shadowMode:!1})},"246f":function(a,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var t={data:function(){return{}},methods:{upload:function(){uni.chooseImage({success:function(a){var e=a.tempFilePaths,n=uni.uploadFile({url:"https://127.0.0.1:5000/common/upload/?dir=product",filePath:e[0],name:"file",formData:{user:"test"},success:function(a){console.log(a.data)}});n.onProgressUpdate((function(a){console.log("上传进度"+a.progress),console.log("已经上传的数据长度"+a.totalBytesSent),console.log("预期需要上传的数据总长度"+a.totalBytesExpectedToSend),a.progress>50&&n.abort()}))}})}}};e.default=t},3923:function(a,e,n){var t=n("24fb");e=t(!1),e.push([a.i,"uni-page-body[data-v-1a89d5b4]{background:$page-color-base;background-image:url(/static/fanxian/index.jpg);background-repeat:no-repeat;background-size:100% 100%;-moz-background-size:100% 100%}body.?%PAGE?%[data-v-1a89d5b4]{background:$page-color-base;background-image:url(/static/fanxian/index.jpg);background-repeat:no-repeat;background-size:100% 100%}",""]),a.exports=e},3980:function(a,e,n){"use strict";var t;n.d(e,"b",(function(){return o})),n.d(e,"c",(function(){return r})),n.d(e,"a",(function(){return t}));var o=function(){var a=this,e=a.$createElement,n=a._self._c||e;return n("v-uni-view")},r=[]},"60ba":function(a,e,n){"use strict";n.r(e);var t=n("3980"),o=n("a16a");for(var r in o)"default"!==r&&function(a){n.d(e,a,(function(){return o[a]}))}(r);n("ca99");var u,c=n("f0c5"),i=Object(c["a"])(o["default"],t["b"],t["c"],!1,null,"1a89d5b4",null,!1,t["a"],u);e["default"]=i.exports},a16a:function(a,e,n){"use strict";n.r(e);var t=n("246f"),o=n.n(t);for(var r in t)"default"!==r&&function(a){n.d(e,a,(function(){return t[a]}))}(r);e["default"]=o.a},ca99:function(a,e,n){"use strict";var t=n("0e89"),o=n.n(t);o.a}}]);