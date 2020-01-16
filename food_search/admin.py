from django.contrib import admin

# Register your models here.
from .models import Food, Diet

admin.site.register(Food)
admin.site.register(Diet)