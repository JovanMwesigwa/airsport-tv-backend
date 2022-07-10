from django.contrib import admin

from .models import SportEvent, Category

# Register your models here.
admin.site.register(SportEvent)
admin.site.register(Category)
