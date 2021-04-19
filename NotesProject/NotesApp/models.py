from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Updf(models.Model):
	g = [('M',"Male"),('F',"Female")]
	age = models.IntegerField(default=18)
	gender = models.CharField(max_length=7,choices=g)
	im = models.ImageField(upload_to="Profile_pics/",default="avatar.png")
	pr = models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def CrtPfle(sender,instance,created,**kwargs):
	 if created:
	 	Updf.objects.create(pr=instance)


class CrNt(models.Model):
	title = models.CharField(max_length=120)
	date = models.DateField()
	desc = models.TextField()
	created_by = models.CharField(max_length=120)
	fil = models.FileField(upload_to="UploadedFiles/")
	gnkey = models.TextField()
	crt = models.ForeignKey(User,on_delete=models.CASCADE)

