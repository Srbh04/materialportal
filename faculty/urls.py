
from django.urls import path
from . import views

urlpatterns = [
	path('',views.facultyLogin),
	path('facultyRegister/<username>',views.view_courses_faculty,name="viewcourses"),
    path('facultyRegister/',views.facultyRegister,name="facultyRegister"),
    path('facultyLogin/',views.facultyLogin,name="facultyLogin"),
    path('facultyLogout/',views.facultyLogout,name="facultyLogout"),
    path('faculty/course',views.view_courses_for_files,name="courses"),
    path('faculty/course/<cid>',views.files_page,name="files"),
    path('faculty/courses/deleteData/<int:pk>',views.deleteData,name="deleteData"),
    # path('showfiles/<cid>',views.showFiles,name="showFiles")
]