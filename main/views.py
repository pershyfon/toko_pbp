import datetime
import json

from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, JsonResponse
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
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user) 

    context = {
        'app_name': 'main',
        'username': request.user.username,
        'class': 'PBP C',
        'items': items,
        'last_login': request.COOKIES.get('last_login'),
    }

    return render(request, "main.html", context)

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
        else:
            messages.error(request, "Your username or password aren't valid!")
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

def get_item_json(request):
  Items = Item.objects.filter(user=request.user)
  return HttpResponse(serializers.serialize('json', Items))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        user = request.user

        new_item = Item(name=name, price=price, amount=amount, description=description, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request):
    data = json.loads(request.body.decode("utf-8"))
    item = Item.objects.get(pk=data["id"])
    item.delete()
    return HttpResponse("DELETED",status=200)

@csrf_exempt
def add_amount_ajax(request):
    data = json.loads(request.body.decode("utf-8"))
    item = Item.objects.get(pk=data["id"])
    item.amount += 1
    item.save()
    return HttpResponse(status=200)

@csrf_exempt
def remove_amount_ajax(request):
    data = json.loads(request.body.decode("utf-8"))
    item = Item.objects.get(pk=data["id"])
    if item.amount > 1:
        item.amount -= 1
        item.save()
    return HttpResponse(status=200)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def show_json_user(request, username):
    data_item = Item.objects.all()
    for data in data_item:
        if data.user.username == username:
            user_id = data.user
            data = Item.objects.filter(user = user_id)
            break
        else:
            data = []
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")