from django.contrib import admin
from .models import *
# Register your models here.
from .models import Users, Questions

admin.site.register(Users)
admin.site.register(Questions)
