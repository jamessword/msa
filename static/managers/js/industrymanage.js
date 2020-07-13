function mody() {

	var old=document.getElementById('oldname').value;
	var newmane= document.getElementById('newname').value;
	var descrip= document.getElementById('descrip').value;

	var span = document.getElementById("sp");
    $.get('/manager/mody',{'oldname':old,'newname' : newmane,'descrip' :descrip},  //发送数据
            function(r){
            if (r == '1'){
                alert(r);
                span.innerHTML="<font color='red' size='4'>修改成功</font>";
            }
            else{
                span.innerHTML="<font color='red' size='4'>修改失败</font>";
            }
            });
}


function addnew() {

	var old=document.getElementById('oldname').value;
	var newmane= document.getElementById('newname').value;
	var descrip= document.getElementById('descrip').value;
    var span = document.getElementById("sp");
    $.get('/manager/mody',{'oldname':old,'newname' : newmane,'descrip' :descrip},  //发送数据
            function(r){

            if (r =='2'){
                span.innerHTML="<font color='red' size='4'>添加成功</font>"
            }
            else{
                span.innerHTML="<font color='red' size='4'>添加失败</font>"
            }
            });
}

function del() {

	var old=document.getElementById('oldname').value;
	var newmane= document.getElementById('newname').value;
	var descrip= document.getElementById('descrip').value;
    var span = document.getElementById("sp");
    $.get('/manager/mody',{'oldname':old,'newname' : newmane,'descrip' :descrip},  //发送数据
            function(r){
            if (r == '3'){
                span.innerHTML="<font color='red' size='4'>删除成功</font>"
            }
            else{
                span.innerHTML="<font color='red' size='4'>删除失败</font>"
            }
            });
}