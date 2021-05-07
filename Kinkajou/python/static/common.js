const prop=function(){
	let ip="127.0.0.1";
	// let ip="120.24.221.15";
	let port="5000";
	let DropDownList={
		orderstatus:[{key:"1",value:"待付款"},{key:"2",value:"待收货"},{key:"3",value:"待评价"},{key:"4",value:"售后"}],
		productstatus:[{1:"待付款"},{2:"待收货"},{3:"待评价"},{4:"售后"}]
	};
	return {
		"serviceIp":ip,
		// "serviceUrl":"http://"+ip+":"+port,
		"serviceUrl":"http://127.0.0.1:5000",
		// "serviceUrl":"http://admin.heshihuan.cn/api"
		"DropDownList":DropDownList
		}
}
var setting = {
			view: {
				addHoverDom: addHoverDom,
				removeHoverDom: removeHoverDom,
				selectedMulti: false
			},
			edit: {
				enable: true,
				editNameSelectAll: true,
				showRemoveBtn: showRemoveBtn,
				showRenameBtn: showRenameBtn
			},
			data: {
				simpleData: {
					enable: true
				}
			},
			callback: {
				beforeDrag: beforeDrag,
				beforeEditName: beforeEditName,
				beforeRemove: beforeRemove,
				beforeRename: beforeRename,
				onRemove: onRemove,
				onRename: onRename
			}
		};

// http://127.0.0.1:5000/common/model/queryAll/?modelName=Category_2
		var zNodes =[
			{ id:0, pId:0, name:"店铺类别", open:true},
			// { id:101, pId:0, name:"大类一"},
		];
		debugger
		$.get(prop().serviceUrl+"/common/model/queryAll/?modelName=Category",function(data,status){

			let category= JSON.parse(data);
			category=category.data
			for(let i=0;i<category.length;i++){
				category[i].id=category[i].cid;
				zNodes.push({ id:category[i].cid, pId:category[i].pid, name:category[i].name});
			}
			$.fn.zTree.init($("#treeDemo"), setting, zNodes);
			$("#selectAll").bind("click", selectAll);
		});
		var log, className = "dark";
		function beforeDrag(treeId, treeNodes) {
			return false;
		}
		function beforeEditName(treeId, treeNode) {
			className = (className === "dark" ? "":"dark");
			showLog("[ "+getTime()+" beforeEditName ]&nbsp;&nbsp;&nbsp;&nbsp; " + treeNode.name);
			var zTree = $.fn.zTree.getZTreeObj("treeDemo");
			zTree.selectNode(treeNode);
			setTimeout(function() {
				if (confirm("进入节点 -- " + treeNode.name + " 的编辑状态吗？")) {
					setTimeout(function() {
						zTree.editName(treeNode);
					}, 0);
				}
			}, 0);
			return false;
		}
		function beforeRemove(treeId, treeNode) {
			className = (className === "dark" ? "":"dark");
			showLog("[ "+getTime()+" beforeRemove ]&nbsp;&nbsp;&nbsp;&nbsp; " + treeNode.name);
			var zTree = $.fn.zTree.getZTreeObj("treeDemo");
			zTree.selectNode(treeNode);
			let r=confirm("确认删除 节点 -- " + treeNode.name + " 吗？")
			if(r){
				let node={};
				node.cid=treeNode.id;
				node.pid=treeNode.pId;
				node.name=treeNode.name;
				node.hasChild=treeNode.check_Child_State==0?true:false;
				console.info(node);
				debugger
				$.get(prop().serviceUrl+"/product/deleteCategory?pid="+node.pid+"&cid="+node.cid,function(data,status){

					product=data
					product= JSON.parse(product);
				});
			}
			return r;
		}
		function onRemove(e, treeId, treeNode) {
			showLog("[ "+getTime()+" onRemove ]&nbsp;&nbsp;&nbsp;&nbsp; " + treeNode.name);
		}
		function beforeRename(treeId, treeNode, newName, isCancel) {
			className = (className === "dark" ? "":"dark");
			showLog((isCancel ? "<span style='color:red'>":"") + "[ "+getTime()+" beforeRename ]&nbsp;&nbsp;&nbsp;&nbsp; " + treeNode.name + (isCancel ? "</span>":""));
			let node={};
			node.cid=treeNode.id;
			node.pid=treeNode.pId;
			node.name=newName;
			node.hasChild=treeNode.check_Child_State==0?true:false;
			console.info(node);
			$.get(prop().serviceUrl+"/product/add_update_category?node="+JSON.stringify(node),function(data,status){

				product=data
				product= JSON.parse(product);
			});

			// var zTree = $.fn.zTree.getZTreeObj("treeDemo");
			// var nodes = zTree.getNodes();
			// var nodes_=[]
			// for(let i=0;i<nodes.length;i++){
			// 	let node={}
			// 	node.cid=nodes[i].id;
			// 	node.pid=nodes[i].pId;
			// 	node.name=nodes[i].name;
			// 	node.hasChild=nodes[i].check_Child_State;
			// 	nodes_.push(node);
			// 	if(nodes[i].check_Child_State!=-1){
			// 		nodesChild=nodes[i].children;
			// 		for(let j=0;j<nodesChild.length;j++){
			// 			let node2={};
			// 			node2.cid=nodesChild[j].id;
			// 			node2.pid=nodesChild[j].pId;
			// 			node2.name=nodesChild[j].name;
			// 			node2.hasChild=nodesChild[j].check_Child_State;
			// 			nodes_.push(node2);

			// 			if(nodesChild[j].check_Child_State!=-1){
			// 				nodesChild2=nodesChild[j].children;
			// 				for(let k=0;k<nodesChild2.length;k++){
			// 					let node3={};
			// 					node3.cid=nodesChild2[k].id;
			// 					node3.pid=nodesChild2[k].pId;
			// 					node3.name=nodesChild2[k].name;
			// 					node3.hasChild=nodesChild2[k].check_Child_State;
			// 					nodes_.push(node3);
			// 					}
			// 			}

			// 			}
			// 	}
			// }



			console.info(newName)
			if (newName.length == 0) {
				setTimeout(function() {
					var zTree = $.fn.zTree.getZTreeObj("treeDemo");

					zTree.cancelEditName();
					alert("节点名称不能为空.");
				}, 0);
				return false;
			}
			return true;
		}
		function onRename(e, treeId, treeNode, isCancel) {
			showLog((isCancel ? "<span style='color:red'>":"") + "[ "+getTime()+" onRename ]&nbsp;&nbsp;&nbsp;&nbsp; " + treeNode.name + (isCancel ? "</span>":""));
		}
		function showRemoveBtn(treeId, treeNode) {
			return !treeNode.isFirstNode;
		}
		function showRenameBtn(treeId, treeNode) {
			// return !treeNode.isLastNode;
			return true;
		}
		function showLog(str) {
			if (!log) log = $("#log");
			log.append("<li class='"+className+"'>"+str+"</li>");
			if(log.children("li").length > 8) {
				log.get(0).removeChild(log.children("li")[0]);
			}
		}
		function getTime() {
			var now= new Date(),
			h=now.getHours(),
			m=now.getMinutes(),
			s=now.getSeconds(),
			ms=now.getMilliseconds();
			return (h+":"+m+":"+s+ " " +ms);
		}
		var newCount = 1;
		$.get(prop().serviceUrl+"/product/maxId",function(data,status){

			id= JSON.parse(data);
			newCount=id.data+1;
		});

		function addHoverDom(treeId, treeNode) {

			var sObj = $("#" + treeNode.tId + "_span");
			if (treeNode.editNameFlag || $("#addBtn_"+treeNode.tId).length>0) return;
			var addStr = "<span class='button add' id='addBtn_" + treeNode.tId
				+ "' title='add node' onfocus='this.blur();'></span>";
			sObj.after(addStr);
			var btn = $("#addBtn_"+treeNode.tId);
			if (btn) btn.bind("click", function(){


				var zTree = $.fn.zTree.getZTreeObj("treeDemo");

				var a=treeNode.level;
				if(a>1){
						alert("只需用到三级分类")
						return false;
				}
				// if(a!= null ){
				// var nodes = zTree.getNodes();
				// 	alert("只需用到二级分类")
				// 	return false;
				// }
				zTree.addNodes(treeNode, {id:(10 + newCount), pId:treeNode.id, name:"new node" + (newCount++)});


				return false;
			});
		};
		function removeHoverDom(treeId, treeNode) {
			$("#addBtn_"+treeNode.tId).unbind().remove();
		};
		function selectAll() {
			var zTree = $.fn.zTree.getZTreeObj("treeDemo");
			zTree.setting.edit.editNameSelectAll =  $("#selectAll").attr("checked");
		}

		$(document).ready(function(){
			$.fn.zTree.init($("#treeDemo"), setting, zNodes);
			$("#selectAll").bind("click", selectAll);
		});
