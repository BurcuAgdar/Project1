"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from school import views
from user import views as eb


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name ='index'),
    path('about/', views.about,name ='about'),
    path('user/',include('user.urls')),
    path('teacher/<str:data>/', eb.teacher,name ='teacher'),
    path('student/<str:data>/', eb.student,name ='student'),
    path('manager/<str:data>/', eb.manager,name ='manager'),
    path('manager/update/<str:data>/',eb.updateTeacher,name='update'),
    path('manager/delete/<str:data>/',eb.deleteTeacher,name='delete'),
    path('manager/updateStudent/<str:data>/',eb.updateStudent,name='updateS'),
    path('manager/deleteStudent/<str:data>/',eb.deleteStudent,name='deleteS'),
    path('teacher/updateStudent/<str:data>/',eb.updateStudentTe,name='updateSt'),
    path('teacher/deleteStudent/<str:data>/',eb.deleteStudentTe,name='deleteS'),
    
    
]
