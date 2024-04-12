"""
URL configuration for webappmovieprj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('movieapp/',include('movieapp.urls')),
    path('favouritesapp/',include('favouritesapp.urls')),
    path('search/',include('searchapp.urls')),
    path('userreviewapp/',include('userreviewapp.urls')),
    path('credentialsapp/',include('credentialsapp.urls')),
    re_path(r'^$', RedirectView.as_view(url='movieapp/')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)