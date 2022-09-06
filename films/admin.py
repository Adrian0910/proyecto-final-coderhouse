from django.contrib import admin
from films.models import Film
# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'year', 'director', 'actors', 'description', 'image']

