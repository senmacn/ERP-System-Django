
from django.urls import path, re_path
from . import views


urlpatterns = [
    path('personnelmanagement/', views.personnel_management, name='ersonnel_management'),
    path('zhizaodingdan/', views.zhizaodingdan1, name='zhizaodingdan'),
    path('zhizaodingdan/add_zhizaodingdan/', views.add_zhizaodingdan , name='add_zhizaodingdan'),
    path('zhizaodingdan/delete_zhizaodingdan/', views.delete_zhizaodingdan,  name='zhizaodingdanDelete'),
    re_path('zhizaodingdan/zhizaodingdanDetail/(?P<id>[0-9]{6})', views.zhizaodingdan_detail, name='zhizaodingdanDetail'),
    path('paigongdan/', views.paigongdan1, name='paigongdan'),
    path('paigongdan/add_paigongdan/', views.add_paigongdan , name='add_paigongdan'),
    path('paigongdan/delete_paigongdan/', views.delete_paigongdan,  name='paigongdanDelete'),
    re_path('paigongdan/paigongdanDetail/(?P<id>[0-9]{6})', views.paigongdan_detail, name='paigongdanDetail'),
    path('jianyandan/', views.jianyandan1, name='jianyandan'),
    path('jianyandan/add_jianyandan/', views.add_jianyandan , name='add_jianyandan'),
    path('jianyandan/delete_jianyandan/', views.delete_jianyandan,  name='jianyandanDelete'),
    re_path('jianyandan/jianyandanDetail/(?P<id>[0-9]{6})', views.jianyandan_detail, name='jianyandanDetail'),
    path('kudan/', views.kudan1, name='kudan'),
    path('kudan/add_kudan/', views.add_kudan, name='add_kudan'),
    path('kudan/delete_kudan/', views.delete_kudan, name='kudanDelete'),
    re_path('kudan/kudanDetail/(?P<app_id>[0-9]{6})', views.kudan_detail, name='kudanDetail'),
]