from django.contrib import admin
from .models import Post
# Register your models here.
#Tạo python3 manage.py create superuser
#Sau đó thêm vô admin
admin.site.register(Post)
