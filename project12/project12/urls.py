"""project12 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from app12 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.studentInfo,name="home"),
    path('studentlogin/',views.studentLogin,name="studentlogin"),
    path('register/',views.studentRegister,name="register"),
    path('registered/',views.studentData,name="registered"),
    path('slogin/',views.sLogin,name="slogin"),
    path('student_home/',views.studentHome,name="student_home"),
    path('student_profile/',views.studentProfile,name="student_profile"),
    path('student_update/',views.studentUpdate,name="student_update"),
    path('update_student/',views.updateStudent,name="update_student"),

    path('forgotpassword/',views.forgot,name="fp"),
    path('check_password/',views.checkPassword,name="check_password"),
    path('ad/',views.adminLogin,name="ad"),
    path('adlog/',views.adLogin,name="adlog"),
    path('admin_home/',views.adminHome,name="admin_home"),
    path('view_profile/',views.viewProfile,name="view_profile"),
    path('adview_profile/',views.adviewProfile,name="adview_profile")


]
