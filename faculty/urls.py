from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('facultyRegister/',views.facultyRegister),
    path('facultyLogin/',views.facultyLogin,name="facultyLogin"),
    path('facultyLogout/',views.facultyLogout,name="facultyLogout"),
]