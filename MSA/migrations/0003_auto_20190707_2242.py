# Generated by Django 2.2.3 on 2019-07-07 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSA', '0002_auto_20190707_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='company',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='describe',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='job',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='school',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='sex',
        ),
    ]
