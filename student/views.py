from django.shortcuts import render,redirect
from django.http import HttpResponse
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
            sid=int(request.POST.get('sid'))
            password=request.POST.get('password')
            f=0
            for item in Student.objects.all():
                if item.sid==sid and item.spass==password:
                    f=1
            if f==1:
                return redirect('s_courses',sid)
            else:
                 messages.info(request,'incorrect crendentials')

    return render(request,'studentLogin.html')


def studentLogout(request):
    logout(request)
    return redirect('studentLogin')

def view_courses_student(request,sid):
    allcourse=faculty_courses.objects.all()
    count=[]
    fac_detail=[]
    course_detail=[]
    for i in allcourse:
        try:
            count.append(len(count)+1)
            fac_detail.append(faculty.objects.get(fusername=i.fusername))
            course_detail.append(course.objects.get(cid=i.cid))
        except:
            z=3
    if request.method=='POST':
        checklist= request.POST.getlist('checks[]')
        for c in checklist:
            ci=int(c)
            sc=student_courses(fusername=fac_detail[ci-1].fusername,cid=course_detail[ci-1].cid,sid=sid)
            sc.save()
        return redirect('studentLogin')
    else:
        zip_data=zip(count,fac_detail,course_detail)
        return render(request,'view_courses.html',{'zip':zip_data})


def view_courses_for_files(request,sid):
    all_cname=[]
    all_cid=[]
    all_fusername=[]
    sc=student_courses.objects.filter(sid=sid)
    print(sc.count())
    for i in sc:
        m=course.objects.get(cid=i.cid)
        all_cname.append(m.cname)
        all_cid.append(i.cid)
        all_fusername.append(i.fusername)
    zip_data=zip(all_cname,all_cid,all_fusername)
    return render(request,'s_courses.html',{'zip':zip_data})