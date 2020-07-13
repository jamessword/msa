
window.onload=function () {
    function sendcode(val) {
        var email2 = $("#email2").val();
        $.ajax({
           url: 'verifycode',
           type: 'get',
           data: {
               'email2': email2,
           },
           dataType: 'json',
       })
    };
    window.sendcode=sendcode;
}



var name_flag=false
var pwd_flag = false

//用户名的验证
function  checkName() {
    var name
       = document.getElementById("Your Name").value
    var span = document.getElementById("sp")
    if(name.length<6){//长度小于6位，不能注册
     span.innerHTML=
    "<font color='red' size='4'>长度不能小于6位</font>"
        name_flag=false
    }else{
        //判断用户名是否存在，通过异步请求
        // name_flag=true;
        //var url="/checkName?uname="+name
        $.get('/checkName/',{'username2':name},
            function(r){
            if (r=="ok"){
                name_flag=true;
               span.innerHTML="<font color='green' size='4'>可以注册</font>"
            }else{
                name_flag=false;
                span.innerHTML="<font color='red' size='4'>用户名已存在，不能注册</font>"
            }
            });

    }

}


//密码的验证
function  checkPwd() {
    var pwd =
     document.getElementById("upwd").value
     var p=
     new RegExp("([0-9]{1,}|[a-zA-Z]{1,}){6,}");
     pwd_flag = p.test(pwd)


}
//验证用户名和密码
function  checkAll() {


   if(name_flag==true &&pwd_flag==true){
       return true
   }else{
       return false
   }
}
//注册-》登录
function signup() {
    var username
        = document.getElementById("Your Name").value;
    var password
        = document.getElementById("Password2").value;
    var email
        = document.getElementById("email2").value;
    var vfcode
       = document.getElementById("vfcode").value;
    var span = document.getElementById("sn");
        //ajaxSettings.async =false
        //判断用户名验证码是否正确
        $.get('/register/',{ 'username2': username, 'password2':password, 'email2':email , 'vfcode':vfcode},
            function(data){
            if (data.result=="false"){
                span.innerHTML="<font color='red' size='4'>验证码错误</font>"
                //清空

            }
            else{
                span.innerHTML="<font color='red' size='4'>验证码正确</font>";

                    document.getElementById("username1").value = username;
                    document.getElementById("password1").value = password;

            }
            })

    $('#close2').trigger('click');
    $('#modal-register').modal('show');

}
function re() {
    return false
}



