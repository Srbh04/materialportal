from django.shortcuts import render
from django.http import HttpResponse
from courses.models import course
from faculty.models import faculty_courses,faculty

# Create your views here.
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
		return render(request,'faculty/view_courses.html',{'course':allcourse})

def view_courses_for_files(request):
	fid=request.user.fid
	fc=list(faculty_courses.objects.filter(fid=fid))
	allcourse=[]
	for i in fc:
		allcourse=append(course.objects.filter(cid=f.cid))
	return render(request,'faculty/index2.html',{'allcourse':allcourse})



