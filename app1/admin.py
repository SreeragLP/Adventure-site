from django.contrib import admin
from .models import AdventurePackage,Rating

# Register your models here.
admin.site.register(AdventurePackage)
admin.site.register(Rating)

