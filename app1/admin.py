from django.contrib import admin
from .models import AdventurePackage,Rating,YourResponse

# Register your models here.
admin.site.register(AdventurePackage)
admin.site.register(Rating)
admin.site.register(YourResponse)

