//全选
var selected = 0;

$(".allselect").click(function(){
				//获取所有的checkbox
				var ches=$("input[name='yhselect']");
				//遍历所有的checkbox,重设选中状态为选中
            if(selected == 0)
				ches.each(function(){
					$(this).prop("checked",true);
					selected=1;
				});
            else
                ches.each(function(){
					$(this).prop("checked",false);
					selected=0;
				});
});

//注销
function cleanuser() {
	//获取所有的checkbox
	var ches=$("input[name='yhselect']");
	var list=new Array();
	//遍历所有checkbox
	ches.each(function () {
		if($(this).is(':checked')) {    //将被选中的checkbox的value（用户的id）放入list
			list.unshift($(this).attr("value"));
		}
    });
	var userlist=list.join(",");

	$.get('/manager/cleanuser', {'userlist':userlist},  //发送数据
        function (r) {
	        window.location.href="/manager/usermanage/";
        })
}


