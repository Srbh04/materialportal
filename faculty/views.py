from django.shortcuts import render,redirect,HttpResponse
from courses.models import course
from faculty.models import faculty_courses,faculty
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
            return redirect('facultyLogin')

    return render(request,'facultyregister.html',{'form':form})

def facultyLogin(request):
    if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request, username=username, password=password)  

            if user is not None:
                login(request,user)
                return render(request,'home.html')
            else:
                messages.info(request,'incorrect crendentials')

    return render(request,'facultylogin.html')


def facultyLogout(request):
    logout(request)
    return redirect('facultyLogin')

def view_courses_faculty(request):
	allcourse=list(course.objects.all())
	if request.method=='POST':
		checklist= request.POST.getlist('checks[]')
		for c in checklist:
			fc=faculty_courses()
			print(request.user.fid)
			#fc.fid=123
			fc.cid=c
			#print(fc.cid)
		return HttpResponse("successfully registered !!!")
	else:
		return render(request,'view_courses.html',{'course':allcourse})

def view_courses_for_files(request):
	fid=request.user.fid
	fc=list(faculty_courses.objects.filter(fid=fid))
	allcourse=[]
	for i in fc:
		allcourse=append(course.objects.filter(cid=f.cid))
	return render(request,'index2.html',{'allcourse':allcourse})



