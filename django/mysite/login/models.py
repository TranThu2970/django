from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class PostLogin(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.title


#Tạo thêm thuộc tính cho user
#1:Tạo model=>#2: settings: AUTH_USER_MODEL = 'login.MyUser'
class MyUser(AbstractUser):
    gender_choice =((0,'Nữ'),(1,'Nam'),(2,'Không xác định'))
    Age = models.IntegerField(default=0)
    Gender = models.IntegerField(choices=gender_choice,default=0)
    Address = models.CharField(default='',max_length=255)