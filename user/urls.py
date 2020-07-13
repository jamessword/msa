from django.urls import path ,re_path
from user import views, changescode

urlpatterns=[
    re_path('main1/$', views.tomain1, name='main1'),
    re_path('analyse/$', views.toanalyse, name='analyse'),
    re_path('changemail/$', views.tochangemail, name='changemail'),
    re_path('infofulfil/$', views.toinfofulfil, name='infofulfil'),
    re_path('infomody/$', views.toinfomody, name='infomody'),
    re_path('modypswd/$', views.tomodypswd, name='modypswd'),
    re_path('mycertain/$', views.tomycertain, name='mycertain'),
    re_path('question/$', views.toquestion, name='question'),
    re_path('sendnewemailcode', changescode.mail, name='sendnewemailcode'),
    re_path('checkemailcode', views.checkcode,name='checkemailcode'),
    re_path('changepassfunc',views.trychangepass,name='changepassfunc'),
    re_path('Infofulfilfunc', views.fulfil, name='Infofulfilfunc'),
    re_path('Infomodyfunc', views.mody, name='Infomodyfunc'),
    re_path(r'^deleteitfunc/(.+)/$', views.deletein, name='deleteitfunc'),
    re_path(r'^intoofunc/(.+)/$', views.getininfo, name='intoofunc'),
    re_path(r'^writeques/',views.writeques,name='writeques'),
    re_path('analyseinfun', views.analysein, name='analyseinfun'),
]