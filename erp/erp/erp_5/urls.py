from django.urls import path, re_path
from . import views


urlpatterns = [
    path('Supplier_management/', views.supplier_management, name='Supplier management'),
    path('supplier_information/', views.supplier_information, name='supplier information'),
    path('add_supplier/', views.add_supplier, name='add supplier'),
    re_path('supplier_information/supplier_detail/(?P<id>[0-9]{6})', views.supplier_detail, name='supplier detail'),
    re_path('supplier_information/supplier_delete/(?P<id>[0-9]{6})', views.supplier_delete, name='supplier delete'),
    path('supply_information/',views.supply_information, name='supply information'),
    re_path('supply_information/supply_detail/(?P<id>[0-9]{1,6})', views.supply_detail, name='supply detail'),
    re_path('supply_information/supply_delete/(?P<id>[0-9]{1,6})', views.supply_delete, name='supply delete'),
    path('add_supply/', views.add_supply, name='add supply'),
    path('supplier_assessment/', views.supplier_assessment, name='supplier assessment'),
    re_path('supplier_assessment/supplier_order/(?P<id>[0-9]{6})', views.supplier_order, name='supplier order'),


    path('Order_management/',views.order_management, name='Order management'),
    path('order_information/', views.order_information, name='order information'),
    re_path('order_information/order_detail/(?P<id>[0-9]{6})',views.order_detail, name='order detail'),
    path('add_order/',views.add_order,name='add order'),
    re_path('order_detail/add_detail/(?P<id>[0-9]{6})',views.add_detail,name='add detail'),
    re_path('order_detail/detail_delete/(?P<did>[0-9]{6})/(?P<oid>[0-9]{6})',views.detail_delete,name='detail delete'),
    re_path('order_detail/add_detail/choose_detail/(?P<rid>[0-9]{6})/(?P<oid>[0-9]{6})',views.choose_detail,name='choose detail'),
    re_path('order_information/order_delete/(?P<id>[0-9]{6})', views.order_delete, name='order delete'),
    path('requisition_information/', views.requisition_information, name='requisition information'),
    path('all_requisition/', views.all_requisition, name='all requisition'),
    re_path('requisition_information/requisition_detail/(?P<id>[0-9]{6})', views.requisition_detail,name='requisition detail'),
    re_path('requisition_information/requisition_detail/choose_supplier(?P<rid>[0-9]{6})/(?P<sid>[0-9]{1,6})', views.choose_supplier, name='choose supplier'),

    path('buyer_management/', views.buyer_management, name='Buyer management'),
    path('buyer_information/', views.buyer_information, name='buyer information'),
    re_path('buyer_information/buyer_order/(?P<id>[0-9]{6})', views.buyer_order, name='buyer order'),
    path('performance/', views.performance, name='performance'),

    path('Receive_management/',views.receive_management,name='Receive management'),
    path('application_information/',views.application_information,name='application information'),
    path('choose_order',views.choose_order,name='choose order'),
    re_path('application_information/choose_order/add_application/(?P<id>[0-9]{1,6})',views.add_application, name='add application'),
    path('assessment_information/', views.assessment_information, name='assessment information'),
    path('assessment/',views.assessment,name='assessment'),

    path('Query_report/',views.query_report,name='Query report'),
    path('query/',views.query,name='query'),
    path('order_on_way/',views.order_on_way,name='order on way'),
    re_path('order_read/(?P<id>[0-9]{6})',views.order_read, name='order read'),
    path('report/',views.report,name='report'),

    ]

