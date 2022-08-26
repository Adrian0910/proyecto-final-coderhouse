"""proyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from proyectoFinal.views import resenas, home, search_catalog, about, pages
from films.views import create_film
from films.views import create_film, list_films
from tv_shows.views import create_tv_show, delete_tv_show, list_tv_shows
from reviews.views import create_review, list_reviews


urlpatterns = [
    path('admin/', admin.site.urls),	
    path('reviews-list/', resenas, name='Reviews'),	
    path('create-film/',create_film, name = 'Create_film'),
    path('',home, name = 'template base'),
    path('list-films/',list_films, name = 'list_films'),
    path('create-tv-show/',create_tv_show, name = 'create_tv_show'),
    path('list-tv-shows/',list_tv_shows, name = 'list_tv_shows'),
    path('create-review/', create_review, name = 'create_review'),
    path('list-reviews/', list_reviews, name = 'list reviews'),
    path('search-catalog/', search_catalog, name = 'search'),
    path('about/', about, name = 'about'),
    path('pages/', pages, name = 'pages'),
    path('delete-tv-show/<int:pk>', delete_tv_show, name='delete_tv_show'),
]

