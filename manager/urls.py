from django.urls import path ,re_path
from . import views

urlpatterns=[
    re_path('main2/$', views.tomain2, name='main2'),
    re_path('industrymanage/$', views.toindustrymanage, name='industrymanage'),
    re_path('modmody/', views.tomodmody, name='modmody'),
    re_path('questionpost/$', views.toquestionpost, name='questionpost'),
    re_path('questionpast/$', views.toquestionpast, name='questionpast'),
    re_path('storemanage/$', views.tostoremanage, name='storemanage'),
    re_path('usermanage/$', views.tousermanage, name='usermanage'),
    re_path(r'^postboard',views.postboard,name='postboard'),
    re_path('cleanuser',views.deleteuser),
    re_path('mody', views.manageindus),
    re_path(r'^postboard', views.postboard, name='postboard'),
    re_path('checkques', views.checkques, name='checkques'),
    re_path('storemanagefunc/',views.storagechange,name='storemanagefunc'),
    re_path('usersearh', views.searchuser, name='usersearh'),
    re_path('questionsearh', views.searchquestion, name='questionsearh'),
    re_path('changinfo', views.changinfo, name='changinfo'),
    re_path(r'^mouser/(.+)/$',views.changinfo,name='mouser'),
    re_path('postques',views.storeques,name='postques'),
]

