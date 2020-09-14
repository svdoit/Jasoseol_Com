from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True) #시간이 자동으로 입력 됨 
<<<<<<< HEAD
    
=======
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    jasoseol = models.ForeignKey(Jasoseol, on_delete=models.CASCADE)
>>>>>>> 98dd5121f3d126249cf239fa303b0d768e401185
