"""MSA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.conf.urls import include
from . import views, verifycode

urlpatterns = [
    # re_path('index/' , views.login ),
    path('', views.toindex , name='index'),
    path('checkName/', views.checkName),
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('verifycode', verifycode.mail, name='verifycode'),
    path('user/', include('user.urls')),
    path('manager/', include('manager.urls')),
    path('gotomain1/', views.gotomain1),
    path('gotomain2/', views.gotomain2),
]
