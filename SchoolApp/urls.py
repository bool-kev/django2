"""
URL configuration for SchoolApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from adminApp.views import root
from django.contrib.auth.views import LoginView
from SchoolApp import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',root,name='acceuil'),
    path('accounts/login/',view=LoginView.as_view(template_name="adminApp/login.html"),name="login"),
    path('user/',include('userApp.urls'),),
    path('admin/',include('adminApp.urls')),
    path('superuser/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
