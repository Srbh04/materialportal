from django.db import models

# Create your models here.
class Student(models.Model):
	sid=models.IntegerField()
	sname=models.CharField(max_length=30)
	smail=models.EmailField()
	spass=models.CharField(max_length=15)
	sdept=models.CharField(max_length=30)

	def __str__(self):
		return self.sname+ ' ' + self.sdept

class student_courses(models.Model):
	sid=models.IntegerField()
	fid=models.IntegerField()
	cid=models.CharField(max_length=10)