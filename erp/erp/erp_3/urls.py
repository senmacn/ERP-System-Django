"""MRP URL Configuration

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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('MPS_manager/', views.MPS_manager, name='MPS_manager'),
    path('indent_create/', views.indent_create, name='indent_create'),
    re_path('indent_show/(?P<MPS_id>[0-9]{6})/', views.indent_show, name='indent_show'),
    re_path('purchase_show/(?P<MPS_id>[0-9]{6})/', views.purchase_show, name='purchase_show'),
    re_path('self_product_show/(?P<MPS_id>[0-9]{6})/', views.self_product_show, name='self_product_show'),
    re_path('indent_all_show/(?P<MPS_id>[0-9]{6})/', views.indent_all_show, name='indent_all_show'),
    path('MRP_record/', views.MRP_record, name='MRP_record'),
    re_path('MPS_detail/(?P<MPS_id>[0-9]{6})/', views.MPS_detail, name='MPS_detail'),
    re_path('MPS_alter/(?P<MPS_id>[0-9]{6})/', views.MPS_alter, name='MPS_alter'),
    re_path('MPS_add/', views.MPS_add, name='MPS_add'),
    re_path('MPS_delete/(?P<MPS_id>[0-9]{6})/', views.MPS_delete, name='MPS_delete'),
    re_path('product_add/(?P<mps_id>[0-9]{6})/', views.product_add, name='product_add'),
    re_path('product_alter/(?P<product_id>[0-9]{6})/', views.product_alter, name='product_alter'),
    re_path('product_delete/(?P<product_id>[0-9]{6})/', views.product_delete, name='product_delete'),
    re_path('plan_alter/(?P<plan_id>[0-9]{6})/', views.plan_alter, name='plan_alter'),
    re_path('plan_delete/(?P<plan_id>[0-9]{6})/', views.plan_delete, name='plan_delete'),
    re_path('plan_add/(?P<product_id>[0-9]{6})/', views.plan_add, name='plan_add'),
]
