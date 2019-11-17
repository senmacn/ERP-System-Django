from django.shortcuts import render, redirect
from .models import *
from erp_1.models import Materials, Bom
from erp_5.models import Detail
from erp_6.models import Check
from datetime import date, timedelta, datetime
import json
import urllib3
# Create your views here.


def MPS_manager(request):
    if 'is_login' not in request.session or request.session.get('is_login')!=True:
        return redirect('/login/')
    if 'role' in request.session and '计划员' in request.session['role']:
        right = True
    if 'id' in request.GET and request.GET['id']:
        search_id = request.GET['id']
        search_MPS = Mps_list.objects.filter(id=search_id)

    if 'name' in request.GET and request.GET['name']:
        search_name = request.GET['name']
        search_MPS = Mps_list.objects.filter(name=search_name)
    MPS = Mps_list.objects.order_by('id')

    return render(request, 'erp_3/MPS_manager.html', locals())


def MPS_alter(request, MPS_id):

    if Mps_list.objects.get(id=MPS_id):
        mps = Mps_list.objects.get(id=MPS_id)
        products = Product_list.objects.filter(forMps=MPS_id)
    if request.POST:
        mps.name = request.POST['name']
        mps.start_time = request.POST['start_time']
        mps.end_time = request.POST['end_time']
        mps.save()
        last_url = 'http://127.0.0.1:8000/erp_3/MPS_detail/'+MPS_id+'/'
        return redirect(last_url)
    return render(request, 'erp_3/MPS_alter.html', locals())


def product_alter(request, product_id):
    materials = Materials.objects.filter(item='产品')
    if Product_list.objects.get(id=product_id):
        product = Product_list.objects.get(id=product_id)
        if request.POST:
            product.product_id = request.POST['pro_alter']
            product.name = Materials.objects.get(id=request.POST['pro_alter']).name
            product.save()

            last_url = 'http://127.0.0.1:8000/erp_3/MPS_detail/'+product.forMps.id+'/'
            return redirect(last_url)
    return render(request, 'erp_3/product_alter.html', locals())


def product_delete(request, product_id):
    if Product_list.objects.get(id=product_id):
        TimeForProduct_list.objects.filter(forProduct=product_id).delete()
        mps_id = Product_list.objects.get(id=product_id).forMps.id
        Product_list.objects.get(id=product_id).delete()
        last_id = 'http://127.0.0.1:8000/erp_3/MPS_detail/'+mps_id+'/'
        return redirect(last_id)


def plan_alter(request, plan_id):
    if TimeForProduct_list.objects.get(id=plan_id):
        plan = TimeForProduct_list.objects.get(id=plan_id)
        mps_id = plan.forProduct.forMps.id
        if request.POST:
            plan.time = request.POST['time']
            plan.amount = request.POST['need']
            plan.save()
            last_url = 'http://127.0.0.1:8000/erp_3/MPS_detail/'+mps_id+'/'
            return redirect(last_url)

    return render(request, 'erp_3/plan_alter.html', locals())


def plan_add(request, product_id):
    if Product_list.objects.get(id=product_id):
        product = Product_list.objects.get(id=product_id)
        id_list = []
        if TimeForProduct_list.objects.all():
            for time in TimeForProduct_list.objects.all():
                id_list.append(int(time.id))
        else:
            id_list.append(0)
        if request.POST:
            plan = TimeForProduct_list(id=str(max(id_list)+1).zfill(6),
                                       time=request.POST['time'],
                                       amount=request.POST['need'],
                                       forProduct=product)
            plan.save()
    return render(request, 'erp_3/add_plan.html', locals())


def plan_delete(request, plan_id):
    if TimeForProduct_list.objects.get(id=plan_id):
        mps_id = TimeForProduct_list.objects.get(id=plan_id).forProduct.forMps.id
        TimeForProduct_list.objects.get(id=plan_id).delete()
        last_id = 'http://127.0.0.1:8000/erp_3/MPS_detail/'+mps_id+'/'
        return redirect(last_id)


def product_add(request, mps_id):
    if Mps_list.objects.get(id=mps_id):
        mps = Mps_list.objects.get(id=mps_id)
        is_add = False
        all_material = Materials.objects.filter(item='产品')
    if request.POST:
        try:
            if 'select_product' in request.POST:
                is_input = True
                if Product_list.objects.all():
                    for p in Product_list.objects.all():
                        if request.POST['select_product'] == p.product_id and p.forMps == mps:
                            raise ValueError
                id_list = []
                if Product_list.objects.all():
                    for pro in Product_list.objects.all():
                        id_list.append(int(pro.id))
                else:
                    id_list.append(0)
                id_key = str(max(id_list)+1).zfill(6)
                product = Product_list(id=id_key,
                                       product_id=request.POST['select_product'],
                                       name=Materials.objects.get(id=request.POST['select_product']).name,
                                       forMps=mps,
                                       )
                product.save()
                product = Product_list.objects.get(id=id_key)
                is_add = True

            if 'time' in request.POST:
                product = Product_list.objects.get(id=request.POST['id_key'])
                id_list = []
                if TimeForProduct_list.objects.all():
                    for time in TimeForProduct_list.objects.all():
                        id_list.append(int(time.id))
                else:
                    id_list.append(0)
                time_need = TimeForProduct_list(id=str(max(id_list)+1).zfill(6),
                                                time=request.POST['time'],
                                                amount=request.POST['need'],
                                                forProduct=product)
                time_need.save()
                is_add = True
        except ValueError:
            massage = '产品已存在！'
    return render(request, 'erp_3/add_product.html', locals())


def MPS_delete(request, MPS_id):
    if Mps_list.objects.get(id=MPS_id):
        products = Product_list.objects.filter(forMps=MPS_id)
        if products:
            for product in products:
                TimeForProduct_list.objects.filter(forProduct=product.id).delete()
        Product_list.objects.filter(forMps=MPS_id).delete()
        Mps_list.objects.get(id=MPS_id).delete()
    return redirect('http://127.0.0.1:8000/erp_3/MPS_manager/')


def MPS_add(request):
    try:
        is_add = False
        if request.POST:
            is_input = True
            if len(request.POST['id']) != 6:
                raise ZeroDivisionError
            for m in Mps_list.objects.all():
                if request.POST['id'] == m.id:
                    raise ValueError
            mps = Mps_list(id=request.POST['id'],
                           name=request.POST['name'],
                           start_time=request.POST['start_time'],
                           end_time=request.POST['end_time'],
                                   )
            mps.save()
            is_add = True
            massage = '提交成功！'
    except ZeroDivisionError:
        massage = "id必须为六位！"
    except ValueError:
        massage = "id冲突，提交失败！"
    return render(request, 'erp_3/add_MPS.html', locals())


def MPS_detail(request, MPS_id):

    if Mps_list.objects.get(id=MPS_id):
        mps = Mps_list.objects.get(id=MPS_id)
        products = []
        if 'id' in request.GET and request.GET['id']:
            search_id = request.GET['id']
            if len(search_id) == 6:
                product = Product_list.objects.get(id=search_id)
                if product and product.forMps.id == mps.id:
                    products.append(product)
        if 'name' in request.GET and request.GET['name']:
            search_name = request.GET['name']
            products_temp = Product_list.objects.filter(name=search_name)
            if products_temp:
                for product in products_temp:
                    if product.forMps.id == MPS_id:
                        products.append(product)
        if not products:
            products = Product_list.objects.filter(forMps=MPS_id)
        products_plan = []
        for product in products:
            product_item = TimeForProduct_list.objects.filter(forProduct=product.id)
            products_plan.append({"product": product, "plan": product_item})
        products = products_plan
    return render(request, 'erp_3/MPS_detail.html', locals())


def indent_create(request):
    if 'is_login' not in request.session or request.session.get('is_login')!=True:
        return redirect('/login/')
    if 'role' in request.session and '计划员' in request.session['role']:
        right = True
    else:
        if 'role' in request.session and '采购员' in request.session['role']:
            right = True
    if Mps_list.objects.all():
        select_mps = Mps_list.objects.all()
    if request.POST:
        mps = Mps_list.objects.get(id=request.POST["select_mps"])
        is_add = True
    return render(request, 'erp_3/indent_create.html', locals())


class Mater:

    def __init__(self):
        self.id = None
        self.ahead_time = None
        self.need_forone = None
        self.bom_id = None
        self.plans = []


class ProductLast:

    def __init__(self):
        self.id = None
        self.plans = []
        self.quota = None
        self.is_buy = None
        self.init_pab = None
        self.ahead_time = None


# def order_list(mps):
#     ma = Manufacture_apply.objects.filter(for_mps=mps)
#     i = 0
#     while i < len(ma) - 1:
#         j = i + 1
#         while j < len(ma):
#             if ma[j].product_id == ma[i].product_id:
#                 plans = TimeForManufacture_list.objects.filter(forProduct_id=ma[j].id)
#                 for plan in plans:
#                     plan.forProduct_id = ma[i].id
#                 ma[j].delete()
#                 j -= 1
#             j += 1
#         i += 1
#     i = 0
#     ma = Manufacture_apply.objects.filter(for_mps=mps)
#     pla = []
#     for ma_0 in ma:
#         pla_0 = TimeForManufacture_list.objects.filter(forProduct=ma_0)
#         pla.extend(pla_0)
#     while i < len(pla) - 1:
#         j = i + 1
#         while j < len(pla):
#             if pla[j].forProduct_id == pla[i].forProduct_id and pla[j].out_time == pla[i].out_time:
#                 pla[j].delete()
#                 j -= 1
#             j += 1
#         i += 1
#
#     ma = Purchase_apply.objects.filter(for_mps=mps)
#     i = 0
#     while i < len(ma) - 1:
#         j = i + 1
#         while j < len(ma):
#             if ma[j].product_id == ma[i].product_id:
#                 plans = TimeForPurchase_list.objects.filter(forProduct_id=ma[j].id)
#                 for plan in plans:
#                     plan.forProduct_id = ma[i].id
#                 ma[j].delete()
#                 j -= 1
#             j += 1
#         i += 1
#     i = 0
#     ma = Purchase_apply.objects.filter(for_mps=mps)
#     pla = []
#     for ma_0 in ma:
#         pla_0 = TimeForPurchase_list.objects.filter(forProduct=ma_0)
#         pla.extend(pla_0)
#     while i < len(pla) - 1:
#         j = i + 1
#         while j < len(pla):
#             if pla[j].forProduct_id == pla[i].forProduct_id and pla[j].time == pla[i].time:
#                 pla[j].delete()
#                 j -= 1
#             j += 1
#         i += 1


def result(all_list, mps):
    i = 0
    while i < len(all_list)-1:
        j = i+1
        while j < len(all_list):
            if all_list[j].id == all_list[i].id:
                all_list[i].plans.extend(all_list[j].plans)
                del all_list[j]
                j -= 1
            j += 1
        i += 1
    print('巨款那可是开始')
    for o in all_list:
        print('附件', o.id)
    i = 0
    while i < len(all_list):
        j = 0
        while j < len(all_list[i].plans)-1:
            t = j + 1
            while t < len(all_list[i].plans):
                if all_list[i].plans[t]['time'] == all_list[i].plans[j]['time']:
                    all_list[i].plans[j]['amount'] += all_list[i].plans[t]['amount']
                    del all_list[i].plans[t]
                    t -= 1
                t += 1
            j += 1
        i += 1

    for mater in all_list:
        for pl in mater.plans:
            if pl['amount'] == 0:
                del pl

    for mater in all_list:
        s = 0
        while s < len(mater.plans)-1:
            r = s+1
            while r < len(mater.plans):

                if int(mater.plans[r]['time']) < int(mater.plans[s]['time']):
                    temp = mater.plans[r]['time']
                    mater.plans[r]['time'] = mater.plans[s]['time']
                    mater.plans[s]['time'] = temp
                r += 1
            s += 1
    print('茶几上的可能产生看')
    for o in all_list:
        print('当时',o.id,'/n')
    all_materials = []
    for p in all_list:
        print('大好时机',p.id)
        material_infer = ProductLast()
        material_infer.id = p.id
        material_infer.quota = Materials.objects.get(id=p.id).Quota
        material_infer.is_buy = Materials.objects.get(id=p.id).is_buy
        material_infer.ahead_time = p.ahead_time
        now_date = date.today().strftime('%Y%m%d')
        amount_form = 0
        for ti in p.plans:
            if ti['time'] >= now_date:
                time_init = ti['time']
                break
            else:
                time_init = p.plans[-1]['time']
            amount_form += ti['amount']
        try:
            c = Check.objects.get(id=time_init+p.id)
            material_infer.init_pab = c.stock_free + c.stock_way
        except:
            material_infer.init_pab = 0
        material_infer.init_pab = material_infer.init_pab - amount_form
        if material_infer.init_pab < 0:
            return False
        material_infer.plans = p.plans
        all_materials.append(material_infer)

    for o in all_materials:
        print('计划好',o.id,'/n')

    if all_materials:

        purchase = Purchase_apply.objects.filter(for_mps=mps)
        for pu in purchase:
            TimeForPurchase_list.objects.filter(forProduct=pu).delete()
        purchase.delete()

        man = Manufacture_apply.objects.filter(for_mps=mps)
        for M in man:
            TimeForManufacture_list.objects.filter(forProduct=M).delete()
        man.delete()

        for m in all_materials:
            if m.is_buy:
                id_list = []
                if Purchase_apply.objects.all():
                    for pur0 in Purchase_apply.objects.all():
                        id_list.append(int(pur0.id))
                else:
                    id_list.append(0)
                name_0 = Materials.objects.get(id=m.id).name
                pur = Purchase_apply(id=str(max(id_list) + 1).zfill(6),
                                     product_id=m.id,
                                     name=name_0,
                                     for_mps=mps
                                     )
                pur.save()
                pab = m.init_pab
                for p in m.plans:

                    id_list = []
                    if TimeForPurchase_list.objects.all():
                        for pla0 in TimeForPurchase_list.objects.all():
                            id_list.append(int(pla0.id))
                    else:
                        id_list.append(0)
                    if pab >= p['amount']:
                        pab = pab - p['amount']
                        amount_0 = 0
                    else:
                        n = p['amount']-pab
                        if n % m.quota != 0:
                            amount_0 = (n // m.quota + 1)*m.quota
                            pab = amount_0 - n
                        else:
                            amount_0 = n
                            pab = 0

                    plan = TimeForPurchase_list(id=str(max(id_list) + 1).zfill(6),
                                                forProduct=pur,
                                                time=datetime.strptime(p['time'], '%Y%m%d'),
                                                amount=amount_0)
                    plan.save()
            else:

                id_list = []
                if Manufacture_apply.objects.all():
                    for manu0 in Manufacture_apply.objects.all():
                        id_list.append(int(manu0.id))
                else:
                    id_list.append(0)
                name_0 = Materials.objects.get(id=m.id).name
                manu = Manufacture_apply(id=str(max(id_list) + 1).zfill(6),
                                         product_id=m.id,
                                         name=name_0,
                                         for_mps=mps
                                         )
                manu.save()
                pab = m.init_pab
                for p in m.plans:

                    id_list = []
                    if TimeForManufacture_list.objects.all():
                        for pla0 in TimeForManufacture_list.objects.all():
                            id_list.append(int(pla0.id))
                    else:
                        id_list.append(0)
                    if pab >= p['amount']:
                        pab = pab - p['amount']
                        amount_0 = 0
                    else:
                        n = p['amount'] - pab
                        if n % m.quota != 0:
                            amount_0 = (n // m.quota + 1)*m.quota
                            pab = amount_0 - n
                        else:
                            amount_0 = n
                            pab = 0

                    o_time = (datetime.strptime(p['time'], '%Y%m%d')-timedelta(days=m.ahead_time)).strftime('%Y%m%d')
                    server = 'http://api.goseek.cn/Tools/holiday?date='
                    http = urllib3.PoolManager()
                    try:
                        while True:
                            r = http.request('GET', server + o_time)
                            vop = json.loads(r.data)
                            if vop['data'] == 1 or vop['data'] == 3:
                                o_time = (datetime.strptime(o_time, '%Y%m%d') -
                                          timedelta(days=1)).strftime("%Y%m%d")
                            else:
                                break
                    except:
                        pass
                    plan = TimeForManufacture_list(id=str(max(id_list) + 1).zfill(6),
                                                   forProduct=manu,
                                                   out_time=datetime.strptime(p['time'], '%Y%m%d'),
                                                   out_amount=amount_0,
                                                   in_amount=amount_0,
                                                   in_time=datetime.strptime(o_time, '%Y%m%d'))
                    plan.save()

    return True


def calculate(material, all_list, not_workday):
    materials = Bom.objects.filter(parent_code=material.bom_id)

    if materials:
        for mater in materials:

            mater1 = Mater()
            mater1.id = mater.materials_id
            mater1.bom_id = mater.id
            mater1.ahead_time = mater.leadtime
            mater1.need_forone = mater.consumption
            for plan in material.plans:

                need_time = (datetime.strptime(plan['time'], '%Y%m%d') -
                             timedelta(days=material.ahead_time)).strftime("%Y%m%d")

                server = 'http://api.goseek.cn/Tools/holiday?date='
                http = urllib3.PoolManager()
                try:
                    while True:

                        r = http.request('GET', server + need_time)
                        vop = json.loads(r.data)
                        if vop['data'] == 1 or vop['data'] == 3 or need_time in not_workday:
                            need_time = (datetime.strptime(need_time, '%Y%m%d')-timedelta(days=1)).strftime("%Y%m%d")

                        else:
                            break
                except:
                    pass
                need_amount = plan['amount']*material.need_forone
                p = {'time': need_time,
                     'amount': need_amount}

                mater1.plans.append(p)
            all_list.append(mater1)
            calculate(mater1, all_list, not_workday)


def indent_show(request, MPS_id):
    print('书法家')
    not_workday = []
    if Mps_list.objects.get(id=MPS_id):
        mps = Mps_list.objects.get(id=MPS_id)
        purchase = Purchase_apply.objects.filter(for_mps=mps)
        for pu in purchase:
            TimeForPurchase_list.objects.filter(forProduct=pu).delete()
        purchase.delete()

        man = Manufacture_apply.objects.filter(for_mps=mps)
        for M in man:
            TimeForManufacture_list.objects.filter(forProduct=M).delete()
        man.delete()

    products = Product_list.objects.filter(forMps=MPS_id)
    all_list = []
    for product in products:
        mater0 = Mater()
        mater0.id = product.product_id
        ma = Materials.objects.get(id=mater0.id)
        mater0.bom_id = Bom.objects.get(materials_id=ma.id).id
        mater0.ahead_time = Bom.objects.get(id=mater0.bom_id).leadtime
        mater0.need_forone = Bom.objects.get(id=mater0.bom_id).consumption
        plans = TimeForProduct_list.objects.filter(forProduct=product)
        mater0.plans = []
        for plan in plans:
            time = datetime.strftime(plan.time, "%Y%m%d")
            p = {
                'time': time,
                'amount': plan.amount
                }

            mater0.plans.append(p)
        all_list.append(mater0)
        calculate(mater0, all_list, not_workday)
    back = result(all_list, mps)
    purchase = Purchase_apply.objects.filter(for_mps=mps)
    purchases = []
    for pur in purchase:
        pl = TimeForPurchase_list.objects.filter(forProduct=pur)
        purchases.append({'pur': pur, 'plan': pl})
    manufacture = Manufacture_apply.objects.filter(for_mps=mps)
    manufactures = []
    for manu in manufacture:
        pla = TimeForManufacture_list.objects.filter(forProduct=manu)
        manufactures.append({'manu': manu, 'plan': pla})

    return render(request, 'erp_3/indent_show.html', locals())


def indent_all_show(request, MPS_id):
    if Mps_list.objects.get(id=MPS_id):
        mps = Mps_list.objects.get(id=MPS_id)
    purchase = Purchase_apply.objects.filter(for_mps=mps)
    purchases = []
    for pur in purchase:
        pl = TimeForPurchase_list.objects.filter(forProduct=pur)
        purchases.append({'pur': pur, 'plan': pl})
    manufacture = Manufacture_apply.objects.filter(for_mps=mps)
    manufactures = []
    for manu in manufacture:
        pla = TimeForManufacture_list.objects.filter(forProduct=manu)
        manufactures.append({'manu': manu, 'plan': pla})
    back = True

    return render(request, 'erp_3/indent_show.html', locals())


def purchase_show(request, MPS_id):
    if Mps_list.objects.get(id=MPS_id):
        mps = Mps_list.objects.get(id=MPS_id)
    purchase = Purchase_apply.objects.filter(for_mps=mps)
    purchases = []
    for pur in purchase:
        pl = TimeForPurchase_list.objects.filter(forProduct=pur)
        purchases.append({'pur': pur, 'plan': pl})
    if 'save_for_buy' in request.POST and request.POST['save_for_buy'] == 'yes':
        for pur_1 in purchases:
            for time in pur_1['plan']:
                not_add = True
                for de in Detail.objects.all():
                    if pur_1['pur'].product_id == de.material_id and time.time == de.required_time:
                        not_add = False
                        break
                    else:
                        not_add = True
                if not_add:
                    id_list = []
                    if Detail.objects.all():
                        for pu in Detail.objects.all():
                            id_list.append(int(pu.id))
                    else:
                        id_list.append(0)
                    detail = Detail(id=str(max(id_list) + 1).zfill(6),
                                    department='MRP',
                                    applicant='被加密',
                                    material_id=pur_1['pur'].product_id,
                                    material_name=pur_1['pur'].name,
                                    amount=time.amount,
                                    required_time=time.time,
                                    send_time=date.today()
                                    )
                    detail.save()

    return render(request, 'erp_3/purchase_show.html', locals())


def self_product_show(request, MPS_id):
    if Mps_list.objects.get(id=MPS_id):
        mps = Mps_list.objects.get(id=MPS_id)
    manufacture = Manufacture_apply.objects.filter(for_mps=mps)
    manufactures = []
    for manu in manufacture:
        pla = TimeForManufacture_list.objects.filter(forProduct=manu)
        manufactures.append({'manu': manu, 'plan': pla})
    return render(request, 'erp_3/self_product_show.html', locals())


def MRP_record(request):
    if 'is_login' not in request.session or request.session.get('is_login')!=True:
        return redirect('/login/')
    if 'role' in request.session and '计划员' in request.session['role']:
        right = True
    else:
        if 'role' in request.session and '采购员' in request.session['role']:
            right = True
    if 'id' in request.GET and request.GET['id']:
        search_id = request.GET['id']
        search_MPS = Mps_list.objects.filter(id=search_id)

    if 'name' in request.GET and request.GET['name']:
        search_name = request.GET['name']
        search_MPS = Mps_list.objects.filter(name=search_name)
    MPS = Mps_list.objects.order_by('id')
    return render(request, 'erp_3/MRP_record.html', locals())
