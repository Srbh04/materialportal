from django.shortcuts import render,redirect
from faculty.models import faculty_courses,faculty
from student.models import student_courses
from courses.models import course
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
                sid=form.cleaned_data['sid']
                return redirect('studentcourse',sid)
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

def view_courses_student(request,sid):
    allcourse=list(faculty_courses.objects.all())
    fac_detail=[]
    course_detail=[]
    for i in allcourse:
        try:
            fac_detail.append(faculty.objects.get(fusername=i.fusername))
            course_detail.append(course.objects.get(cid=i.cid))
        except:
            z=3

    if request.method=='POST':
        checklist= request.POST.getlist('checks[]')
        for c in checklist:
            print(c)
            fc=student_courses(fusername=username,cid=c,sid=sid)
            fc.save()
        return HttpResponse("successfully registered !!!")
    else:
        zip_data=zip(fac_detail,course_detail)
        return render(request,'view_courses.html',{'zip':zip_data})