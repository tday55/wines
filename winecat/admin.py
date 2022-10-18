from django.contrib import admin

# Register your models here.

from .models import Wine, Location, Maker, Stock

admin.site.register(Wine)
admin.site.register(Location)
admin.site.register(Maker)
admin.site.register(Stock)