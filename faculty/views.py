from django.shortcuts import render,redirect,HttpResponse
from courses.models import course
from faculty.models import faculty_courses,faculty,files
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def facultyRegister(request):
    form=CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            name=form.cleaned_data['first_name']
            mail=form.cleaned_data['email']
            passs=form.cleaned_data['password1']
            f=faculty(fusername=username,fname=name,fmail=mail,fpass=passs)
            f.save()
            return redirect('viewcourses',username)

    return render(request,'facultyregister.html',{'form':form})

def facultyLogin(request):
    if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)  

            if user is not None:
                login(request,user)
                return redirect('courses')
            else:
                messages.info(request,'incorrect crendentials')

    return render(request,'facultylogin.html')


def facultyLogout(request):
    logout(request)
    return redirect('facultyLogin')

def view_courses_faculty(request,username):
    allcourse=list(course.objects.all())
    if request.method=='POST':
        checklist= request.POST.getlist('checks[]')
        print(username)
        for c in checklist:
            print(c)
            fc=faculty_courses(fusername=username,cid=c)
            fc.save()
        return redirect('facultyLogin')
    else:
        return render(request,'fview_courses.html',{'course':allcourse})

def view_courses_for_files(request):
    username=request.user.username
    allname=[]
    allid=[]
    fc=faculty_courses.objects.filter(fusername=username)
    for i in fc:
        m=course.objects.get(cid=i.cid)
        allname.append(m.cname)
        allid.append(i.cid)
    zip_data=zip (allname,allid)
    return render(request,'course.html',{'zip':zip_data})

def files_page(request,cid):
    username=request.user.username
    tot_files=files.objects.filter(fusername=username).filter(cid=cid)
    return render(request,'files.html',{'f':tot_files})


def index(request):
    return render(request,'base.html')