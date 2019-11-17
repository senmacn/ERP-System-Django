from django.urls import path, re_path
from . import views


urlpatterns = [
    path('WMS/', views.WMS1, name='WMS'),
    # path('WMS/add_wms/', views.add_wms1, name='add_wms'),
    path('WMS/delete_WMS/', views.delete_wms1,  name='WMSDelete'),
    re_path('WMS/WMSDetail/(?P<id>[0-9]{6})/', views.WMSdetail1, name='WMSDetail'),

    path('Goods/', views.Goods1, name='Goods'),

    path('Check/', views.Check1, name='Check'),
    path('Check/add_check/', views.add_check1, name='add_check'),
    path('Check/delete_check/', views.delete_check1,  name='checkDelete'),
    re_path('Check/apply/(?P<id>[0-9]{14})/', views.apply,  name='apply'),
    re_path('Check/CheckDetail/(?P<id>[0-9]{14})/', views.checkdetail1, name='checkDetail'),

    path('App/', views.App1, name='App'),
    path('App/add_app/', views.add_app1, name='add_app'),
    path('App/delete_app/', views.delete_app1,  name='appDelete'),
    re_path('App/appDetail/(?P<id>[0-9]{6})/', views.appdetail1, name='appDetail'),

    path('Move/', views.Move1, name='Move'),
    path('Change/add_move/', views.add_move1, name='add_move'),

    path('Change/', views.Change1, name='Change'),
    path('Change/add_change/', views.add_change1, name='add_change'),
    path('Change/delete_change/', views.delete_change1,  name='changeDelete'),
    re_path('Change/changeDetail/(?P<id>[0-9]{6})/', views.changeDetail1, name='changeDetail'),
]