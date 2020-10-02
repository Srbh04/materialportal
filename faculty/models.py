from django.db import models

# Create your models here.
class faculty(models.Model):
	fusername=models.CharField(max_length=30)
	fname=models.CharField(max_length=30)
	fmail=models.EmailField()
	fpass=models.CharField(max_length=15)

class faculty_courses(models.Model):
	fid=models.IntegerField()
	cid=models.CharField(max_length=10)

class files(models.Model):
	fid=models.IntegerField()
	cid=models.CharField(max_length=10)
	material=models.FileField()
	date=models.DateField()