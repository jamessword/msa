# Generated by Django 2.2.3 on 2019-07-08 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSA', '0005_auto_20190707_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='level',
            field=models.IntegerField(default=2, max_length=2),
        ),
    ]
