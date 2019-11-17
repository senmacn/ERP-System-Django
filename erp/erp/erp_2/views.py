from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from erp_1.models import *
from erp_6.models import *


def staff_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    department = Department.objects.get(name='销售')
    staff = Staff.objects.filter(department=department)
    if 'id' in request.GET and request.GET['id']:
        search_id = request.GET['id']
        search_staff = staff.filter(id=search_id)
    return render(request, 'erp_2/staff_management.html', locals())


def customer_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '销售员' in request.session['role']:
        right = True
    if 'id' in request.GET and request.GET['id']:
        search_id = request.GET['id']
        search_customer = Customer.objects.filter(id=search_id)
    customer = Customer.objects.all()
    return render(request, 'erp_2/customer_management.html', locals())


def product_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '销售员' in request.session['role']:
        right = True
    product = Product.objects.all()
    return render(request, 'erp_2/product_management.html', locals())


def order_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '销售员' in request.session['role']:
        right = True
    if 'id' in request.GET and request.GET['id']:
        search_id = request.GET['id']
        search_order = Order2.objects.filter(id=search_id)
    if 'salesman' in request.GET and request.GET['salesman']:
        search_order = Order2.objects.filter(salesman_id=request.GET['salesman'])
    order = Order2.objects.order_by('id')
    return render(request, 'erp_2/order_management.html', locals())


def add_order(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    department = Department.objects.get(name='销售')
    departments_1 = Staff.objects.filter(department=department)
    departments_2 = Customer.objects.all()
    departments_3 = Product.objects.all()
    if request.POST:
        # try:
        if 1:
            order = Order2(id=request.POST['id'],
                          customer=Customer.objects.get(name=request.POST['customer']),
                          salesman=Staff.objects.get(name=request.POST['salesman']),
                          product=Product.objects.get(name=request.POST['product']),
                          price=request.POST['price'],
                          amount=request.POST['amount'],
                          date=request.POST['date'],
                          )
            order.save()
        # except:pass
        return redirect('/erp_2/order_management/')
    else:
        return render(request, 'erp_2/add_order.html', locals())


def OrderDetails(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if request.POST:
        order = Order2.objects.get(id=id)
        # order.customer = Customer.objects.get(name=request.POST['customer']),
        # order.salesman = Staff.objects.get(name=request.POST['salesman']),
        # order.product = Product.objects.get(name=request.POST['product']),
        order.price = request.POST['price']
        order.amount = request.POST['amount']
        order.deliver2 = request.POST['deliver2']
        order.payment = request.POST['payment']
        order.save()
        return redirect('/erp_2/order_management/')
    order = Order2.objects.get(id=id)
    # customer = Customer.objects.all()
    # salesman = Staff.objects.all()
    # product = Product.objects.all()
    return render(request, 'erp_2/OrderDetails.html', locals())


def delete_order(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if request.POST:
        # try:
        Order2.objects.filter(id=request.POST['id']).delete()
        # except:pass
    return redirect('/erp_2/order_management/')


def add_customer(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if request.POST:
        # try:
        if 1:
            customer = Customer(id=request.POST['id'],
                          name=request.POST['name'],
                          address=request.POST['address'],
                          grade=request.POST['grade'],
                          tel=request.POST['tel'],
                          )
            customer.save()
        # except:pass
        return redirect('/erp_2/customer_management/')
    else:
        return render(request, 'erp_2/add_customer.html', locals())


def CustomerDetails(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if request.POST:
        customer = Customer.objects.get(id=id)
        customer.name = request.POST['name']
        customer.address = request.POST['address']
        customer.grade = request.POST['grade']
        customer.tel = request.POST['tel']
        customer.save()
        return redirect('/erp_2/customer_management/')
    customer = Customer.objects.get(id=id)
    return render(request, 'erp_2/CustomerDetails.html', locals())


def delete_customer(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if request.POST:
        # try:
        Customer.objects.filter(id=request.POST['id']).delete()
        # except:pass
    return redirect('/erp_2/customer_management/')


def add_product(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if request.POST:
        # try:
        if 1:
            product = Product(id=request.POST['id'],
                          name=request.POST['name'],
                          cost=request.POST['cost'],
                          basic_price=request.POST['basic_price'],
                          )
            product.save()
        # except:pass
        return redirect('/erp_2/product_management/')
    else:
        return render(request, 'erp_2/add_product.html', locals())


def ProductDetails(request, id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if request.POST:
        product = Product.objects.get(id=id)
        product.name = request.POST['name']
        product.cost = request.POST['cost']
        product.basic_price = request.POST['basic_price']
        product.save()
        return redirect('/erp_2/product_management/')
    product = Product.objects.get(id=id)
    return render(request, 'erp_2/ProductDetails.html', locals())


def delete_product(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if request.POST:
        # try:
        Product.objects.filter(id=request.POST['id']).delete()
        # except:pass
    return redirect('/erp_2/product_management/')


def application_management(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 'role' in request.session and '销售员' in request.session['role']:
        right = True
    department = Department.objects.get(name='销售')
    application = []
    for staff in Staff.objects.filter(department=department):
        apps = App.objects.filter(applicant=staff)
        for ppp in apps:
            application.append(ppp)
    return render(request, 'erp_2/application_management.html', locals())


def add_app2(request):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    department = Department.objects.get(name='销售')
    product = Product.objects.all()
    applicant = Staff.objects.filter(department=department)
    if request.POST:
        # try:
        if 1:
            id_list = []
            if App.objects.all():
                for app in App.objects.all():
                    id_list.append(int(app.app_id))
            else:
                id_list.append(0)
            apps = App(app_id=str(max(id_list)+1).zfill(6),
                       io=request.POST['io'],
                       goods_name=request.POST['goods_name'],
                       goods_id=Materials.objects.get(name=request.POST['goods_name']).id,
                       demand=request.POST['demand'],
                       date_app=request.POST['date_app'],
                       date_io=request.POST['date_io'],
                       applicant=Staff.objects.get(name=request.POST['applicant']),
                       state=request.POST['state'],
                       )
            apps.save()
        # except:pass
        return redirect('/erp_2/application_management/')
    else:
        return render(request, 'erp_2/add_app2.html', locals())



def delete_app2(request, app_id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 1:
        # try:
        App.objects.filter(app_id=app_id).delete()
        # except:pass
    return redirect('/erp_2/application_management/')


def confirm_app2(request, app_id):
    if 'is_login' not in request.session or request.session['is_login']!=True:
        return redirect('/login/')
    if 1:
        app = App.objects.get(app_id=app_id)
        app.state = '已收货'
        app.save()
    return redirect('/erp_2/application_management/')