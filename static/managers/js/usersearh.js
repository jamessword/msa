//搜索
function searchuser() {
	var username =$("#username").val();
	var level = $("#userlevel").find("option:selected").text();
	var sex = $("#usersex").find("option:selected").text();
	$.get('/manager/usersearh', {'username':username, 'level':level, 'sex':sex },  //发送数据
        function (r) {
		alert('tiaoshi');
	        window.location.href="/manager/usermanage/";
        });
}


//搜索
function searchquestion() {
    var questionid =$('#quebiaohao').val;
    var date1=document.getElementById("startdate");
    var startdate =date1.value;
	//var startdate =$("#startdate").val;
	//var enddate = $("#enddate").val;
	$.get('/manager/questionsearh', {'questionid':questionid, 'startdate':startdate, 'enddate':enddate },  //发送数据
        function (r) {
		alert('tiaoshi');
	        window.location.href="/manager/questionpast/";
        });
}

//修改用户信息
function changinfo(){
	//var usernameold =获取选中的一个用户
	var username =$('#usernamec').val;
	var levelstr = $('#levelc').val;
	var level;
	if (levelstr=='普通用户'){
		level=2
	}
	else if(levelstr=='会员'){
		level=1
	}
	var email = $('#emailc').val;
	$.get('/manager/changinfo',{'usernameold':usernameold, 'usernamenew':username, 'level':level,'email':email},
		function (r) {
			alert('修改成功');
			window.location.href="/manager/usermanage/"
        })
}