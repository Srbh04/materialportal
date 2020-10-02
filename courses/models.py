from django.db import models

# Create your models here.
class course(models.Model):
	cid=models.CharField(max_length=10)
	cname=models.CharField(max_length=40)
	cdept=models.CharField(max_length=30)

	def __str__ (self):
		return str(self.cid)