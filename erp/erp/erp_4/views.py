from django.shortcuts import render, redirect
from django.contrib import messages

#验证用户
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from .models import *
from erp_1.models import Staff, Department,Materials
from erp_6.models import App








def zhizaodingdan1(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '计划员' in request.session['role']:
       right = True
    if 'id' in request.GET and request.GET['id']:
        search_id = request.GET['id']
        search_zhizaodingdan = zhizaodingdan.objects.filter(id=search_id)
    if 'huohao' in request.GET and request.GET['huohao']:
        search_huohao = request.GET['huohao']
        search_zhizaodingdan = zhizaodingdan.objects.filter(huohao = search_huohao)
    Zhizaodingdan = zhizaodingdan.objects.order_by('id')
    return render(request, 'erp_4/zhizaodingdan.html', locals())

def paigongdan1(request):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')
    #if 'role' in request.session and '计划员' in request.session['role']:
       # right = True
    if 'role' in request.session and '计划员' in request.session['role']:
       right = True
    if 'id' in request.GET and request.GET['id']:
        search_id = request.GET['id']
        search_paigongdan = paigongdan.objects.filter(id=search_id)
    Paigongdan = paigongdan.objects.order_by('id')
    return render(request, 'erp_4/paigongdan.html', locals())

def jianyandan1(request):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')
   # if 'role' in request.session and '计划员' in request.session['role']:
       # right = True
    if 'role' in request.session and '计划员' in request.session['role']:
       right = True
    if 'id' in request.GET and request.GET['id']:
        search_id = request.GET['id']
        search_jianyandan = jianyandan.objects.filter(id=search_id)
    Jianyandan = jianyandan.objects.order_by('id')
    return render(request, 'erp_4/jianyandan.html', locals())

def kudan1(request):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')
   # if 'role' in request.session and '计划员' in request.session['role']:
       # right = True
    if 'role' in request.session and '计划员' in request.session['role']:
       right = True
    if 'app_id' in request.GET and request.GET['app_id']:
        search_id = request.GET['app_id']
        search_App = App.objects.filter(app_id=search_id)
    ios = []
    APP = App.objects.order_by('app_id')
    for app in APP:
        if app.io == '1':
            ios.append(True)
        if app.io == '0':
            ios.append(False)
    io_app = zip(APP, ios)
    return render(request, 'erp_4/kudan.html', locals())

def personnel_management(request):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')

    department = Department.objects.get(name='车间')
    staff = Staff.objects.filter(department=department)

    return render(request, 'erp_4/personnel_management.html', locals())

def add_zhizaodingdan(request):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')
    Materialss = Materials.objects.all()
    if request.POST:
        # try:
        id_list = []
        if zhizaodingdan.objects.all():
            for Zhizaodingdan1 in zhizaodingdan.objects.all():
                id_list.append(int(Zhizaodingdan1.id))
        else:
            id_list.append(0)
        Zhizaodingdan = zhizaodingdan(id=str(max(id_list) + 1).zfill(6),
                                      huohao=Materials.objects.get(id=request.POST['huohao']),
                                      piliang=request.POST['piliang'],
                                      chejianbianhao=request.POST['chejianbianhao'],
                                      shijian=request.POST['shijian'],
                                      )
        Zhizaodingdan.save()
        # except:pass
        return redirect('/erp_4/zhizaodingdan/')
    else:
        return render(request, 'erp_4/add_zhizaodingdan.html', locals())




def add_paigongdan(request):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')
    jiagongzhongxins = jiagongzhongxin.objects.all()
    Materialss = Materials.objects.all()
    Staffs = Staff.objects.all()
    if request.POST:
        id_list = []
        if paigongdan.objects.all():
            for Paigongdan1 in paigongdan.objects.all():
                        id_list.append(int(Paigongdan1.id))
        else:
            id_list.append(0)

        Paigongdan = paigongdan(id=str(max(id_list) + 1).zfill(6),
                                jiagongzhongxin_id=jiagongzhongxin.objects.get(id=request.POST['jiagongzhongxin_id']),
                                wuliaobianhao=Materials.objects.get(id=request.POST['wuliaobianhao']),
                                pgid=Staff.objects.get(id=request.POST['pgid']),
                                shijian=request.POST['shijian'],
                                      )
        Paigongdan.save()
        # except:pass
        return redirect('/erp_4/paigongdan/')
    else:
        return render(request, 'erp_4/add_paigongdan.html', locals())

def add_kudan(request):

    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')
    staffs = Staff.objects.all()
    Materialss = Materials.objects.all()
    if request.POST:
        # try:
        id_list = []
        if App.objects.all():
            for app in App.objects.all():
                id_list.append(int(app.app_id))
        else:
            id_list.append(0)
        APP = App(app_id=str(max(id_list) + 1).zfill(6),
                                io=request.POST['io'],
                                goods_id=request.POST['goods_id'],
                                goods_name=Materials.objects.get(id=request.POST['goods_id']).name,
                                demand=request.POST['demand'],
                                demand_io=request.POST['demand_io'],
                                date_app=request.POST['date_app'],
                                date_io=request.POST['date_io'],
                                applicant=Staff.objects.get(id=request.POST['applicant']),
                                      )
        APP.save()
        # except:pass

        return redirect('/erp_4/kudan/')
    else:
        return render(request, 'erp_4/add_kudan.html', locals())


def delete_zhizaodingdan(request):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')

    if request.POST:
        # try:
        zhizaodingdan.objects.filter(id=request.POST['id']).delete()
        # except:pass
    return redirect('/erp_4/zhizaodingdan/')

def delete_paigongdan(request):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')

    if request.POST:
        # try:
        paigongdan.objects.filter(id=request.POST['id']).delete()
        # except:pass
    return redirect('/erp_4/paigongdan/')

def delete_jianyandan(request):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')

    if request.POST:
        # try:
        jianyandan.objects.filter(id=request.POST['id']).delete()
        # except:pass
    return redirect('/erp_4/jianyandan/')

def delete_kudan(request):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')

    if request.POST:
        # try:
        App.objects.filter(app_id=request.POST['app_id']).delete()
        # except:pass
    return redirect('/erp_4/kudan/')

def zhizaodingdan_detail(request, id):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')
    Materialss = Materials.objects.all()
    if request.POST:
        Zhizaodingdan = zhizaodingdan.objects.get(id=id)
        if request.POST['huohao'] != 'None':
            Zhizaodingdan.huohao= Materials.objects.get(id=request.POST['huohao'])
        Zhizaodingdan.piliang = request.POST['piliang']
        Zhizaodingdan.chejianbianhao = request.POST['chejianbianhao']
        Zhizaodingdan.shijian = request.POST['shijian']
        Zhizaodingdan.save()
        return redirect('/erp_4/zhizaodingdan/')
    Zhizaodingdan = zhizaodingdan.objects.get(id=id)
    return render(request, 'erp_4/zhizaodingdanDetail.html', locals())

def paigongdan_detail(request, id):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')
    if 'role' in request.session and '计划员' in request.session['role']:
            right = True
    if request.POST:
        Paigongdan = paigongdan.objects.get(id=id)

        if request.POST['jiagongzhongxin_id'] != 'None':
            Paigongdan.jiagongzhongxin_id = jiagongzhongxin.objects.get(id=request.POST['jiagongzhongxin_id'])

        if request.POST['wuliaobianhao'] != 'None':
            Paigongdan.wuliaobianhao= Materials.objects.get(id=request.POST['wuliaobianhao'])
        if request.POST['pgid'] != 'None':
            Paigongdan.pgid= Staff.objects.get(id=request.POST['pgid'])
        Paigongdan.shijian = request.POST['shijian']
        Paigongdan.save()
        return redirect('/erp_4/paigongdan/')
    Paigongdan = paigongdan.objects.get(id=id)
    jiagongzhongxins = jiagongzhongxin.objects.all()
    Materialss = Materials.objects.all()
    Staffs = Staff.objects.all()
    return render(request, 'erp_4/paigongdanDetail.html', locals())

def jianyandan_detail(request, id):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')
    if request.POST:
        j = bool(int(request.POST['jieguo']))
        Jianyandan = jianyandan.objects.get(id=id)

        if request.POST['wuliaobianhao'] != 'None':
            print('大家都觉得就')
            Jianyandan.wuliaobianhao = Materials.objects.get(id=request.POST['wuliaobianhao'])

        if request.POST['jiagongzongxin_id'] != 'None':
            Jianyandan.jiagongzongxin_id = jiagongzhongxin.objects.get(id=request.POST['jiagongzongxin_id'])
        if request.POST['jyrid'] != 'None':
            Jianyandan.jyrid = Staff.objects.get(id=request.POST['jyrid'])

        Jianyandan.chejianid = request.POST['chejianid']
        Jianyandan.shijian = request.POST['shijian']
        Jianyandan.shuliang = request.POST['shuliang']
        Jianyandan.jieguo = j
        Jianyandan.save()
        return redirect('/erp_4/jianyandan/')
    Jianyandan = jianyandan.objects.get(id=id)
    jiagongzhongxins = jiagongzhongxin.objects.all()
    Materialss = Materials.objects.all()
    Staffs = Staff.objects.all()
    return render(request, 'erp_4/jianyandanDetail.html', locals())

def kudan_detail(request, app_id):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')
    if request.POST:
        APP = App.objects.get(app_id=app_id)
        APP.io = request.POST['io']

        APP.goods_id = request.POST['goods_id']
        APP.demand = request.POST['demand']
        APP.demand_io = request.POST['demand_io']
        APP.date_app = request.POST['date_app']
        APP.date_io = request.POST['date_io']
        if request.POST['applicant'] != 'None':

            APP.applicant = Staff.objects.get(id=request.POST['applicant'])
        APP.save()
        return redirect('/erp_4/kudan/')
    APP = App.objects.get(app_id=app_id)
    staffs = Staff.objects.all()
    Materialss = Materials.objects.all()
    return render(request, 'erp_4/kudanDetail.html', locals())

def add_jianyandan(request):
    if 'is_login' not in request.session or request.session['is_login'] != True:
        return redirect('/login/')
    jiagongzhongxins = jiagongzhongxin.objects.all()
    Materialss = Materials.objects.all()
    Staffs = Staff.objects.all()
    if request.POST:
        j = bool(int(request.POST['jieguo']))
        id_list = []
        if jianyandan.objects.all():
            for Jianyandan1 in jianyandan.objects.all():
                id_list.append(int(Jianyandan1.id))
        else:
            id_list.append(0)
        Jianyandan = jianyandan(id=str(max(id_list) + 1).zfill(6),
                                wuliaobianhao=Materials.objects.get(id =request.POST['wuliaobianhao']),

                                jiagongzongxin_id=jiagongzhongxin.objects.get(id =request.POST['jiagongzongxin_id']),
                                jyrid=Staff.objects.get(id=request.POST['jyrid']),

                                chejianid=request.POST['chejianid'],
                                shijian=request.POST['shijian'],
                                shuliang=request.POST['shuliang'],
                                jieguo=j,
                                )
        Jianyandan.save()
        # except:pass
        return redirect('/erp_4/jianyandan/')
    else:
        return render(request, 'erp_4/add_jianyandan.html', locals())








