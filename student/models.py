from django.db import models

# Create your models here.
class student(models.Model):
	sid=models.IntegerField()
	sname=models.CharField(max_length=30)
	smail=models.EmailField()
	spass=models.CharField(max_length=15)
	sdept=models.CharField(max_length=30)

class student_courses(models.Model):
	sid=models.IntegerField()
	fid=models.IntegerField()
	cid=models.CharField(max_length=10)