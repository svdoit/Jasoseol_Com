from django.db import models

# Create your models here.

class Jasoseol(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True) #시간이 자동으로 입력 됨 
    