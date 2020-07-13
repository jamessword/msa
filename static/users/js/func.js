

//修改邮箱
function changemail() {
    var cfcode
       = document.getElementById("cfcode").value
    var oldemail
       = document.getElementById("oldemail").value
    var emailpass
       = document.getElementById("emailpass").value
    var newemail
       = document. getElementById("newemail").value

    var span1 = document.getElementById("dn")
    var span2 = document.getElementById("sn")
    var span3 = document.getElementById("zn")

        //判断信息是否正确
        $.get('/user/checkemailcode/',{'cfcode':cfcode, 'oldemail':oldemail, 'emailpass':emailpass,'newemail':newemail},
            function(data){
            alert(data.result)
            if (data.result == "her"){
                alert(data.result)
                span1.innerHTML="<font color='red' size='4'>原邮箱或密码错误</font>"
                span2.innerHTML="<font color='red' size='4'></font>"
            }
            else if(data.result == "him"){
                alert(data.result)
                span1.innerHTML="<font color='red' size='4'></font>"
                span2.innerHTML="<font color='red' size='4'>验证码错误</font>"
            }
            else{
                alert(data.result)
                span1.innerHTML="<font color='red' size='4'></font>"
                span2.innerHTML="<font color='red' size='4'></font>"
                span3.innerHTML="<font color='red' size='4'>修改成功</font>"
            }
            })
}



//实时监测第二次密码的一致性
function checktwopass(){
    var changepass
       = document.getElementById("changepass").value
    var changepassagain
       = document.getElementById("changepassagain").value

    var span2 = document.getElementById("sn")

    if ( changepass != changepassagain){
        span.innerHTML="<font color='red' size='4'>两次密码不一致</font>"
    }
    else{
        span.innerHTML="<font color='red' size='4'>一致</font>"
    }
}



function changepass() {
    var email
       = document.getElementById("email").value
    var changepass
       = document.getElementById("changepass").value
    var changepassagain
       = document.getElementById("changepassagain").value

    var span1 = document.getElementById("dn")
    var span2 = document.getElementById("sn")
    var span3 = document.getElementById("zn")

        //判断信息是否正确
        $.get('/user/changepassfunc',{'email':email, 'changepass':changepass, 'changepassagain':changepassagain},
            function(data){
            if (data.result == "1"){
                span1.innerHTML="<font color='red' size='4'></font>"
                span2.innerHTML="<font color='red' size='4'></font>"
                span3.innerHTML="<font color='red' size='4'>修改成功</font>"
            }
            else if(data.result=="2"){
                span1.innerHTML="<font color='red' size='4'></font>"
                span2.innerHTML="<font color='red' size='4'>两次密码不一致</font>"
                span3.innerHTML="<font color='red' size='4'></font>"
            }
            else{
                span1.innerHTML="<font color='red' size='4'>修改成功</font>"
                span2.innerHTML="<font color='red' size='4'></font>"
                span3.innerHTML="<font color='red' size='4'></font>"
            }
            })
}

window.onload=function () {
    function Infofulfil(val) {
        var sex = $("input[name='sex']:checked").val();
        var contact = $("#contact").val();
        var birth= $("#birth").val();
        var school= $("#school").val();
        var company= $("#company").val();
        var job= $("#job").find("option:selected").text()
        var country= $("#country").find("option:selected").text()
        var province= $("#province").find("option:selected").text()
        var city= $("#city").find("option:selected").text()

        var describe= $("#describe").val();


        $.ajax({
           url: '/user/Infofulfilfunc/',
           type: 'get',
           data: {
               'sex' : sex,
               'contact' : contact,
               'birth' : birth,
               'school' : school,
               'company' : company,
               'job' : job,
               'country' : country,
               'province' : province,
               'city' : city,
               'describe' : describe
           },
           dataType: 'json',
       })
    };
    window.Infofulfil=Infofulfil;
}


//行业分析
var thisintitle;
var arr= new Array();
var heng=new Array();
var bheng=new Array();
var thislist;

function industryanalyse() {
    var search = document.getElementById("search").value;
    var sid= document.getElementById("sid").value;
    $.get('/user/analyseinfun',{ 'search': search, 'sid':sid },
        function (data) {
            thislist=data.split(",");
            thisintitle=thislist[2];

            if(thislist[13]==1){
                heng=['Month1', 'Month3', 'Month6', 'Month9', 'Month12'];
            }
            else if(thislist[13]==2){
                heng=['Day5', 'Day10', 'Day15', 'Day20', 'Day30'];
            }
            else{
                heng=['Day3', 'Day7', 'Day10', 'Day12', 'Day15'];
            }

            arr=[thislist[7],thislist[8],thislist[4],thislist[5],thislist[6]];
            bheng=['保守', '积极', '较积极', '消极', '较消极'];
            //window.location.href="/user/analyse/";
        })
}