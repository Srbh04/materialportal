from django.db import models

# Create your models here.
class faculty(models.Model):
	fusername=models.CharField(max_length=30,default="00s00")
	fname=models.CharField(max_length=30)
	fmail=models.EmailField()
	fpass=models.CharField(max_length=15)

class faculty_courses(models.Model):
	fusername=models.CharField(max_length=30,default="00s00")
	cid=models.CharField(max_length=10)

class files(models.Model):
	fusername=models.CharField(max_length=30)
	cid=models.CharField(max_length=10)
	title=models.CharField(max_length=200)
	material=models.FileField()
	date=models.DateField()

	def __str__(self):
		return self.title + ' ' +self.cid + ' ' + self.fusername
	
	def delete(self,*args,**kwargs):
		self.material.delete()
		super().delete(*args,**kwargs)