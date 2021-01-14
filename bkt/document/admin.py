from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Radar)
admin.site.register(Content)
admin.site.register(ContentA)
admin.site.register(ContentB)

