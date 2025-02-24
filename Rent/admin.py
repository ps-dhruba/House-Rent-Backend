from django.contrib import admin
from . import models

class LocationPanel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('location',), }

class HouseTypePanel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('type',), }
    
admin.site.register(models.Location, LocationPanel)
admin.site.register(models.HouseType, HouseTypePanel)
admin.site.register(models.House)
admin.site.register(models.Review)