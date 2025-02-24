from django.contrib import admin
from .models import ContactUs


class ContactPanel(admin.ModelAdmin):
    list_display = ['name', 'phone', 'query']
    
admin.site.register(ContactUs, ContactPanel)
