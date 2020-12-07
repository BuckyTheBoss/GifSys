from django.contrib import admin
from .models import Category, Gif
# Register your models here.
admin.site.register(Gif)
admin.site.register(Category)