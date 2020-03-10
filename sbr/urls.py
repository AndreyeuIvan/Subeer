"""sbr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from search import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.serial_all, name='serial'),
    path('season/', views.season_all, name='season'),
    path('episode/', views.episode_id, name='episode'),
    path('<int:serial_id>/', views.serial_id, name='serial_id'),
    path('<int:season_id>/', views.season_id, name='season_id'),
    path('<int:episode_id>/',views.episode_id, name='epidose_id'),
]
