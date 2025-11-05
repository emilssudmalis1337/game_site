"""
URL configuration for game_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from . import views
from django.views.generic.base import TemplateView
#from cruds.urls import crud_for_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('games/', views.games_view, name="games"),
    path('update_game/<id>', views.update_game, name="update_game"),
    path('delete_game/<id>', views.delete_game, name="delete_game"),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", views.games_view_main, name="home"),
    path('game/<int:game_id>/json/', views.game_detail_json, name='game_detail_json'),
]
