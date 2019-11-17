"""erp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from erp_1 import views
import erp_1.urls
import erp_2.urls
import erp_3.urls
import erp_4.urls
import erp_5.urls
import erp_6.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('index/', views.index, name='index'),
    path('', views.index, name='index'),
    path('erp_1/', include(erp_1.urls)),
    path('erp_2/', include(erp_2.urls)),
    path('erp_3/', include(erp_3.urls)),
    path('erp_4/', include(erp_4.urls)),
    path('erp_5/', include(erp_5.urls)),
    path('erp_6/', include(erp_6.urls)),
]