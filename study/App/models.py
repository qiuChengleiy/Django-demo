from django.db import models

# Create your models here.

# 年级表
class Grade(models.Model):
    name = models.CharField(max_length=32)


# 新建一个Sduent模型 - student表
class Student(models.Model):
    name = models.CharField(max_length=16) #设置字段名称
    age = models.IntegerField(default=1)
    grade_id = models.ForeignKey(Grade, on_delete=models.CASCADE) # 级联关系 2.0后定义外键和一对一的关系时要加上这个参数

