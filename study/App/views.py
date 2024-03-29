from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

import random

# 导入模型
from App.models import Student,Grade

# Create your views here.
def hello(request):
    return HttpResponse('可还行') # 直接响应 - 也可以是html字符串 返回给浏览器会直接渲染

def index(request):
    return render(request, "index.html") # 渲染模板文件 --- App/templates
    #return render(request, "hello.html")  # 渲染模板文件 --- /templates   根目录 -- 但是要在settings里注册
    
    # 这个过程其实是处理好的html字符串返回给客户端
    # 利用loader.get_template('index.html').render(context=context)

# 新增用户数据
def addStudent(request):
    students = Student()
    students.name = 'tom %d' % random.randrange(90)
    students.save()

    return HttpResponse('success %s' % students.name)

# 获取学生数
def getStudent(request):
    students = Student.objects.all()
    # 返回json序列化
    str_students = serializers.serialize("json", students)

    #return HttpResponse(str_students
    # 模板返回值
    # return render(request, 'contexts.html', context = { "name": "xiaoming", "age": 12 })
    # 渲染列表
    return render(request, 'list.html', context = { "students": students})

# 更新学生数据
def updateStudent(req):
    # 先查后保存
    student = Student.objects.get(id=1)
    student.name = 'test_update_name'
    student.save()

    return HttpResponse('update success')


# 删除学生数据
def deleteStudent(req):
    student = Student.objects.get(id=1)
    student.delete()

    return HttpResponse('delete success')


# 外键查询
def getGradeName(req):
    student = Student.objects.get(id=3)
    grade = student.grade_id
    print(grade.name) # 二年级 关联到了grade表

    return HttpResponse(req)

# 通过外键查询所有学生名单
def getStudentsName(req):
    # 先查年级
    grade = Grade.objects.get(name='一年级')
    students = grade.student_set.all()

    return render(req, 'student.html', context={ 'students': students })

    