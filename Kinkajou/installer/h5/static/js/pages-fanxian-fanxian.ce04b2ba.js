(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["pages-fanxian-fanxian"],{1465:function(n,e,t){"use strict";var a=t("3219"),o=t.n(a);o.a},2342:function(n,e,t){var a=t("24fb");e=a(!1),e.push([n.i,"uni-page-body[data-v-0f269d53]{background:$page-color-base;background-image:url(/static/fanxian/index.jpg);background-repeat:no-repeat;background-size:100% 100%;-moz-background-size:100% 100%}body.?%PAGE?%[data-v-0f269d53]{background:$page-color-base;background-image:url(/static/fanxian/index.jpg);background-repeat:no-repeat;background-size:100% 100%}",""]),n.exports=e},"2c56":function(n,e,t){"use strict";t.r(e);var a=t("4f1b"),o=t.n(a);for(var r in a)"default"!==r&&function(n){t.d(e,n,(function(){return a[n]}))}(r);e["default"]=o.a},3219:function(n,e,t){var a=t("2342");"string"===typeof a&&(a=[[n.i,a,""]]),a.locals&&(n.exports=a.locals);var o=t("4f06").default;o("31222dd7",a,!0,{sourceMap:!1,shadowMode:!1})},"4f1b":function(n,e,t){"use strict";Object.defineProperty(e,"__esModule",{value:!0}),e.default=void 0;var a={data:function(){return{}},methods:{upload:function(){uni.chooseImage({success:function(n){var e=n.tempFilePaths,t=uni.uploadFile({url:"https://127.0.0.1:5000/common/upload/?dir=product",filePath:e[0],name:"file",formData:{user:"test"},success:function(n){console.log(n.data)}});t.onProgressUpdate((function(n){console.log("上传进度"+n.progress),console.log("已经上传的数据长度"+n.totalBytesSent),console.log("预期需要上传的数据总长度"+n.totalBytesExpectedToSend),n.progress>50&&t.abort()}))}})}}};e.default=a},"9bcb":function(n,e,t){"use strict";var a;t.d(e,"b",(function(){return o})),t.d(e,"c",(function(){return r})),t.d(e,"a",(function(){return a}));var o=function(){var n=this,e=n.$createElement,t=n._self._c||e;return t("v-uni-view")},r=[]},"9e13":function(n,e,t){"use strict";t.r(e);var a=t("9bcb"),o=t("2c56");for(var r in o)"default"!==r&&function(n){t.d(e,n,(function(){return o[n]}))}(r);t("1465");var u,c=t("f0c5"),i=Object(c["a"])(o["default"],a["b"],a["c"],!1,null,"0f269d53",null,!1,a["a"],u);e["default"]=i.exports}}]);