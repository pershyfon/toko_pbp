import datetime
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse
from main.models import Item
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    
    total_amount = Item.objects.filter(user=request.user).aggregate(total_amount=Sum('amount'))['total_amount']
    jumlah_items = total_amount if total_amount is not None else 0   

    context = {
        'app_name': 'main',
        'username': request.user.username,
        'class': 'PBP C',
        'items': items,
        'jumlah_items': str(jumlah_items),
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
     product = form.save(commit=False)
     product.user = request.user
     product.save()
     return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_amount(request, id):
    try:
        items = Item.objects.get(pk=id)
        if request.method == 'GET':
            items.amount += 1
            items.save()
            messages.success(request, 'Sukses Menambah Amount.')
            return redirect('main:show_main')
        return redirect('main:show_main')
    except Item.DoesNotExist:
        raise Http404("Item tidak ditemukan.")
    
def remove_amount(request, id):
    try:
        items = Item.objects.get(pk=id)
        if request.method == 'GET':
            items.amount -= 1
            items.save()
            if items.amount == 0:
                items.delete()
            messages.success(request, 'Sukses Mengurangi Amount.')
            return redirect('main:show_main')
        return redirect('main:show_main')
    except Item.DoesNotExist:
        raise Http404("Item tidak ditemukan.")

def delete_item(request, id):
    try:
        items = Item.objects.get(pk=id)
        if request.method == 'GET':
            items.delete()
            messages.success(request, 'Sukses Menghapus Item.')
            return redirect('main:show_main')
        return redirect('main:show_main')
    except Item.DoesNotExist:
        raise Http404("Item tidak ditemukan.")