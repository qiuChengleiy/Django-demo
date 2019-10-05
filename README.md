# Django-demo
Django框架学习， 采坑记录

## Django简介

Django是一个用python编写的web框架（MVC架构）版本标有LTS： 长期支持版本

#####  1.MVC设计模式

一种设计模式，用业务逻辑使数据、界面显示分离的方法组织代码，将业务逻辑聚集到一个部件上，在改进和个性化界面与用户交互的同时不需要重新编写业务逻辑。（M:model   V:view C:controller)

- 核心思想： 解耦(更好从组织代码，1个文件拆成5个文件，可以分摊风险)

- 优点： 降低各模块之间的耦合性，方便变更，更容易重构代码，最大程度实现了代码的重用

  

##### 2.MVT设计模式（Django）

本质上和mvc差不多，也是各组件之间为了保持松耦合关系，只是定义不同

- Model: 负责业务对象与数据库(ORM)的对象
- View: 负责业务逻辑，并在适当的时候调用Model和Template，相当于C
- Template: 负责把页面展示给用户

Django里还有一个url分发器（路由），主要用来将一个个url页面的请求分发给不同的view进行处理，View在调用相应的Model,和Template.



##  二、Django安装

1. 通过pip安装（Python包管理器) （[pip](https://www.runoob.com/w3cnote/python-pip-install-usage.html)用法

```shell
$curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # 下载安装脚本

$sudo -H python get-pip.py --no-wheel    # 运行安装脚本(加上options忽略wheels)
# 安装如果出现以下提示加上 --no-wheel
ERROR: Could not find a version that satisfies the requirement wheel (from versions: none)
ERROR: No matching distribution found for wheel
# 验证安装
$pip --version
# 卸载
$python -m pip uninstall pip
# 查看指定包的安装位置
$pip show packageName
```

**注意：***用哪个版本的 Python 运行安装脚本，pip 就被关联到哪个版本，如果是 Python3 则执行以下命令：*

```shell
$sudo -H python3 get-pip.py    # 运行安装脚本
```

2. 安装django (不指定的话，安装很慢)

```shell
$pip install django==1.11.7 -i https://pypi.douban.com/simple/ tornado # 指定版本号 指定镜像源

# 验证
$pip list 
```

3. 创建项目

```shell
$django-admin startproject projectName # 创建项目
$tree # 树形查看项目结构
$python manage.py startapp appName # 创建一个应用
```

 4.开启服务

```shell
$python manager.py runserver [127.0.0.1:][8000] #启动服务 - 可以直接写端口号 - 默认是8000
```

5.IDE打开要与manager.py同级， 打开projectName项目

  

## 三、Django文件解读

1.settings.py(项目配置)

```python
BASE_DIR  #项目的绝对路径：也就是根路径
SECRECT_KEY #秘钥 - 用于生产环境
DEBUG #调试开关 - 用于开发
ALLOWED_HOSTS = ["*"] #允许访问的主机
INSTALLED_APPS = [...] #已经安装的app，django安装的应用
MIDDLEWARE = [...] #中间件
ROOT_URLCONF = '....urls' #根路由
TEMPLATES #模板
WSGI_APPLICATION #部署用的
DATABASES #数据库
AUTH_PASSWORD_VALIDATORS #鉴权相关
LAUGUAFE_CODE = 'zh-hans' #语言编码
```

2.urls.py（路由）

3.apps.py 应用配置

4.admin.py 后台管理

5.model.py 数据模型

6.tests.py 写测试

7.sqlite

- 轻量级嵌入式数据库
- 特点小，常用于Android ios wp
- 数据库常规操作和mysql很像

```shell
$python3 manage.py migrate # 数据库迁移
```



##  四、路由管理

```python
from django.contrib import admin
from django.urls import path

# 导入view
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.hello),  # 添加路由 - 对应模块下的方法
    path('html/', views.index)
]

# App/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('可还行') # 直接响应 - 也可以是html字符串 返回给浏览器会直接渲染

def index(request):
    return render(request, "index.html") # 渲染模板文件
```



##  五、Model数据模型

Django的models使用了ORM（Object Relational Mapping 对象关系映射）技术，将业务逻辑进行了一个解耦合，在操作数据库时无需关注什么数据库，只需要调用对应的对象和方法，就可以映射成对应的sql语句去执行。

相关文章https://www.bbsmax.com/A/KE5QXjPZJL/

##### 1.创建一张表

DDL: 定义数据库，Django里用models去定义一个数据库模型 - 表

```python
App/models.py
from django.db import models

# Create your models here.

# 新建一个Sduent模型 - student表
class Student(models.Model):
    name = models.CharField(max_length=16) #设置字段名称
    age = models.IntegerField(default=1)
```

然后执行出，表名称 APP_Student

```shell
$python3 manage.py makemigrations # 生成用户表
$python3 manage.py migrate # 数据库迁移
```

##### 2.新增数据

```python
from django.shortcuts import render
from django.http import HttpResponse
import random

# 导入模型
from App.models import Student


# 新增用户数据
def student(request):
    students = Student()
    students.name = 'tom %d' % random.randrange(90)
    students.save()

    return HttpResponse('success %s' % students.name)
```

##### 3.查询数据

```python
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

import random

# 导入模型
from App.models import Student

# 获取学生数
def getStudent():
    students = Student.objects.all()
    # 返回json序列化
    str_students = serializers.serialize("json", students)

    return HttpResponse(str_students)
```

```json
// 会返回如下信息
[{
	"model": "App.student",
	"pk": 1,
	"fields": {
		"name": "tom 39",
		"age": 1
	}
}]
```

##### 4.更新数据

```python
# 更新学生数据
def updateStudent(req):
    # 先查后保存
    student = Student.objects.get(id=1)
    student.name = 'test_update_name'
    student.save()

    return HttpResponse('update success')
```

##### 5.删除数据

```python
# 删除学生数据
def deleteStudent(req):
    student = Student.objects.get(id=1)
    student.delete()

    return HttpResponse('delete success')
```

##### 6.链接mysql数据库

1. 首先修改settings.py下的 DATABASES

```python
DATABASES = {
    # mysql
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoStudy', # dbName
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',
        'port': '3306'
    }
}
```

2. 安装mysql驱动

   （1）mysqlclient: 对mysql有要求，需要存在指定位置的配置文件

    （2）python-mysql: 支持python2

      (3) pymysql: 这个都支持--- 常用

3. 执行shell

```shell
$python3 manage.py makemigrations
$python3 manage.py migrate
```

如果报： raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3.

到django /db/mysql下把base.py如下代码注释掉：

```python
# base.py
# if version < (1, 3, 13):
#     raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)

```

如果报：  query = query.decode(errors='replace') AttributeError: 'str' object has no attribute 'decode'

修改 operations.py, 将decode 修改为 encode

```python
#query = query.decode(errors='replace')
query = query.encode(errors='replace')
```

如果开启服务报： raise RuntimeError("cryptography is required for sha256_password or caching_sha2_password") RuntimeE

执行该条命令

```shell
$pip install cryptography
```

##### 7.数据库操作

- 外键约束

```python
# models.py
from django.db import models

# Create your models here.

# 年级表
class Grade(models.Model):
    name = models.CharField(max_length=32)


# 新建一个Sduent模型 - student表
class Student(models.Model):
    name = models.CharField(max_length=16) #设置字段名称
    age = models.IntegerField(default=1)
    # 级联关系 2.0后定义外键和一对一的关系时要加上这个参数
    grade_id = models.ForeignKey(Grade, on_delete=models.CASCADE) 
    
    
# 相关参数
on_delete=None,               # 删除关联表中的数据时,当前表与其关联的field的行为
on_delete=models.CASCADE,     # 删除关联数据,与之关联也删除
on_delete=models.DO_NOTHING,  # 删除关联数据,什么也不做
on_delete=models.PROTECT,     # 删除关联数据,引发错误ProtectedError

models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)

on_delete=models.SET_NULL,    # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）

models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）

# views.py
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

```



## 六、template模板语法

##### 1.基本语法

```python
# 返回字典对象
return render(request, 'contexts.html', context = { "name": "xiaoming", "age": 12 })
# 这个过程其实是处理好的html字符串返回给客户端
# 利用loader.get_template('index.html').render(context=context)
  
# html
<h1>{{ name }}</h1>
<h2>{{ age }}</h2>
```

##### 2.for循环

```python
# 渲染一个列表
 return render(request, 'list.html', context = { "students": students})

# list.html
<!-- 渲染模板列表 -->
<ul>
    {% for student in students %}
       <li>{{ student.name }}</li>
    {% endfor %}
</ul>
```