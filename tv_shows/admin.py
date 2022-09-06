from django.contrib import admin

# Register your models here.

from tv_shows.models import Tv_shows

class Tv_showsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'year', 'director', 'actors', 'description', 'image')


