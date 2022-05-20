from django.contrib import admin

# Register your models here.

from .models import Wine, Location, Maker

admin.site.register(Wine)
admin.site.register(Location)
admin.site.register(Maker)