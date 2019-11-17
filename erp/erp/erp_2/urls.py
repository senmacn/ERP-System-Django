from django.urls import path,re_path
from . import views


urlpatterns = [
    path('staff_management/', views.staff_management, name='staff_management'),
    path('customer_management/', views.customer_management, name='customer_management'),
    path('product_management/', views.product_management, name='product_management'),
    path('order_management/', views.order_management, name='order_management'),
    path('order_management/add_order/', views.add_order, name='add_order'),
    path('order_management/delete_order/', views.delete_order,  name='OrderDelete'),
    re_path('order_management/OrderDetails/(?P<id>[0-9]{6})', views.OrderDetails, name='OrderDetails'),
    path('customer_management/add_customer/', views.add_customer, name='add_customer'),
    path('customer_management/delete_customer/', views.delete_customer, name='CustomerDelete'),
    re_path('customer_management/CustomerDetails/(?P<id>[0-9]{6})', views.CustomerDetails, name='CustomerDetails'),
    path('product_management/add_product/', views.add_product, name='add_product'),
    path('product_management/delete_product/', views.delete_product, name='ProductDelete'),
    re_path('product_management/ProductDetails/(?P<id>[0-9]{6})', views.ProductDetails, name='ProductDetails'),
    path('application_management/', views.application_management, name='application_management'),
    path('application_management/add_app2/', views.add_app2, name='add_app2'),
    re_path('application_management/delete_app2/(?P<app_id>[0-9]{6})', views.delete_app2, name='delete_app2'),
    re_path('application_management/confirm_app2/(?P<app_id>[0-9]{6})', views.confirm_app2, name='confirm_app2'),
    path('application_management/confirm_app/', views.confirm_app2, name='confirm_app2'),
]