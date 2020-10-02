from django.shortcuts import render,redirect
from faculty.models import faculty_courses
from student.models import student_courses
from .forms import StudentForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db import connection
from .models import Student
# Create your views here.
def studentRegister(request):
    form=StudentForm()
    if request.method == 'POST':
            form=StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('studentLogin')
    context={'form':form}
    return render(request,'studentregister.html',context)

def studentLogin(request):
    if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            f=0
            for item in Student.objects.all():
                if item.sname==username and item.spass==password:
                    f=1
           
            if f==1:
                return render(request,'home.html')
            else:
                 messages.info(request,'incorrect crendentials')

    return render(request,'studentlogin.html')


def studentLogout(request):
    logout(request)
    return redirect('studentLogin')