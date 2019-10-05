from django.db import models

# Create your models here.

# 新建一个Sduent模型 - student表
class Student(models.Model):
    name = models.CharField(max_length=16) #设置字段名称
    age = models.IntegerField(default=1)



