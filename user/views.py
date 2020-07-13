
from django.shortcuts import render
from django.http import HttpResponse
from MSA import models, views
from user import changescode
import json
from datetime import datetime, date
from itertools import chain


# Create your views here.

#跳转用户主页
def tomain1(request):
    name = request.session.get('username')
    context={'myname':name}
    return render(request, 'user/main1.html',context)

#跳转行业分析
def toanalyse(request):
    name = request.session.get('username')
    context = {'myname': name}
    results = models.IndustryInfo.objects.all()
    json_list = []
    for result in results:
        json_dict = {}
        json_dict['name'] = result.inname
        json_list.append(json_dict['name'])
        jdata = json_list
    return render(request, 'user/analyse.html', locals())

#跳转邮箱修改
def tochangemail(request):
    name = request.session.get('username')
    context = {'myname': name}
    return render(request, 'user/changemail.html',context)

#跳转完善信息
def toinfofulfil(request):
    name = request.session.get('username')
    context = {'myname': name}
    return render(request, 'user/infofulfil.html',context)

#跳转修改信息
def toinfomody(request):
    name = request.session.get('username')
    context = {'myname': name}
    return render(request, 'user/infomody.html',context)

#跳转修改密码
def tomodypswd(request):
    name = request.session.get('username')
    context = {'myname': name}
    return render(request, 'user/modypswd.html',context)


#！！！！！！！！！！！！！！！！！！！！！！修改信息
#修改用户信息
def mody(request):
    name = request.session.get('username')
    h = request.GET.get('newname', '')
    models.UserInfo.objects.filter(username=name).update(username=h)
    return render(request, 'user/main1.html')





#！！！！！！！！！！！！！！！！！！！！！！！！！修改邮箱
def checkcode(request):
    a = request.GET.get('cfcode', '')
    b = request.GET.get('oldemail', '')
    c = request.GET.get('emailpass', '')
    d = request.GET.get('newemail', '')
    name = request.session.get('username')
    resultset = models.UserInfo.objects.filter(username=name, email=b, password=c,level=2)

    if resultset:
        if a == changescode.str:
            models.UserInfo.objects.filter(username=name,level=2).update(email=d)
            data = {"result": "me"}
            return HttpResponse(json.dumps(data, ensure_ascii=False))
        else:
            data = {"result": "him"}
            return HttpResponse(json.dumps(data, ensure_ascii=False))
    else:
        data = {"result": "her"}
        return HttpResponse(json.dumps(data, ensure_ascii=False))



#！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！行业分析

def analysein(request):

    inname=request.GET.get('search','')
    reporttype=request.GET.get('sid','')
    if reporttype=="年":
        reporttype=1
    elif reporttype=="月":
        reporttype=2
    elif reporttype=="周":
        reporttype=3

    obj=models.Analyse.objects.filter(inname=inname,type=reporttype)
    list=[obj[0].id,obj[0].time,obj[0].inname,obj[0].conser,obj[0].d10,obj[0].d12,obj[0].d15,obj[0].d3,obj[0].d7,obj[0].nega,obj[0].posi,obj[0].sunega,obj[0].suposi,obj[0].type]
    liststr=','.join('%s'%id for id in list)
    return HttpResponse(liststr)






#！！！！！！！！！！！！！！！！！！！！！！！！！！修改密码
def trychangepass(request):
    a = request.GET.get('email', '')
    b = request.GET.get('changepass', '')
    c = request.GET.get('changepassagain', '')
    name = request.session.get('username')
    resultset=models.UserInfo.objects.filter(username=name, email=a,level=2)

    if resultset:
        if b==c:
            models.UserInfo.objects.filter(username=name,level=2).update(password=b)
            data = {"result":"1"}
            return HttpResponse(json.dumps(data,ensure_ascii=False))
        else:
            data = {"result": "2"}
            return HttpResponse(json.dumps(data, ensure_ascii=False))
    else:
        data = {"result": "3"}
        return HttpResponse(json.dumps(data, ensure_ascii=False))













#！！！！！！！！！！！！！！！！！！！！！！！！！！完善信息
def fulfil(request):
    a = request.GET.get('sex', '')
    b = request.GET.get('contact', '')
    c = request.GET.get('birth', '')
    d = request.GET.get('school', '')
    e = request.GET.get('company', '')
    f = request.GET.get('job', '')
    g = request.GET.get('country', '')
    h = request.GET.get('province', '')
    i = request.GET.get('city', '')
    j = request.GET.get('describe', '')
    name = request.session.get('username')
    models.UserInfo.objects.filter(username= name).update(sex=a, phone=b, birthday=c,school=d, company=e, job=f, address=g+h+i, describe=j)
    return render(request, 'user/infofulfil.html')











#！！！！！！！！我的关注

#查看我的关注
def tomycertain(request):
    myname = views.name
    myuid = models.UserInfo.objects.get(username=myname,level=2).id  # 得到用户id
    focus_objs = models.Focus.objects.filter(uid=myuid)  # 根据用户id找到关注的所有行业
    my_list = []  # 结果的序列集
    for focus_obj in focus_objs:
        myindid = focus_obj.indid  # 每一个行业的id
        indus_obj = models.IndustryInfo.objects.filter(id=myindid)  # 根据每一个行业的id找到IndustryInfo中的记录
        my_dict = {}  # Queryset转成字典
        my_dict["id"] = indus_obj[0].id
        my_dict["inname"] = indus_obj[0].inname
        my_dict["description"] = indus_obj[0].description
        my_list.append(my_dict)  # 将每一个字典加入序列集
    return render(request, 'user/mycertain.html', locals())

#删除关注
def deletein(request,myindid):
    name = request.session.get('username')
    myuid = models.UserInfo.objects.get(username=name,level=2).id   #得到用户id
    models.Focus.objects.get(uid=myuid,indid=myindid).delete()

    focus_objs = models.Focus.objects.filter(uid=myuid)  # 根据用户id找到关注的所有行业
    my_list = []  # 结果的序列集
    for focus_obj in focus_objs:
        myindid = focus_obj.indid  # 每一个行业的id
        indus_obj = models.IndustryInfo.objects.filter(id=myindid)  # 根据每一个行业的id找到IndustryInfo中的记录
        my_dict = {}  # Queryset转成字典
        my_dict["id"] = indus_obj[0].id
        my_dict["inname"] = indus_obj[0].inname
        my_dict["description"] = indus_obj[0].description
        my_list.append(my_dict)  # 将每一个字典加入序列集

    return render(request,'user/mycertain.html/',locals())

#详细信息
def getininfo(request,myinname):
    in_obj = models.IndustryInfo.objects.get(inname=myinname,level=2)
    in_id=in_obj.id
    return render(request,'user/analyse.html',locals())



    






#！！！！！！！填写问卷

#加载所有问卷
def toquestion(request):
    ques_objs = models.Paper.objects.filter(done=0)
    my_list = []
    thisdate=date.today()
    #thisdatestr=datetime.strftime(thisdate,'%Y-%m-%d')
    for ques_obj in ques_objs:
        my_dict = {}
        my_dict["id"] = ques_obj.id
        my_dict["title"] = ques_obj.pname
        timefrom=ques_obj.startime
        timeto=ques_obj.deadline
        if thisdate>timeto:
            ques_obj.done=1
            ques_obj.save()
            continue
        my_dict["time"] = datetime.strftime(timefrom,'%Y-%m-%d') + " 至 " + datetime.strftime(timeto,'%Y-%m-%d')
        m_id= ques_obj.mid
        m_name=models.UserInfo.objects.get(level=0,id=m_id).username
        my_dict["creator"]=m_name
        my_list.append(my_dict)
    return render(request, 'user/question.html',locals())

#填写问卷(传)

def writeques(request):
    return render(request, 'user/write.html')
#填写问卷（收）
#def storeques(request):













#！！！！！！！！！！！！！！！！！修改信息
#修改用户名
def changeusername(request):
    mynewname=request.GET.get('username','')
    name = request.session.get('username')
    obj=models.UserInfo.objects.get(username=name,level=2)
    obj.username=mynewname
    obj.save()
    views.name=mynewname
    return render(request,'user/infomody.html',locals())