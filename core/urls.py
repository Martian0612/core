"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from home.views import *
from vege.views import *
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name = "index"),
    path('success-page', success_page, name = "success_page"),
    path('receipe', receipe, name = "receipe"),
    path('show-receipe', show_receipe, name = "show_receipe"),
    path('update-receipe/<int:id>',update_receipe, name = "update_receipe"),
    path('delete-receipe/<int:id>', delete_receipe, name = "delete_receipe"),
    path('register',register, name = "register"),
    path('login',login_page, name = "login_page"),
    path('logout',logout_page, name = "logout_page"),
    path('get_data',get_student_data,name = "get_student_data"),
    path('view-marks/<str:student_id>/',view_marks,name= "view_marks")
]
