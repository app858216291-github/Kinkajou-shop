const prop=function(){
	let ip="127.0.0.1";

	let port="5000";
	let DropDownList={
		orderstatus:[{key:"1",value:"待付款"},{key:"2",value:"待收货"},{key:"3",value:"待评价"},{key:"4",value:"售后"}],
		productstatus:[{1:"待付款"},{2:"待收货"},{3:"待评价"},{4:"售后"}]
	};
	return {
		"serviceIp":ip,
		"serviceUrl":"http://127.0.0.1:5000",
		"DropDownList":DropDownList
		}
}


const layui_table=function(tableid,url,cols,tableName){
	
	layui.use('table', function(){
	  var table = layui.table; 
	  table.render({
	    elem: "#"+tableid
	    ,url:url
	    ,cols: cols
	    ,page: true
	  });

	  //监听工具条
	  table.on('tool(test)', function(obj){ //注：tool是工具条事件名，test是table原始容器的属性 lay-filter="对应的值"
	    var data = obj.data; //获得当前行数据
	    var layEvent = obj.event; //获得 lay-event 对应的值（也可以是表头的 event 参数对应的值）
	    var tr = obj.tr; //获得当前行 tr 的DOM对象
		// var href=window.href;
		var viewPage="./common-view.html?table=";
		var editPage="./common-edit.html?table=";
		if(window.location.href.indexOf("/company/") != -1){
			viewPage="../common-view.html?table=";
			editPage="../common-edit.html?table=";
		}
	    
	    if(layEvent === 'detail'){ //查看
		
			
	  	xadmin.open('添加用户',viewPage+tableName+'&id='+obj.data.id,800,600);
	    } else if(layEvent === 'del'){ //删除
	  	layer.confirm('真的删除行么', function(index){
				$.get(prop().serviceUrl+"/common/model/del/?modelName="+tableName+"&id="+data.id,function(data,status){
					layer.msg("删除成功");
				});
	  	  obj.del(); //删除对应行（tr）的DOM结构，并更新缓存
	  	  layer.close(index);
	  	  //向服务端发送删除指令
	  	});
	    } else if(layEvent === 'edit'){ //编辑
			var s=function(){
			alert("回调成功")
			}
	  	xadmin.open('添加用户',editPage+tableName+'&id='+obj.data.id,800,600);
	  	//同步更新缓存对应的值
			// table.reload(tableid, {page: {curr: 1 }});
	  	// obj.update({
	  	//   username: '123'
	  	//   ,title: 'xxx'
	  	// });
	    }
	  });
	  
	  
	  //监听单元格编辑
	  table.on('edit(test)',
	  function(obj) {
	      var value = obj.value //得到修改后的值
	      ,
	      data = obj.data //得到所在行所有键值
	      ,
	      field = obj.field; //得到字段
	  	$.get(prop().serviceUrl+"/common/model/edit/?modelName="+tableName+"&id="+data.id+"&"+field+"="+value,function(data,status){
	  		layer.msg("修改成功");
	  	});
	      layer.msg('[ID: ' + data.id + '] ' + field + ' 字段更改为：' + value);
	  });
		var $ = layui.jquery, layer = layui.layer;
		
		// var dellAll2=function(){
		// 	var checkStatus=table.checkStatus(tableid),data=checkStatus.data;
		// 	for(var i=)
		// 	debugger
		// }
		$("#delbutton").click(function(){
			var checkStatus=table.checkStatus(tableid),data=checkStatus.data;
			for(var i=0;i<checkStatus.data.length;i++){
				$.get(prop().serviceUrl+"/common/model/del/?modelName="+tableName+"&id="+checkStatus.data[i].id,function(data,status){
				console.info("删除")
				});
				location.reload();
			}
		});
		// var aa = document.getElementById('delAll2')
		// aa.onclick = dellAll2
		// 	debugger
		// 	var othis = $(this), method = othis.data('method');
  //       active[method].call(this, othis);
		// }
		// //动态加载元素用
  //   $('#dellAll').click(function(){
		// 	debugger
		// 	$("p").slideToggle();
		// });
	  
	});
	
}

function delAll(){
		location.reload();
}

function returnPic(mainImgs){
		if(!mainImgs||mainImgs.length<=0)
			return "";
		if(mainImgs[0]==','){
			mainImgs=mainImgs.substring(1,mainImgs.length)
		}
		let imgList=mainImgs.split(',')
		let template=      "<div id='mainImg'>"
		for(let i=0;i<imgList.length;i++){
			if(imgList[i].trim()==""){
				continue;
			}
			template=template+"<img width=150 src="+imgList[i]+"?x-oss-process=image/resize,h_100>&nbsp;"
		}
		template=template+"</div>"
		return template
}