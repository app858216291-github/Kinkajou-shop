const prop=function(){
	return {
		"serviceIp":'http://127.0.0.1',
		"serviceUrl":"http://127.0.0.1:5000"
	
		}
};

const test1=function(tableid,url,cols,tableName){
	alert("aa"); 
};
const get=function(){
	
	  let htmlobj=$.ajax({
		  url:"http://127.0.0.1:5000/api/common/model/queryAll/?modelName=Category&page=1&pageSize=50",async:true
		  });
	  // debugger;
	  $("#myDiv").html(htmlobj.responseText);
};
//获取参数
const getQueryVariable=function(variable)
	{
		   var query = window.location.search.substring(1);
		   var vars = query.split("&");
		   for (var i=0;i<vars.length;i++) {
				   var pair = vars[i].split("=");
				   if(pair[0] == variable){return pair[1];}
		   }
		   return(false);
	}
//	获取页面
const pageName=function()
     {
         var strUrl=location.href;
         var arrUrl=strUrl.split("/");
		 arrUrl=arrUrl[arrUrl.length-1].split("?")
         var strPage=arrUrl[0];
		 
         return strPage;
     }
//默认使用同步get
const getJson=function (url,asyncstate=false)
	{	
	    $.ajaxSettings.async = asyncstate;
		var r;
		url=prop().serviceUrl+url;
	
		$.getJSON(url,function(result){
		
			r=result.data
		})
		$.ajaxSettings.async = true;
		return r;
	}