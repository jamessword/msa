function postboard() {
    var postcontext = document.getElementById("boardpost").value;
    var span = document.getElementById("sp");
    $.get('/manager/postboard', {'postcontext':postcontext},
        function (r) {
        if (r =='1'){
            span.innerHTML="<font color='red' size='4'>提交成功</font>";
        }
        else {
            span.innerHTML="<font color='red' size='4'>提交失败</font>";
        }
        })
}

//存储管理
window.onload=function () {
    function storemanage(val) {

        var paperstyle= $("#paperstyle").find("option:selected").text();
        var numberselect= $("#numberselect").find("option:selected").text();
        var datestyle= $("#datestyle").find("option:selected").text();
        $.ajax({
           url: '/manager/storemanagefunc/',
           type: 'get',
           data: {
               'paperstyle' :  paperstyle,
               'numberselect' : numberselect,
               'datestyle' : datestyle,

           },
           dataType: 'json',
       })
    };
    window.storemanage=storemanage;
}