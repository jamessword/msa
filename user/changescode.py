import smtplib
from random import Random
from email.mime.text import MIMEText
from email.utils import formataddr
from django.shortcuts import render
from MSA import models

from django.http import HttpResponse, JsonResponse

my_sender = '1370204344@qq.com'  # 发件人邮箱账号
my_pass = 'bxekvamkymarfjjj'  # 发件人邮箱密码


def mail(request):
    my_user = request.GET.get('newemail', '')  # 收件人邮箱账号，我这边发送给自己

    chars='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
    length=len(chars)-1
    random=Random()
    global str
    str = ''
    for i in range(6):
        str +=chars[random.randint(0,length)]

    try:
        msg = MIMEText('验证码为：'+str, 'plain', 'utf-8')
        msg['From'] = formataddr(["From your father", my_sender])    # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["my son", my_user])    # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "验证码"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)    # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)    # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())    # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()    # 关闭连接

    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print("验证码发送失败！")