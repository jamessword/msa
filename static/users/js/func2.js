//发送验证码
window.onload=function () {
    function sendchangecode(val) {
        var newemail = $("#newemail").val();
        $.ajax({
           url: 'user/sendnewemailcode',
           type: 'get',
           data: {
               'newemail': newemail,
           },
           dataType: 'json',
       })
    };
    window.sendchangecode=sendchangecode;
}