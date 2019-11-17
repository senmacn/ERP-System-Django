from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *
from erp_1.models import *
from erp_6.models import *
import datetime


def supplier_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '采购员' in request.session['role']:
        right = True
    return render(request, 'erp_5/Supplier_management.html', locals())


def supplier_information(request):
    supplier = Supplier.objects.all()
    if 'supplier_id' in request.GET and request.GET['supplier_id']:
        search_id = request.GET['supplier_id']
        search_supplier = Supplier.objects.filter(id=search_id)
    if 'supplier_name' in request.GET and request.GET['supplier_name']:
        search_name = request.GET['supplier_name']
        search_supplier = Supplier.objects.filter(name=search_name)
    return render(request, 'erp_5/supplier_information.html', locals())


def add_supplier(request):
    if request.POST:
        if 1:
            supplier = Supplier(id=request.POST['id'],
                          name=request.POST['name'],
                          contact=request.POST['contact'],
                          number=request.POST['number'],
                          mail=request.POST['mail'],
                          address=request.POST['address'],
                          )
            supplier.save()
        return redirect('/erp_5/supplier_information/')
    else:
        return render(request, 'erp_5/add_supplier.html', locals())


def supplier_detail(request, id):
    if request.POST:
        supplier = Supplier.objects.get(id=id)
        supplier.id = request.POST['id']
        supplier.name = request.POST['name']
        supplier.contact = request.POST['contact']
        supplier.number = request.POST['number']
        supplier.mail = request.POST['mail']
        supplier.address = request.POST['address']
        supplier.save()
        return redirect('/erp_5/supplier_information/')
    supplier = Supplier.objects.get(id=id)
    return render(request, 'erp_5/supplier_detail.html', locals())


def supplier_delete(request,id):
    if 1:
        Supplier.objects.filter(id=id).delete()
    return redirect('/erp_5/supplier_information/')


def supplier_assessment(request):
    suppliers = Supplier.objects.all()
    supp_orders = []
    for supplier in suppliers:
        oders = Order.objects.filter(supplier_id=supplier.id)
        mark1 = 0.0
        mark2 = 0.0
        temp = 0
        sum = 0
        for item in oders:
            if item.state == '已完成':
                mark1 = item.credit_mark+mark1
                mark2 = item.quality_mark+mark2
                sum = sum+1
                if item.trouble_order == 0:
                    temp = temp+1
        supp_orders.append({'supplier': supplier,'credit': mark1/sum,'quality': mark2/sum,'trouble': temp,'order_sum':sum})
    order = Order.objects.all()
    return render(request, 'erp_5/supplier_assessment.html', locals())


def supplier_order(request,id):
    order = Order.objects.filter(supplier_id=id)
    return render(request, 'erp_5/supplier_order.html', locals())


def supply_information(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '采购员' in request.session['role']:
         right = True
    if 'supplys_id' in request.GET and request.GET['supplys_id']:
        search_id = request.GET['supplys_id']
        search_materials = Materials.objects.get(id=search_id)
        search_supply = Supply.objects.filter(material_id=search_materials)
    if 'supplier_name' in request.GET and request.GET['supplier_name']:
        search_name = request.GET['supplier_name']
        search_supplier = Supplier.objects.get(name=search_name)
        search_supply = Supply.objects.filter(supplier=search_supplier)
    supply = Supply.objects.all()
    return render(request, 'erp_5/supply_information.html', locals())


def supply_detail(request, id):
    if request.POST:
        supply = Supply.objects.get(id=id)
        supply.price = request.POST['price']
        supply.tran_price = request.POST['tran_price']
        supply.rate = request.POST['rate']
        supply.save()
        return redirect('/erp_5/supply_information/')
    supply = Supply.objects.get(id=id)
    return render(request, 'erp_5/supply_detail.html', locals())


def add_supply(request):
    item1 = Materials.objects.all()
    item2 = Supplier.objects.all()
    if request.POST:
        if 1:
            supply = Supply(material=Materials.objects.get(id=request.POST['material']),
                          supplier=Supplier.objects.get(name=request.POST['supplier']),
                          price=request.POST['price'],
                          tran_price=request.POST['tran_price'],
                          rate=request.POST['rate'],
                          )
            supply.save()
        return redirect('/erp_5/supply_information/')
    else:
        return render(request, 'erp_5/add_supply.html', locals())


def supply_delete(request,id):
    if 1:
        Supply.objects.filter(id=id).delete()
    return redirect('/erp_5/supply_information/')


def order_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '采购员' in request.session['role']:
        right = True
    return render(request, 'erp_5/Order_management.html', locals())


def order_information(request):
    order = Order.objects.all()
    return render(request, 'erp_5/order_information.html', locals())


def order_detail(request,id):
    supplier = Supplier.objects.all()
    staff = Staff.objects.filter(department=Department.objects.get(name='采购'))
    requisition = Detail.objects.filter(order=Order.objects.get(id=id))
    if request.POST:
        order = Order.objects.get(id=id)
        order.staff = Staff.objects.get(name=request.POST['buyer'])
        order.address = request.POST['address']
        order.order_maker = request.POST['order_maker']
        order.reviewer = request.POST['reviewer']
        order.number = request.POST['number']
        # order.predict_time = request.POST['predict_time']
        order.state = request.POST['state']
        order.remarks = request.POST['remarks']
        order.save()
        return redirect('/erp_5/order_information/')
    order = Order.objects.get(id=id)
    return render(request, 'erp_5/order_detail.html', locals())


def add_order(request):
    item1 = Supplier.objects.all()
    item2 = Staff.objects.filter(department=Department.objects.get(name='采购'))
    id_list = []
    if Order.objects.all():
        for item in Order.objects.all():
            id_list.append(int(item.id))
    else:
        id_list.append(0)
    if request.POST:
        if 1:
            order = Order(id=str(max(id_list) + 1).zfill(6),
                          supplier=Supplier.objects.get(name=request.POST['supplier_name']),
                          staff=Staff.objects.get(name=request.POST['buyer']),
                          address=request.POST['address'],
                          order_maker=request.POST['order_maker'],
                          predict_time=request.POST['predict_time'],
                          )
            order.save()
        last_url = '/erp_5/order_information/order_detail/'+str(order.id)+'/'
        return redirect(last_url)
    else:
        return render(request, 'erp_5/add_order.html', locals())


def add_detail(request,id):
    detail = Detail.objects.all()
    order = Order.objects.get(id=id)
    return render(request, 'erp_5/add_detail.html', locals())


def choose_detail(request,rid,oid):
    order = Order.objects.get(id=oid)
    requisition = Detail.objects.get(id=rid)
    requisition.order = order
    requisition.save()
    detail = Detail.objects.all()
    return render(request, 'erp_5/add_detail.html', locals())


def detail_delete(request,did,oid):
    detail = Detail.objects.get(id=did)
    detail.order = None
    detail.save()
    order = Order.objects.get(id=oid)
    last_url = '/erp_5/order_information/order_detail/' + str(order.id) + '/'
    return redirect(last_url)


def order_delete(request,id):
    if 1:
        Order.objects.filter(id=id).delete()
    return redirect('/erp_5/order_information/')


def requisition_information(request):
    requisition = Detail.objects.filter(order=None)
    flag=1
    return render(request, 'erp_5/requisition_information.html', locals())


def all_requisition(request):
    requisition = Detail.objects.all()
    flag=0
    return render(request, 'erp_5/requisition_information.html', locals())


def requisition_detail(request, id):
    requisition = Detail.objects.get(id=id)
    search_id=requisition.material_id
    supply = Supply.objects.filter(material=Materials.objects.get(id=search_id))
    return render(request, 'erp_5/requisition_detail.html', locals())


def choose_supplier(request,rid,sid):
    requisition = Detail.objects.get(id=rid)
    supply = Supply.objects.get(id=sid)
    requisition.supplier=supply.supplier.name
    requisition.price=supply.price
    requisition.tran_price=supply.tran_price
    requisition.rate=supply.rate
    requisition.save()
    requisition = Detail.objects.all()
    return render(request, 'erp_5/requisition_information.html', locals())


def buyer_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '采购员' in request.session['role']:
        right = True
    return render(request, 'erp_5/Buyer_management.html', locals())


def buyer_information(request):
    buyer = Staff.objects.filter(department=Department.objects.get(name='采购'))
    return render(request, 'erp_5/buyer_information.html', locals())


def buyer_order(request,id) :
    order = Order.objects.filter(staff=Staff.objects.get(id=id))
    return render(request,'erp_5/buyer_order.html', locals())



def performance(request):
    return render(request, 'erp_5/performance.html', locals())


def receive_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '采购员' in request.session['role']:
        right = True
    return render(request,'erp_5/Receive_management.html',locals())


def application_information(request):
    shenqing = []
    for staff in Staff.objects.filter(department=Department.objects.get(name='采购')):
        shenqings = App.objects.filter(applicant=staff)
        for s in shenqings:
            shenqing.append(s)
    return render(request, 'erp_5/application_information.html', locals())


def choose_order(request):
    order = Order.objects.filter(state='已确认')
    buyer = Staff.objects.filter(department=Department.objects.get(name='采购'))
    return render(request, 'erp_5/choose_order.html', locals())


def add_application(request,id):
    shenqingss = Detail.objects.filter(order=Order.objects.get(id=id))
    for item in shenqingss :
        id_list = []
        if App.objects.all():
            for app in App.objects.all():
                id_list.append(int(app.app_id))
        else:
            id_list.append(0)
        app = App(app_id=str(max(id_list) + 1).zfill(6),
                      io=1,
                      goods_id=item.material_id,
                      goods_name=item.material_name,
                      norms=item.specifications,
                      demand=item.amount,
                      date_app=datetime.datetime.now(),
                      date_io=datetime.datetime.now(),
                      order=Order.objects.get(id=id),
                      applicant=Order.objects.get(id=id).staff,
                      )
        app.save()
    order = Order.objects.get(id=id)
    order.state = '已发出'
    order.send_time=datetime.datetime.now()
    order.save()
    shenqing = []
    for staff in Staff.objects.filter(department=Department.objects.get(name='采购')):
        shenqings = App.objects.filter(applicant=staff)
        for s in shenqings:
            shenqing.append(s)
    return redirect('/erp_5/application_information/')


def assessment_information(request):
    order = Order.objects.filter(state='已完成')
    if 'order_id' in request.GET and request.GET['order_id']:
        search_id = request.GET['order_id']
        search_order = Order.objects.filter(id=search_id)
    return render(request, 'erp_5/assessment_information.html', locals())


def assessment(request):
    order = Order.objects.filter(state='已发出')
    staff = Staff.objects.filter(department=Department.objects.get(name='采购'))
    item = 0
    if request.POST:
        if 1:
            print(request.POST['id'])
            order = Order.objects.get(id=request.POST['id'])
            order.reality_time = request.POST['reality_time']
            order.trouble_order = request.POST['trouble']
            order.credit_mark = request.POST['credit_mark']
            order.quality_mark = request.POST['quality_mark']
            order.remarks = request.POST['remarks']
            order.operator = request.POST['operator']
            order.assess_time = request.POST['assess_time']
            order.state = '已完成'
            order.save()
            return redirect( '/erp_5/Receive_management/')
    else:
        return render(request, 'erp_5/assessment.html', locals())


def query_report(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '采购员' in request.session['role']:
        right = True
    return render(request, 'erp_5/query_report.html', locals())


def query(request):
    search_order = []
    flag = 1
    if 'material_id' in request.GET and request.GET['material_id']:
        search_id = request.GET['material_id']
        search_detail = Detail.objects.filter(material_id=search_id)
        for item in search_detail:
            if item.order != None:
                order = Order.objects.get(id=item.order.id)
                search_order.append(order)
    if 'order_id' in request.GET and request.GET['order_id']:
        search_id = request.GET['order_id']
        item = Order.objects.get(id=search_id)
        search_order.append(item)
    order = Order.objects.all()
    return render(request, 'erp_5/query.html', locals())


def order_on_way(request):
    search_order = []
    flag = 0
    if 'material_id' in request.GET and request.GET['material_id']:
        search_id = request.GET['material_id']
        search_detail = Detail.objects.filter(material_id=search_id)
        for item in search_detail:
            order = Order.objects.get(id=item.id)
            search_order.append(order)
    if 'order_id' in request.GET and request.GET['order_id']:
        search_id = request.GET['order_id']
        item = Order.objects.get(id=search_id)
        search_order.append(item)
    order = Order.objects.filter(state='已发出')
    return render(request, 'erp_5/query.html', locals())


def order_read(request,id):
    requisition = Detail.objects.filter(order=Order.objects.get(id=id))
    amount = 0.0
    for item in requisition:
        amount = amount+item.price*item.amount
    order = Order.objects.get(id=id)
    return render(request, 'erp_5/order_read.html', locals())


def report(request):
    return render(request, 'erp_5/report.html', locals())