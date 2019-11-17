from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView
#验证用户
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from .models import *


def logout(request):
    request.session.flush()
    return redirect("/login/")


def login(request):
    if request.method == 'POST':
        try:
            user_name = request.POST['Username']
            password = request.POST['Password']
            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                auth.login(request, user)
                request.session['is_login'] = True
                request.session['user_name'] = user_name
                user = User.objects.get(username=user_name)
                role = ''
                for user1 in user.user_role.all():
                    role = role + str(user1.name)
                request.session['role'] = role
                return redirect('/index/')
            else:
                messages.add_message(request, messages.WARNING, '登陆失败')
        except:
            messages.add_message(request, messages.WARNING, '登陆失败')
    if request.session.get('is_login', None):
        return redirect("/index/")
    return render(request, 'login.html', locals())


def register(request):
    roles = Role.objects.all()
    if request.method == 'POST':
        try:
            username = request.POST['Username']
            password = request.POST['Password']
            # 判断用户名是否存在
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.WARNING, '用户已存在')
                return render(request, 'register.html', locals())
            else:
                user = User.objects.create_user(username=username, password=password)
                role = Role.objects.get(name=request.POST['role'])
                role.user.add(user)
                role.save()
                user.save()
                messages.add_message(request, messages.WARNING, '用户创建成功')
                return redirect("/login/")
        except:
            messages.add_message(request, messages.WARNING, '注册失败')
    return render(request, 'register.html', locals())


def index(request):
    if 'is_login' not in request.session or request.session.get('is_login') != True:
        return redirect('/login/')

    staff_name = request.session['user_name']
    staff_role = request.session['role']
    staff_num = len(Staff.objects.all())
    return render(request, 'erp_1/index.html', locals())


def personnel_management(request):
    if 'is_login' not in request.session or request.session.get('is_login')!=True:
        return redirect('/login/')
    if 'role' in request.session and '人事员' in request.session['role']:
        right = True

    if 'id' in request.GET and request.GET['id']:
        search_id = request.GET['id']
        search_staff = Staff.objects.filter(id=search_id)
    if 'name' in request.GET and request.GET['name']:
        search_name = request.GET['name']
        search_staff = Staff.objects.filter(name=search_name)
    staff = Staff.objects.order_by('id')
    return render(request, 'erp_1/personnel_management.html', locals())


def department_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    departments = Department.objects.order_by('id')
    return render(request, 'erp_1/department_management.html', locals())


def material_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '生产员' in request.session['role']:
        right = True

    if 'id' in request.GET and request.GET['id']:
        search_id = request.GET['id']
        search_materials = Materials.objects.filter(id=search_id)
    if 'name' in request.GET and request.GET['name']:
        search_name = request.GET['name']
        search_materials = Materials.objects.filter(name=search_name)
    materials = Materials.objects.order_by('id')
    return render(request, 'erp_1/material_management.html', locals())


def FlowOfProduction_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '生产员' in request.session['role']:
        right = True

    if 'leading_man' in request.GET and request.GET['leading_man']:
        search_leading_man = request.GET['leading_man']
        search_flow = FlowOfProduction.objects.filter(leading_man=search_leading_man)
    if 'name' in request.GET and request.GET['name']:
        search_name = request.GET['name']
        search_flow = FlowOfProduction.objects.filter(name=search_name)
    flows = FlowOfProduction.objects.all()
    return render(request, 'erp_1/FlowOfProduction_management.html', locals())


def process_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '生产员' in request.session['role']:
        right = True

    if 'name' in request.GET and request.GET['name']:
        search_name = request.GET['name']
        search_process = ProductionProcess.objects.filter(name=search_name)
    processes = ProductionProcess.objects.all()
    return render(request, 'erp_1/ProductionProcess_management.html', locals())


def BOM_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '生产员' in request.session['role']:
        right = True

    if 'id' in request.GET and request.GET['id']:
        search_id = request.GET['id']
        search_bom = Bom.objects.filter(id=search_id)
    boms = Bom.objects.order_by('id')
    return render(request, 'erp_1/BOM_management.html', locals())


def add_people(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')

    departments = Department.objects.all()
    id_ordered = '>' + Staff.objects.order_by('id').last().id
    if request.POST:
        try:
            staff = Staff(id=request.POST['id'],
                          name=request.POST['name'],
                          gender=request.POST['gender'],
                          department=Department.objects.get(name=request.POST['department']),
                          on_the_job=True,
                          qualification=request.POST['qualification'],
                          native_place=request.POST['native_place'],
                          post=request.POST['post'],
                          level=request.POST['level'],
                          phone_number=request.POST['phone_number'],
                          nation=request.POST['nation'],
                          seniority=0,
                          mail=request.POST['mail'],
                          )
            staff.save()
        except:pass
        return redirect('/erp_1/personnelmanagement/')
    else:
        return render(request, 'erp_1/add_people.html', locals())


def delete_people(request):
    if request.POST:
        # try:
        Staff.objects.filter(id=request.POST['id']).delete()
        # except:pass
    return redirect('/erp_1/personnelmanagement/')


def staff_detail(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')

    if request.POST:
        staff = Staff.objects.get(id=id)
        staff.name = request.POST['name']
        staff.gender = request.POST['gender']
        if request.POST['department'] != 'None':
            staff.department = Department.objects.get(name=request.POST['department'])
        staff.on_the_job = request.POST['on_the_job']
        staff.qualification = request.POST['qualification']
        staff.native_place = request.POST['native_place']
        staff.post = request.POST['post']
        staff.level = request.POST['level']
        staff.phone_number = request.POST['phone_number']
        staff.nation = request.POST['nation']
        staff.seniority = request.POST['seniority']
        staff.mail = request.POST['mail']
        staff.save()
        return redirect('/erp_1/personnelmanagement/')
    departments = Department.objects.all()
    staff = Staff.objects.get(id=id)
    gender_flag = (staff.gender=='男')
    return render(request, 'erp_1/StaffDetail.html', locals())


def add_materials(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')

    id_ordered = '>' + Materials.objects.order_by('id').last().id
    if request.POST:
        try:
            if request.POST['type']=='自产':
                is_buy = False
            else:
                is_buy = True
            material = Materials(id=request.POST['id'],
                                 name=request.POST['name'],
                                 type=request.POST['type'],
                                 specification=request.POST['specification'],
                                 Quota=request.POST['Quota'],
                                 safety_stock_quantity=request.POST['safety_stock_quantity'],
                                 item=request.POST['item'],
                                 is_buy=is_buy,
                                 )
            material.save()
        except:pass
        return redirect('/erp_1/material_management/')
    else:
        return render(request, 'erp_1/add_materials.html', locals())


def material_detail(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')

    if request.POST:
        material = Materials.objects.get(id=id)
        material.name = request.POST['name']
        material.type = request.POST['type']
        material.specification = request.POST['specification']
        material.Quota = request.POST['Quota']
        material.safety_stock_quantity = request.POST['safety_stock_quantity']
        if request.POST['type'] == '自产':
            is_buy = False
        else:
            is_buy = True
        material.is_buy = is_buy
        material.save()
        return redirect('/erp_1/material_management/')
    material = Materials.objects.get(id=id)
    type_flag = (material.type=='外购')
    return render(request, 'erp_1/MaterialsDetail.html', locals())


def delete_materials(request):
    if request.POST:
        try:
            Materials.objects.filter(id=request.POST['id']).delete()
        except:pass
    return redirect('/erp_1/material_management/')


def add_BOM(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')

    id_ordered = '>' + Bom.objects.order_by('id').last().id
    if request.POST:
        try:
            bom = Bom(id=request.POST['id'],
                      materials=Materials.objects.get(name=request.POST['material']),
                      parent_code=request.POST['parent_code'],
                      leadtime=request.POST['leadtime'],
                      consumption=request.POST['consumption'],
                      bom_level=request.POST['bom_level'],
                      )
            bom.save()
        except:pass
        return redirect('/erp_1/BOM_management/')
    materials = Materials.objects.all()
    return render(request, 'erp_1/add_BOM.html', locals())


def BOM_detail(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')

    if request.POST:
        bom = Bom.objects.get(id=id)
        bom.materials = Materials.objects.get(name=request.POST['material'])
        bom.parent_code = request.POST['parent_code']
        bom.leadtime = request.POST['leadtime']
        bom.consumption = request.POST['consumption']
        bom.bom_level = request.POST['bom_level']
        bom.save()
        return redirect('/erp_1/BOM_management/')
    bom = Bom.objects.get(id=id)
    materials = Materials.objects.all()
    return render(request, 'erp_1/BOMDetail.html', locals())


def delete_BOM(request):
    if request.POST:
        try:
            Bom.objects.filter(id=request.POST['id']).delete()
        except:pass
    return redirect('/erp_1/BOM_management/')


def add_flow(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')

    if request.POST:
        try:
            flow = FlowOfProduction(id=request.POST['id'],
                                    name=request.POST['name'],
                                    leading_man=request.POST['leading_man'],
                                    required_time=request.POST['required_time'],
                                    note=request.POST['note'],
                                    )
            flow.save()
        except:
            pass
        return redirect('/erp_1/FlowOfProduction_management/')
    return render(request, 'erp_1/add_flow.html', locals())


def flow_detail(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')

    flow = FlowOfProduction.objects.get(id=id)
    staff = Staff.objects.filter(department=Department.objects.get(name='生产'))
    chain = flow.productionChain
    processes = ProductionProcess.objects.all()
    process = []
    process.append(chain)
    while chain.next:
        chain = chain.next
        process.append(chain)
    process = list(zip(range(1, len(process)+1), process))
    if request.POST:
        if 'id' in request.POST and request.POST['id']:
            flow = FlowOfProduction.objects.get(id=id)
            flow.name = request.POST['name']
            flow.leading_man = Staff.objects.get(name=request.POST['leading_man'])
            flow.required_time = request.POST['required_time']
            flow.note = request.POST['note']
            flow.save()
        if '1' in request.POST and request.POST['1']:
            for i, chain in process:
                chain.process = ProductionProcess.objects.get(id=request.POST[i])
        return redirect('/erp_1/FlowOfProduction_management/')
    return render(request, 'erp_1/Flow_detail.html', locals())

def delete_flow(request):
    if request.POST:
        pass
        # ProductionProcess.objects.filter(id=request.POST['id']).delete()
    return redirect('/erp_1/ProductionProcess_management/')


def add_process(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')

    id_ordered = '>' + ProductionProcess.objects.order_by('id').last().id
    if request.POST:
        # try:
        if 1:
            process = ProductionProcess(
                id=request.POST['id'],
                name=request.POST['name'],
                materials=Materials.objects.get(name=request.POST['materials']),
                leading_man=Staff.objects.get(name=request.POST['leading_man']),
                required_time=request.POST['required_time'],
                note=request.POST['note'],
            )
            process.save()
        # except:
        #     pass
        return redirect('/erp_1/ProductionProcess_management/')
    materials = Materials.objects.all()
    staff = Staff.objects.filter(department=Department.objects.get(name='生产'))
    return render(request, 'erp_1/add_process.html', locals())


def process_detail(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')

    materials = Materials.objects.all()
    staff = Staff.objects.filter(department=Department.objects.get(name='生产'))
    if request.POST:
        process = ProductionProcess.objects.get(id=id)
        process.id = request.POST['id']
        process.name = request.POST['name']
        process.materials = Materials.objects.get(name=request.POST['materials'])
        process.leading_man = Staff.objects.get(name=request.POST['leading_man'])
        process.required_time = request.POST['required_time']
        process.note = request.POST['note']
        process.save()
        return redirect('/erp_1/ProductionProcess_management/')
    process = ProductionProcess.objects.get(id=id)
    return render(request, 'erp_1/ProcessDetail.html', locals())

def delete_process(request):
    if request.POST:
        ProductionProcess.objects.filter(id=request.POST['id']).delete()
    return redirect('/erp_1/ProductionProcess_management/')
