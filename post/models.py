from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	poster = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	title = models.TextField(null=True)
	description = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True)

class Files(models.Model):
	file_user = models.ForeignKey('Post',on_delete=models.CASCADE,null=True)
	file = models.FileField(blank=True)





# Create your models here.
