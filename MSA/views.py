from django.shortcuts import render
from MSA import models, views
from django.http import HttpResponse
from MSA import verifycode
import json

from tkinter import messagebox

# Create your views here.




#跳转主页
def toindex(request):
    return render(request, 'index/index.html')

#登录
def login(request):
    global name
    request.session['username'] = request.POST.get('username1', '')
    pwd = request.GET.get('password1', '')
    name = request.GET.get('username1','')
    context = {'myname': name}
    if name.find('@') != -1:
        resultset = models.UserInfo.objects.filter(email= name, password= pwd)
        if resultset:
                if resultset[0].level== 0:
                    return render(request, 'manager/main2.html', context)
                else:
                    return render(request, 'user/main1.html', context)
        else:
            return HttpResponse('1')
            # 报错
    else:
        resultset = models.UserInfo.objects.filter(username=name, password=pwd)
        if resultset:
            if resultset[0].level == 0:
                return HttpResponse('guan')         #跳转管理员主页
            else:
                return HttpResponse('yong')         #跳转用户主页
        else:
            return HttpResponse("false")            #用户不存在，报错提示

#跳转用户主页函数
def gotomain1(request):
    return render(request,'user/main1.html')
#跳转管理员主页函数
def gotomain2(request):
    return  render(request,'manager/main2.html')

#新人注册（注册格式限制在js中实现）
def register(request):
    a = request.GET.get('username2', '')
    b = request.GET.get('password2', '')
    c = request.GET.get('email2', '')
    d = request.GET.get('vfcode', '')

    if d == verifycode.str:
        models.UserInfo.objects.create(username= a, password= b, email= c)
        data = {"result":"ok"}
        return  render(request,'index/index.html',data)
    else:
        data = {"result": "false"}
        return HttpResponse(json.dumps(data, ensure_ascii=False))


#注册时，判断用户名是否已存在
def checkName(request):
    name = request.GET.get("username2")
    #到数据库中进行查询
    resultset = models.UserInfo.objects.filter(username=name)
    if resultset:
        return HttpResponse('false')
    else:
        return HttpResponse('ok')
