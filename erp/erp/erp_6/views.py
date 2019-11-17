from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from .models import *
from erp_1.models import *
from erp_4.models import *
from erp_5.models import *
from datetime import date, datetime, timedelta
from django.db.models import Q


def WMS1(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if 'role' in request.session and '库存员' in request.session['role']:
        right = True
    if 'goods_id' in request.GET and request.GET['goods_id']:
        search_goods_id = request.GET['goods_id']
        search_wms = WMS.objects.filter(goods_id=search_goods_id)
    WMS.objects.all().delete()
    locations_t = []
    goo = Goods.objects.all()
    for g in goo:
        locations_t.append(g.location)
    locations = list(set(locations_t))

    for l in locations:
        WMSs = Goods.objects.filter(location=str(l))
        a = 0
        for W in WMSs:
            a = a + W.amount
            wms = WMS(WMS_id=W.WMS_id,
                         location=W.location,
                         goods_id=W.goods_id,
                         goods_name=W.goods_name,
                         norms=W.norms,
                         employ=a,
                         ratio=a/10000,
                         charger_id=W.charger_id,
                         charger_name=Staff.objects.get(id=W.charger_id).name,
                         )
        wms.save()
    WMSs1 = WMS.objects.all()
    wms = WMS.objects.order_by('location')
    # WMSs = WMS.objects.all()
    return render(request, 'erp_6/WMS.html', locals())


# def add_wms1(request):
#     if 'is_login' not in request.session or request.session['is_login']!=True:
#         redirect('/login/')
#     if request.POST:
#         # try:
#         if 1:
#             wms = WMS(WMS_id = request.POST['WMS_id'],
#                     location = request.POST['location'],
#                     goods_id = request.POST['goods_id'],
#                     goods_name = request.POST['goods_name'],
#                     norms = request.POST['norms'],
#                     volume = request.POST['volume'],
#                     employ = request.POST['employ'],
#                     ratio = request.POST['ratio'],
#                     charger_id = request.POST['charger_id'],
#                     charger_name = request.POST['charger_name'],
#                           )
#             wms.save()
#         # except:pass
#         return redirect('/erp_6/WMS/')
#     else:
#         return render(request, 'erp_6/add_wms.html', locals())


def delete_wms1(request):
    if request.POST:
        # try:
        WMS.objects.filter(location=request.POST['location']).delete()
        # except:pass
    return redirect('/erp_6/WMS/')


def WMSdetail1(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if request.POST:
        wms = WMS.objects.get(location=id)
        wms.WMS_id = request.POST['WMS_id']
        wms.location = request.POST['location']
        wms.goods_id = request.POST['goods_id']
        wms.goods_name = request.POST['goods_name']
        wms.norms = request.POST['norms']
        wms.volume = request.POST['volume']
        wms.employ = request.POST['employ']
        wms.ratio = request.POST['ratio']
        wms.charger_id = request.POST['charger_id']
        wms.charger_name = request.POST['charger_name']
        wms.save()
        return redirect('/erp_6/WMS/')
    wms = WMS.objects.get(location=id)
    return render(request, 'erp_6/WMSdetail.html/', locals())


def Goods1(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    Goods.objects.all().delete()
    Goodss = Change.objects.all()
    for C in Goodss:
        G = App.objects.get(app_id=C.app_id)
        if G.io == '0':
            good = Goods(id=G.app_id,
                goods_id=G.goods_id,
                goods_name=G.goods_name,
                norms=G.norms,
                WMS_id=C.WMS_id,
                location=C.location,
                amount_app=0-G.demand,
                amount=0-G.demand_io,
                date_in=G.date_io,
                time=500,
                date_line=G.date_io + timedelta(days=500),
                charger_id=G.charger_id,
                charger_name=Staff.objects.get(id=G.charger_id).name,
                deal=500 - (date.today() - G.date_io).days,
                     )
            # print('加粉快点哈萨克', 500 - (date.today() - G.date_io).days, '爱仕达快递费', )
        else:
            good = Goods(id=G.app_id,
                goods_id=G.goods_id,
                goods_name=G.goods_name,
                norms=G.norms,
                WMS_id=C.WMS_id,
                location=C.location,
                amount_app=G.demand,
                amount=G.demand_io,
                date_in=G.date_io,
                time=500,
                date_line=G.date_io + timedelta(days=500),
                charger_id=G.charger_id,
                charger_name=Staff.objects.get(id=G.charger_id).name,
                deal=500 - (date.today() - G.date_io).days,
                    )
            # print('加粉快点哈萨克', 500-(date.today() - G.date_io).days, '爱仕达快递费',)
        good.save()
    Goodss1 = Goods.objects.all()

    return render(request, 'erp_6/Goods.html', locals())


def Check1(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if 'role' in request.session and '库存员' in request.session['role']:
        right = True
    if 'goods_id' in request.GET and request.GET['goods_id']:
        search_goods_id = request.GET['goods_id']
        search_check = Check.objects.filter(goods_id=search_goods_id)
    if 'goods_name' in request.GET and request.GET['goods_name']:
        search_goods_name = request.GET['goods_name']
        search_check = Check.objects.filter(goods_name=search_goods_name)
    Checks = Check.objects.all()
    return render(request, 'erp_6/Check.html', locals())


def add_check1(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if request.POST:
        scheck = Goods.objects.filter(goods_id=request.POST['goods_id'])
        a, b, c = 0, 0, 0
        for sch in scheck:
            e = sch.norms
            a = a+sch.amount
            if sch.amount==0 and sch.amount_app>0:
                b = b+sch.amount_app
            if sch.amount==0 and sch.amount_app<0:
                c = c-sch.amount_app
            # try:
            if 1:
                d = datetime.strftime(datetime.now(), '%Y%m%d')+request.POST['goods_id']
                check = Check(id=d,
                              goods_id=request.POST['goods_id'],
                              goods_name=Materials.objects.get(id=request.POST['goods_id']).name,
                              # norms=request.POST['norms'],
                              norms=e,
                              characteristic=request.POST['characteristic'],
                              value=request.POST['value'],
                              date=datetime.now(),
                              order_point=1000,
                              pur=Materials.objects.get(id=request.POST['goods_id']).type,
                              state=request.POST['state'],
                              stock_now=a,
                              stock_way=b,
                              stock_secure=Materials.objects.get(id=request.POST['goods_id']).safety_stock_quantity,
                              stock_real=request.POST['stock_real'],
                              stock_free=a-c-Materials.objects.get(id=request.POST['goods_id']).safety_stock_quantity,
                              unit=request.POST['unit'],
                              charger_id=request.POST['charger_id'],
                              charger_name=Staff.objects.get(id=request.POST['charger_id']).name,
                              )
                check.save()
        # except:pass
        return redirect('/erp_6/Check/')
    else:
        return render(request, 'erp_6/add_check.html', locals())


def delete_check1(request):
    if request.POST:
        # try:
        Check.objects.filter(id=request.POST['id']).delete()
        # except:pass
    return redirect('/erp_6/Check/')


def checkdetail1(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if request.POST:
        check = Check.objects.get(id=id)
        check.id = request.POST['id']
        check.goods_id = request.POST['goods_id']
        check.goods_name = request.POST['goods_name']
        check.norms = request.POST['norms']
        check.characteristic = request.POST['characteristic']
        check.value = request.POST['value']
        check.date = datetime.now()
        check.order_point = request.POST['order_point']
        check.pur = request.POST['pur']
        check.stock_now = request.POST['stock_now']
        check.stock_way = request.POST['stock_way']
        check.stock_secure = request.POST['stock_secure']
        check.stock_real = request.POST['stock_real']
        check.stock_free = request.POST['stock_free']
        check.unit = request.POST['unit']
        check.charger_id = request.POST['charger_id']
        check.charger_name = request.POST['charger_name']
        check.save()
        return redirect('/erp_6/Check/')
    check = Check.objects.get(id=id)
    return render(request, 'erp_6/checkDetail.html/', locals())


def App1(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if 'goods_id' in request.GET and request.GET['goods_id']:
        search_goods_id = request.GET['goods_id']
        search_app = App.objects.filter(goods_id=search_goods_id)
    if 'applicant.depart' in request.GET and request.GET['applicant.depart']:
        search_applicant_depart = request.GET['applicant.depart']
        search_app = App.objects.filter(applicant_depart=search_applicant_depart)
    # for app in App.objects.all():
    #     if app.goods_id == '':
    #         app.goods_id = Materials.objects.get(id=app.goods_name).id,
    #     else:
    #         app.goods_name = Materials.objects.get(id=app.goods_id).name,
    #     app.save()
    Apps = App.objects.all()
    return render(request, 'erp_6/App.html', locals())


def add_app1(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if request.POST:
        # try:
        if 1:
            id_list = []
            if App.objects.all():
                for app in App.objects.all():
                    id_list.append(int(app.app_id))
            else:
                id_list.append(0)
            app = App(app_id=str(max(id_list)+1).zfill(6),
                          io=request.POST['io'],
                          goods_id=request.POST['goods_id'],
                          goods_name=Materials.objects.get(id=request.POST['goods_id']).name,
                          norms=request.POST['norms'],
                          demand=request.POST['demand'],
                          demand_io=request.POST['demand_io'],
                          date_app=request.POST['date_app'],
                          date_io=request.POST['date_io'],
                          applicant_id=request.POST['applicant_id'],
                          applicant=Staff.objects.get(id=request.POST['applicant_id']),
                          # applicant_name=request.POST['applicant.name'],
                          # applicant_tel=request.POST['applicant.tel'],
                          # applicant_depart=request.POST['applicant.depart'],
                          charger_id=request.POST['charger_id'],
                          charger=Staff.objects.get(id=request.POST['charger_id']),
                          state=request.POST['state'],
                          )
            app.save()
        # except:pass
        return redirect('/erp_6/App/')
    else:
        return render(request, 'erp_6/add_app.html', locals())


def delete_app1(request):
    if request.POST:
        # try:
        App.objects.filter(app_id=request.POST['app_id']).delete()
        # except:pass
    return redirect('/erp_6/App/')


def appdetail1(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if request.POST:
        app = App.objects.get(app_id=id)
        app.app_id = request.POST['app_id']
        app.io = request.POST['io']
        app.goods_id = request.POST['goods_id']
        app.norms = request.POST['norms']
        app.demand = request.POST['demand']
        app.demand_io = request.POST['demand_io']
        # app.date_app = request.POST['date_app']
        app.date_io = request.POST['date_io']
        app.applicant_id = request.POST['applicant_id']
        app.applicant_name = request.POST['applicant_name']
        app.applicant_tel = request.POST['applicant_tel']
        app.applicant_depart = request.POST['applicant_depart']
        app.charger_id = request.POST['charger_id']
        app.state = request.POST['state']
        app.save()
        return redirect('/erp_6/App/')
    app = App.objects.get(app_id=id)
    return render(request, 'erp_6/appDetail.html/', locals())


def Move1(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if 'role' in request.session and '库存员' in request.session['role']:
        right = True
    Moves = Move.objects.all()
    return render(request, 'erp_6/Move.html', locals())


def add_move1(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if request.POST:
        # try:
        if 1:
            move = Move(goods_id=WMS.objects.get(location=request.POST['out_location']).goods_id,
                            goods_name=WMS.objects.get(location=request.POST['out_location']).goods_name,
                            WMS_out_id=WMS.objects.get(location=request.POST['out_location']).WMS_id,
                            out_location=request.POST['out_location'],
                            WMS_in_id=WMS.objects.get(location=request.POST['in_location']).WMS_id,
                            in_location=request.POST['in_location'],
                            charger_out_id=WMS.objects.get(location=request.POST['out_location']).charger_id,
                            charger_out_name=WMS.objects.get(location=request.POST['out_location']).charger_name,
                            charger_in_id=WMS.objects.get(location=request.POST['in_location']).charger_id,
                            charger_in_name=WMS.objects.get(location=request.POST['in_location']).charger_name,
                          )
            a = move.WMS_out_id
            b = move.out_location
            c = move.WMS_in_id
            d = move.in_location
            if 1:
                id_list = []
                if App.objects.all():
                    for app in App.objects.all():
                        id_list.append(int(app.app_id))
                else:
                    id_list.append(0)
                app = App(app_id=str(max(id_list) + 1).zfill(6),
                          io='0',
                          goods_id=move.goods_id,
                          goods_name=move.goods_name,
                          norms=WMS.objects.get(location=move.out_location).norms,
                          demand=WMS.objects.get(location=move.out_location).employ,
                          demand_io=WMS.objects.get(location=move.out_location).employ,
                          date_app=datetime.now(),
                          date_io=datetime.now(),
                          applicant_id=move.charger_in_id,
                          applicant=Staff.objects.get(id=move.charger_in_id),
                          # applicant_name=request.POST['applicant.name'],
                          # applicant_tel=request.POST['applicant.tel'],
                          # applicant_depart=request.POST['applicant.depart'],
                          charger_id=move.charger_out_id,
                          charger=Staff.objects.get(id=move.charger_out_id),
                          state='是',
                          )
                app.save()
                change = Change(app_id=str(max(id_list) + 1).zfill(6),
                          WMS_id=a,
                          location=b,
                          )
                change.save()

            if 1:
                id_list = []
                if App.objects.all():
                    for app in App.objects.all():
                        id_list.append(int(app.app_id))
                else:
                    id_list.append(0)
                app = App(app_id=str(max(id_list) + 1).zfill(6),
                          io='1',
                          goods_id=move.goods_id,
                          goods_name=move.goods_name,
                          norms=WMS.objects.get(location=move.out_location).norms,
                          demand=WMS.objects.get(location=move.out_location).employ,
                          demand_io=WMS.objects.get(location=move.out_location).employ,
                          date_app=datetime.now(),
                          date_io=datetime.now(),
                          applicant_id=move.charger_out_id,
                          applicant=Staff.objects.get(id=move.charger_out_id),
                          # applicant_name=request.POST['applicant.name'],
                          # applicant_tel=request.POST['applicant.tel'],
                          # applicant_depart=request.POST['applicant.depart'],
                          charger_id=move.charger_in_id,
                          charger=Staff.objects.get(id=move.charger_in_id),
                          state='是',
                          )
                app.save()
                change = Change(app_id=str(max(id_list) + 1).zfill(6),
                                WMS_id=c,
                                location=d,
                                )
                change.save()
            move.save()
        # except:pass
        return redirect('/erp_6/Move/')
    else:
        return render(request, 'erp_6/add_move.html', locals())


def Change1(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if 'role' in request.session and '库存员' in request.session['role']:
        right = True
    if 'app_id' in request.GET and request.GET['app_id']:
        search_app_id = request.GET['app_id']
        search_change = Change.objects.filter(app_id=search_app_id)
    # if App.objects.all.filter(~Q(demand_io=0))
    #     Changes = App.objects.all()
    Changes = Change.objects.all()
    return render(request, 'erp_6/Change.html', locals())


def add_change1(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if request.POST:
        # try:
        if 1:
            change = Change(app_id=request.POST['app_id'],
                          WMS_id=request.POST['WMS_id'],
                          location=request.POST['location'],
                          )
            change.save()
        # except:pass
        return redirect('/erp_6/Change/')
    else:
        return render(request, 'erp_6/add_change.html', locals())


def delete_change1(request):
    if request.POST:
        # try:
        Change.objects.filter(app_id=request.POST['app_id']).delete()
        # except:pass
    return redirect('/erp_6/Change/')


def changeDetail1(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        redirect('/login/')
    if request.POST:
        change = Change.objects.get(app_id=id)
        change.app_id = request.POST['app_id']
        change.WMS_id = request.POST['WMS_id'],
        change.location = request.POST['location'],
        change.save()
        return redirect('/erp_6/Change/')
    change = Change.objects.get(app_id=id)
    return render(request, 'erp_6/changedetail.html/', locals())


def apply(request, id):
    # if request.POST:
    if Check.objects.get(id=id).pur == '外购':
        id_list = []
        if Detail.objects.all():
            for detail in Detail.objects.all():
                id_list.append(int(detail.id))
        else:
            id_list.append(0)
        to_buy = Check.objects.get(id=id)
        add_buy = Detail(id=str(max(id_list) + 1).zfill(6),
            applicant = to_buy.charger_name,
            department = '库存',
            send_time = datetime.now(),
            material_id = to_buy.goods_id,
            material_name = to_buy.goods_name,
            specifications = to_buy.norms,
            amount = ((10000-to_buy.stock_now)//Materials.objects.get(id=to_buy.goods_id).Quota)*Materials.objects.get(id=to_buy.goods_id).Quota,
            required_time = datetime.now() + timedelta(days=5),
        )
        add_buy.save()
    else:
        id_list = []
        if zhizaodingdan.objects.all():
            for Zhizaodingdan in zhizaodingdan.objects.all():
                id_list.append(int(Zhizaodingdan.id))
        else:
            id_list.append(0)
        to_do = Check.objects.get(id=id)
        add_do = zhizaodingdan(id=str(max(id_list) + 1).zfill(6),
                         huohao=Materials.objects.get(id=to_do.goods_id),
                         piliang=((10000-to_do.stock_now)//Materials.objects.get(id=to_do.goods_id).Quota)*Materials.objects.get(id=to_do.goods_id).Quota,
                         shijian=datetime.now() + timedelta(days=5),
                         )
        add_do.save()
    return redirect('/erp_6/Check/')
