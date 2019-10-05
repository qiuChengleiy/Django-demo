# 路由分发 --- 主路由上include导入
from django.urls import path

# 导入view
from App import views

urlpatterns = [
    path('test/', views.hello),  # 添加路由
    path('html/', views.index),
    path('add/', views.addStudent),
    path('get/', views.getStudent),
    path('update/', views.updateStudent),
    path('delete/', views.deleteStudent),
]