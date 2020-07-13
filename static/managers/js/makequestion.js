
var sentence=new Array();
var item=new Array();
var size=new Array();


function addb($this) {
    var len = $this.parent().prev().children().length + 1;
    var pid = $this.parent().parent().attr("id");
    var divId = pid + "b" + len;
    var inputId = pid + "input" + len;
    if (len >= 7) {
            alert("已经达到六个了");
        return;
    };
   $this.parent().prev().append("<div id=" + divId + ">"+len+":<input type='text' id=" + inputId + " style=\"border-radius: 5px;width:40%;font-size: 20px \"" +" ></br></div>");//选项
    ipid=parseInt(pid);
    size[ipid]=len;
};

function deleteb($this) {
    var len = $this.parent().prev().prev().children().length;
    $this.parent().prev().prev().children().eq(len-1).remove();
    var pid=$this.parent().parent().attr("id");
    ipid=parseInt(pid);
    size[ipid]=len-1;

};



function increasea($this) {
    var len = $this.parent().prev().children().length + 1;
    var divId =  len;
    var inputId = "input" + len;
    if (len >= 11) {
            alert("已经达到十个了");
        return;
    };//问题
    $(".bbbbb").append("<div  id=\""+len+"\">\n" +
        "                           <h6 class=\"m-0 font-weight-bold text-info:hover\" style='display: inline;position: relative;left: 10%'>问题"+len+"：</h6>\n" +
        "\t\t\t\t\t\t<input type=\"email\" class=\"form-control form-control-user\" id=\""+len+"t\" aria-describedby=\"emailHelp\" placeholder=\"问题"+len+"\" style=\"margin-top:5px;width:30%;display: inline;position: relative;left: 10%\">\n" +
        "\t\t\t\t\t\t<br/><br/>\n" +
        "\n" +
        "\n" +
        "                         <h6 class=\"m-0 font-weight-bold text-info:hover\" style=\"display: inline;position: relative;left: 15%\">选项</h6>\n" +
        "                            <div class=\"container\" style='position: relative;left: 15%;margin-bottom: 15px'>\n" +
        "\n" +
        "                                <div id=\""+len+"b1\">1:<input type=\"text\" id=\""+len+"input1\" name=\"1\" style='border-radius: 5px;width: 40%;font-size: 20px'><br/></div>\n" +
        "                            </div>\n" +
        "                            <div style=\"display: inline\">\n" +

        "<a href='#' class='btn btn-success btn-circle add' value='add' onclick='addb($(this))' style='position: relative;left: 15%'>\n"+
         "          <i class='fas fa-exclamation-triangle'></i>\n"+
         "    </a>\n"+

        "                            </div>\n" +
        "                              <div style=\"display: inline\">\n" +
        "<a href='#' class='btn btn-warning btn-circle del' value='del' onclick='deleteb($(this))' style='position: relative;left: 15%'>\n"+
         "          <i class='fas fa-exclamation-triangle'></i>\n"+
         "    </a>\n"+
        "      </div>\n" +
        "   </div>"
);
};

function minusa($this) {
    var len = $this.parent().prev().prev().children().length;

   $this.parent().prev().prev().children().eq(len-1).remove();
   size.pop();

}

function postthisques($this) {
    for (var i=1;i<size.length;i++){
        item[0]=$("#"+i+"t").val();
        for(var j=0;j<size[i];j++){
            var thisid=i+"input"+(j+1);
            item[j+1]=$("#"+thisid).val();
        }
        var itemstr=item.join(",");
        item=[];
        sentence[i]=itemstr;
    }
    var sentencestr=sentence.join("^");

    var questitle=$("#questitle").val();
    var startdate=$("#startdate").val();
    var enddate=$("#enddate").val();

    var span = document.getElementById("sp");
    $.get('/manager/postques', {'sentencestr':sentencestr,'questitle':questitle,'startdate':startdate,'enddate':enddate},  //发送数据
        function (r) {
            if(r=="ok"){
                span.innerHTML="<font color='green' size='4'>提交成功</font>";
            }
        });
}









