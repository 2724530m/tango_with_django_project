"""tango_with_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls import include
from rango import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('logout/', views.user_logout, name='logout'),
    path('restricted/', views.restricted, name='restricted'),
    path('login/', views.user_login, name='login'),
    path('',views.index,name='index'),
    path('admin/', admin.site.urls),
    path('rango/', include('rango.urls')),
# The above maps any URLs starting with rango/ to be handled by rango
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)