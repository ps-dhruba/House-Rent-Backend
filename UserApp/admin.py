from django.contrib import admin
from . import models

class UserPanel(admin.ModelAdmin):
    list_display = ['first_name','last_name','mobile_no', 'image', 'address']
    
    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name
    
    
admin.site.register(models.UserModel, UserPanel)