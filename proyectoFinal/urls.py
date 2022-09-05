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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from proyectoFinal.views import resenas, index, search_catalog, about, pages
from films.views import create_film, list_films,delete_film,update_film, Detail_film 
from tv_shows.views import create_tv_show, delete_tv_show, list_tv_shows, update_tv_show, Detail_tv_show
from reviews.views import create_review, delete_review, list_reviews, Detail_review

urlpatterns = [
    path('', index, name = 'index'),
    path('admin/', admin.site.urls),	
    path('reviews-list/', resenas, name='Reviews'),	
    path('create-film/',create_film, name = 'Create_film'),
    path('list-films/',list_films, name = 'list_films'),
    path('create-tv-show/',create_tv_show, name = 'create_tv_show'),
    path('list-tv-shows/',list_tv_shows, name = 'list_tv_shows'),
    path('create-review/', create_review, name = 'create_review'),
    path('list-reviews/', list_reviews, name = 'list reviews'),
    path('search-catalog/', search_catalog, name = 'search'),
    path('about/', about, name = 'about'),
    path('pages/', pages, name = 'pages'),

    path('delete-tv-show/<int:pk>', delete_tv_show, name='delete_tv_show'),
    path('delete-film/<int:pk>', delete_film, name='delete_film'),
    path('delete-review/<int:pk>', delete_review, name = 'delete_review'),

    path('detail-film/<int:pk>', Detail_film.as_view(), name='Detail_film'),
    path('detail-review/<int:pk>', Detail_review.as_view(), name='Detail_review'),
    path('detail-tv-show/<int:pk>', Detail_tv_show.as_view(), name='Detail_tv_show'),
    path('users/', include('users.urls')),

    path('update-tv-show/<int:pk>', update_tv_show, name='update_tv_show'),
    path('update-film/<int:pk>', update_film, name='update_film'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

