from django.contrib import admin
from  django.contrib.auth.models  import  Group
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','password']
    search_fields = ['id','username','email']

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)