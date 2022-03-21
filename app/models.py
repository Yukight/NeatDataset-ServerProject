from email.headerregistry import Address
from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField('记录编号', primary_key = True)
    userName = models.CharField('用户账号', db_column='user_name', max_length=32, null=False)
    passWord = models.CharField('用户密码', max_length=32, null=False)
    name = models.CharField('用户姓名', max_length=20, null=False)
    gender = models.CharField('用户性别', max_length=4, null=False)
    age = models.IntegerField('用户年龄', null=False)
    phone = models.CharField('联系电话', max_length=20, null=False)
    email = models.CharField('电子邮箱', max_length=32, null=False)
    type = models.CharField('用户身份', null=False)
    class Meta:
        db_table = 'users'

class Notices(models.Model):
    id = models.AutoField('记录编号', primary_key=True)
    title = models.CharField('通知标题', max_length=32, null=False)
    detail = models.AutoField('通知详情',  max_length=125, null=False)
    creatTime = models.AutoField('通知时间',  db_column='create_time', max_lenth=19)
    class Meta:
        db_table = 'notices'