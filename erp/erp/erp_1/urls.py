from django.urls import path, re_path
from . import views


urlpatterns = [
    path('personnelmanagement/', views.personnel_management, name='personnel_management'),
    path('departmentmanagement/', views.department_management, name='department_management'),
    path('material_management/', views.material_management, name='material_management'),
    path('FlowOfProduction_management/', views.FlowOfProduction_management, name='FlowOfProduction_management'),
    path('ProductionProcess_management/', views.process_management, name='process_management'),
    path('BOM_management/', views.BOM_management, name='BOM_management'),

    path('personnelmanagement/add_people/', views.add_people, name='add_people'),
    path('personnelmanagement/delete_people/', views.delete_people,  name='StaffDelete'),
    re_path('personnelmanagement/StaffDetail/(?P<id>[0-9]{6})', views.staff_detail, name='StaffDetail'),

    path('material_management/add_materials/', views.add_materials, name='add_materials'),
    re_path('material_management/MaterialsDetail/(?P<id>[0-9]{6})', views.material_detail, name='MaterialsDetail'),
    path('material_management/delete_materials/', views.delete_materials,  name='MaterialsDelete'),

    path('BOM_management/add_BOM/', views.add_BOM, name='add_BOM'),
    re_path('BOM_management/BOMDetail/(?P<id>[0-9]{6})', views.BOM_detail, name='BOMDetail'),
    path('material_management/delete_BOM/', views.delete_BOM,  name='BomDelete'),

    path('ProductionProcess_management/add_process/', views.add_process, name='add_process'),
    path('ProductionProcess_management/delete_process/', views.delete_process, name='processDelete'),
    re_path('ProductionProcess_management/ProcessDetail/(?P<id>[0-9]{6})', views.process_detail, name='ProcessDetail'),

    path('FlowOfProduction_management/add_flow/', views.add_flow, name='add_flow'),
    path('FlowOfProduction_management/delete_fow/', views.delete_flow, name='flowDelete'),
    re_path('FlowOfProduction_management/flowDetail/(?P<id>[0-9]{6})', views.flow_detail, name='flowDetail'),
]