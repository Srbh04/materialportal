
from django.urls import path
from . import views

urlpatterns = [
	path('',views.view_courses_faculty,name="viewcourses"),
    path('facultyRegister/',views.facultyRegister,name="facultyRegister"),
    path('facultyLogin/',views.facultyLogin,name="facultyLogin"),
    path('facultyLogout/',views.facultyLogout,name="facultyLogout"),
]