from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.

@login_required(login_url = 'user-login')
def Home(request):
    orders =Order.objects.all()
    products=Product.objects.all()
    if request.method =='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('Home')
    else:
        form=OrderForm()
    context ={
        'orders': orders,
        'form': form,
        'products':products,
    }
    return render(request, 'dash/Home.html',context)

@login_required(login_url = 'user-login')
def Inventory(request):
    items = Product.objects.all()

    if request.method=='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request,f'{product_name } has been added')
            return redirect('Inventory')
    else:
        form =ProductForm()
    context ={
        'items': items,
        'form': form,
    }
    return render(request, 'dash/Inventory.html',context)

@login_required(login_url = 'user-login')
def Orders(request):
    orders= Order.objects.all()

    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('product')
            messages.success(request,f'{product_name } has been added')
            return redirect('Orders')
    else:
        form =OrderForm()
    context ={
        'orders':orders,
        'form': form,

    }
    return render(request, 'dash/Orders.html',context)

@login_required(login_url = 'user-login')
def Staff(request):
    workers= User.objects.all()
    workers_count=workers.count()
    context ={
        'workers':workers,
    }
    return render(request, 'dash/staff.html',context)

@login_required(login_url = 'user-login')
def Staff_details(request,pk):
    workers= User.objects.get(id=pk)
    context ={
        'workers':workers,

    }
    return render(request, 'dash/staff_details.html',context)

@login_required(login_url = 'user-login')
def profile(request):
    return render(request, 'user/profile.html')


@login_required(login_url = 'user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect ('Inventory')
    return render(request, 'dash/product_delete.html' )

@login_required(login_url = 'user-login')
def product_update(request ,pk):
    item = Product.objects.get(id=pk)
    if request.method =='POST':
        form=ProductForm(request.POST,instance =item)
        if form.is_valid():
            form.save()
            return redirect('Inventory')
    else:
        form =ProductForm(instance =item)
    context ={
        'form': form,

    }
    return render (request, 'dash/product_update.html',context)

