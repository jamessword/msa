from django.shortcuts import render
from django.http import HttpResponse
from MSA import models, views
from datetime import datetime, date, timedelta

# Create your views here.
#跳转到管理员主页
def tomain2(request):
    name = request.session.get('username')
    context = {'myname': name}
    objs = models.Board.objects.all().order_by('-time')
    obj = objs[0]
    content = obj.content
    return render(request, 'manager/main2.html', locals())

#跳转行业管理
def toindustrymanage(request):
    name = request.session.get('username')
    context = {'myname': name}
    return render(request , 'manager/industrymanage.html', context)

#跳转发布公告界面
def tomodmody(request):
    name = request.session.get('username')
    context = {'myname': name}
    return render(request , 'manager/modmody.html', context)

#跳转发布问卷界面
def toquestionpost(request):
    name = request.session.get('username')
    context = {'myname': name}
    return render(request , 'manager/questionpost.html',context)

#跳转存储管理界面
def tostoremanage(request):
    name = request.session.get('username')
    context = {'myname': name}
    return render(request, 'manager/storemanage.html', locals())









#!!!!!!!!!!!!!!!!!!!!!!!!!!!!! usermanage.html
#加载
def tousermanage(request):
    user_objs=models.UserInfo.objects.exclude(level=0)[:100]
    my_list = []
    for obj in user_objs:
        my_dict = {}
        my_dict["id"]=obj.id
        my_dict["username"] = obj.username
        quanxian = obj.level
        if quanxian == 2:
            my_dict["level"] = "普通用户"
        elif quanxian == 1:
            my_dict["level"] = "会员"
        my_dict["email"] = obj.email
        my_list.append(my_dict)
    return render(request , 'manager/usermanage.html', locals())


#搜索
def searchuser(request):
    thisusername=request.GET.get('username','')
    thislevel=request.GET.get('level','')
    thissex=request.GET.get('sex','')

    if thislevel=="普通用户":
        thislevel=2
    else:
        thislevel=1
    if thisusername==None:
        user_objs=models.UserInfo.objects.filter(sex=thissex,level=thislevel)
    else:
        user_objs=models.UserInfo.objects.filter(username=thisusername,sex=thissex,level=thislevel)
        my_list=[]
        for obj in user_objs:
            my_dict={}
            my_dict["username"]=obj.username
            quanxian=obj.level
            if quanxian==2:
                my_dict["level"]="普通用户"
            elif quanxian==1:
                my_dict["level"]="会员"
            my_dict["eamil"]=obj.email
            my_list.append(my_dict)
    return render(request , 'manager/usermanage.html', locals())

#删除用户
def deleteuser(request):
    name = request.session.get('username')
    context = {'myname': name}
    bb=request.GET.get('userlist','')
    aa=bb.split(",")
    for index in range(len(aa)):
        models.UserInfo.objects.filter(id=aa[index]).delete()
    return render(request, 'manager/usermanage.html', context)


#修改用户信息
def changinfo(request):
    name = request.session.get('username')
    context = {'myname': name}
    usernameold = request.GET.get('usernameold', '')
    usernamenew = request.GET.get('usernamenew', '')
    level = request.GET.get('level', '')
    email = request.GET.get('email', '')
    models.UserInfo.objects.filter(username=usernameold).update(username=usernamenew,level=level,email=email)
    return render(request, 'manager/usermanage.html', context)


###########################################
def moduserinfo(request,aa,b):
    name = request.session.get('username')
    context = {'myname': name}
    for index in range(len(aa)):
        models.UserInfo.objects.filter(username=aa[index]).update(level=b)
    return render(request, 'manager/usermanage.html', context)









#！！！！！！！！！！！！！！！！！！！！！！industrymanage.html
#行业管理
def manageindus(request):
    a = request.GET.get('oldname', '')
    b = request.GET.get('newname', '')
    c = request.GET.get('descrip', '')

    if a != '':

        if b != '':
            d = models.IndustryInfo.objects.filter(inname=a).exists()
            if d:
                models.IndustryInfo.objects.filter(inname=a).update(inname=b, description=c)

                return HttpResponse('1')

            else:
                return HttpResponse('4')

        else:
            d = models.IndustryInfo.objects.filter(inname=a).exists()
            if d:
                models.IndustryInfo.objects.filter(inname=a).delete()
                return HttpResponse('3')
            else:
                return HttpResponse('4')

    else:

        if b != '':
            d = models.IndustryInfo.objects.filter(inname=b).exists()
            if d:
                return HttpResponse('4')
            else:
                models.IndustryInfo.objects.create(inname=b, description=c)
                return HttpResponse('2')
        else:
            return HttpResponse('4')











#！！！！！！！！！！！！！！！！！！！！！！modmody.html
#发布公告
def postboard(request):
    context=request.GET.get('postcontext','')
    m_name = request.session.get('username')
    m_id=models.UserInfo.objects.get(username=m_name,level=0).id
    time=datetime.now()
    models.Board.objects.create(time=time, mid=m_id, content=context)
    return HttpResponse('1')







#！！！！！！！！！！！！！！！storemanage.html
#存储管理，按需清空本地空间
def storagechange(request):
    x = request.GET.get('paperstyle', '')
    y = request.GET.get('numberselect', '')
    z = request.GET.get('datestyle', '')
    if x=="年报":
        x=1
    elif x=="月报":
        x=2
    elif x=="周报":
        x=3

    if z=="周":
        thatday=date.today()-timedelta(weeks=int(y))
    elif z=="月":
        thisday=date.today()
        thismonth=thisday.month
        if thismonth>int(y):
            thatday=str(thisday.year)+"-"+str(thismonth-int(y))+"-"+str(thisday.day)
        else:
            thatday=str(thisday.year-1)+"-"+str(thismonth+12-int(y))+"-"+str(thisday.day)
        thatday=datetime.strptime(thatday,'%Y-%m-%d')
    elif z=="年":
        thisday = date.today()
        thatday = str(thisday.year-int(y)) + "-" + str(thisday.year-int(y)) + "-" + str(thisday.day)
        thatday = datetime.strptime(thatday, '%Y-%m-%d')
    models.Analyse.objects.filter(type=x,time__lt=thatday).delete()

    return HttpResponse()










#！！！！！！！！！！！！！！！！！！！！！storemanage.html存储管理
#存储问卷
def storeques(request):
    pname=request.GET.get('questitle','')
    startime=request.GET.get('startdate','')
    deadtime=request.GET.get('enddate','')
    m_name=request.session.get('username')
    m_id=models.UserInfo.objects.filter(username=m_name)[0].id
    p_id=models.Paper.objects.create(pname=pname,startime=startime,deadline=deadtime,mid=m_id).id

    aa=request.GET.get('sentencestr','')
    bb=aa.split("^")
    del bb[0]
    for indexs in range(len(bb)):
        bb[indexs]=bb[indexs].split(",")
    for item in bb:
        title=item[0]
        del item[0]
        items=[None]*6
        for index in range(len(item)):
            items[index]=item[index]
        models.Question.objects.create(type=1, title=title, pid=p_id,A=items[0],B=items[1],C=items[2],D=items[3],E=items[4],F=items[5])
    return HttpResponse("ok")





#！！！！！！！！！！！！！！！！！！！！！！！！questionpast.html历史问卷
#加载
def toquestionpast(request):
    ques_objs = models.Paper.objects.all()[:100]
    my_list = []
    thisdate=date.today()
    for obj in ques_objs:
        my_dict = {}
        my_dict["ID"] = obj.id
        my_dict["pname"]=obj.pname
        timefrom = obj.startime
        timeto = obj.deadline
        if obj.done==0:
            if thisdate>timeto:
                obj.done=1
                obj.save()
            else:
                continue
        my_dict["time"] = datetime.strftime(timefrom, '%Y-%m-%d') + " 至 " + datetime.strftime(timeto, '%Y-%m-%d')
        m_id = obj.mid
        m_name = models.UserInfo.objects.get(level=0, id=m_id).username
        my_dict["creator"] = m_name
        my_list.append(my_dict)
    return render(request, 'manager/questionpast.html',locals())


#搜索
def searchquestion(request):
    name = request.session.get('username')
    context = {'myname': name}
    thisquesid=request.GET.get('questionid','')
    thisstatime=request.GET.get('startdate','')
    thisdeatime=request.GET.get('enddate','')
    if thisquesid:
        if thisstatime:
            if thisdeatime:
                ques_objs=models.Paper.objects.filter(id=thisquesid,startime__gte=thisstatime,deadline__lte=thisdeatime)
            else:
                ques_objs = models.Paper.objects.filter(id=thisquesid, startime__gte=thisstatime)
        elif thisdeatime:
            ques_objs = models.Paper.objects.filter(id=thisquesid,deadline__lte=thisdeatime)
        else:
            ques_objs = models.Paper.objects.filter(id=thisquesid)
    else:
        ques_objs = models.Paper.objects.all()

    my_list = []
    for obj in ques_objs:
        my_dict = {}
        my_dict["ID"] = obj.id
        my_dict["pname"] = obj.pname
        timefrom = obj.startime
        timeto = obj.deadline
        my_dict["time"] = datetime.strftime(timefrom, '%Y-%m-%d') + " 至 " + datetime.strftime(timeto, '%Y-%m-%d')
        m_id = obj.mid
        m_name = models.UserInfo.objects.get(level=1, id=m_id).username
        my_dict["creator"] = m_name
        my_list.append(my_dict)
        my_list.append(my_dict)
    return render(request, 'manager/questionpast.html', locals())



#问卷详情
def checkques(request):
    return render(request, 'manager/check.html')

