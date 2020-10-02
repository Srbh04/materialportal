from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('studentRegister/',views.studentRegister,name="studentRegister"),
    path('studentLogin/',views.studentLogin,name="studentLogin"),
    path('studentLogout/',views.studentLogout,name="studentLogout"),

]