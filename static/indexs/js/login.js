//登录
//用户名的验证
function  log_in() {
    var username1 = document.getElementById("username1").value;
    var password1 = document.getElementById("password1").value;

    var span = document.getElementById("ddd");

    $.get('/login', {'username1': username1, 'password1': password1},
        function (r) {
            if (r == "false") {
                span.innerHTML = "<font color='red' size='4'>用户名或密码错误</font>"
            }
            else if(r=="yong"){
                window.location.href = "/gotomain1/";
            }
            else{
                window.location.href = "/gotomain2/";
            }
        })

}