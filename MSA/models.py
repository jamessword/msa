from django.db import models

# Create your models here.

#用户信息表（基本信息）
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    sex = models.CharField(max_length=32, default=None,null= True)
    phone = models.CharField(max_length=32, default=None,null= True)
    birthday = models.CharField(max_length=20, default=None,null= True)
    school = models.CharField(max_length=20, default=None,null= True)
    company = models.CharField(max_length=20, default=None,null= True)
    job = models.CharField(max_length=20, default=None,null= True)
    address = models.TextField(max_length=50, default=None,null= True)
    describe = models.TextField(max_length=200, default=None,null= True)
    level = models.IntegerField(default=2, null= False)

#行业信息表
class IndustryInfo(models.Model):
    inname = models.CharField(max_length=32)
    description = models.CharField(max_length=200, default=None, null=True)

#用户关注
class Focus(models.Model):
    uid = models.IntegerField(null=False)
    indid = models.IntegerField(null=False)

#题库
class Question(models.Model):
    type = models.IntegerField(null=False, default=1)
    title = models.CharField(max_length=32,null=False)
    A = models.CharField(max_length=32, default=None,null=True)
    B = models.CharField(max_length=32, default=None, null=True)
    C = models.CharField(max_length=32, default=None, null=True)
    D = models.CharField(max_length=32, default=None, null=True)
    E = models.CharField(max_length=32, default=None, null=True)
    F = models.CharField(max_length=32, default=None, null=True)
    pid = models.IntegerField(null=False)

#问卷信息
class Paper(models.Model):
    pname = models.CharField(max_length=32,null=False)
    startime = models.DateField(null=False)
    deadline = models.DateField(null=False)
    done = models.IntegerField(default=0,null=False)
    mid = models.IntegerField(null=False)

#问卷调查结果
class Questionfill(models.Model):
    uid = models.IntegerField(null=False)
    time = models.TimeField(null=False)
    qid = models.IntegerField(null=False)
    answer=models.CharField(max_length=200,null=False)

#管理员的公告发布
class Board(models.Model):
    time = models.DateTimeField(null= False)
    content = models.CharField(max_length=255)
    mid = models.IntegerField(null= False)

#市场分析表（数据来源于爬虫）
class Analyse(models.Model):
    id = models.IntegerField(null=False, primary_key= True)
    time = models.DateField(max_length=32)
    inname = models.CharField(max_length=32)
    suposi = models.IntegerField(null=False, default=0)
    posi = models.IntegerField(null=False, default=0)
    conser = models.IntegerField(null=False, default=0)
    nega = models.IntegerField(null=False, default=0)
    sunega = models.IntegerField(null=False, default=0)
    d3 = models.FloatField(null=False, default=0)
    d7 = models.FloatField(null=False, default=0)
    d10 = models.FloatField(null=False, default=0)
    d12 = models.FloatField(null=False, default=0)
    d15 = models.FloatField(null=False, default=0)
    type = models.FloatField(null=False,default=1)
