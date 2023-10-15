from django.shortcuts import render
from .models import Member, Order
from django.views import generic
from django.shortcuts import redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse
import json
from NeoCoffee.models import Category
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.

# def index(request):
#     num_coffee = coffee.objects.all().count()

#     context = {
#         'num_coffee' : num_coffee,
#     }

#     return render(request, 'home/index.html', context=context)


def sign_up(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        member_name = request.POST['username']
        member_email = request.POST['email']
        member_address = request.POST['address']
        member_number = request.POST['number']

        if form.is_valid():
            _member = Member(member_name=member_name, 
                             member_email=member_email,
                             member_address=member_address,
                             member_number=member_number,)
            _member.save()
            form.save()
            return redirect('/Shopping/login')
        
    context = {
        'form' : form
    }

    return render(request, 'accounts/register.html', context)

def sign_in(request):
    form = LoginForm()
    error_message = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  #重新導向到首頁
        else:
            error_message = "帳號不存在或密碼錯誤"

    context = {
        'form' : form,
        'error_message': error_message
    }

    return render(request, 'accounts/login.html', context)


def log_out(request):
    logout(request)

    return render(request, 'accounts/logout.html')


def place_order(request):
    data = json.loads(request.body)
    category_id = data.get('category_id')

    # Fetch the corresponding member and category name.
    try:
        member_obj = Member.objects.get(member_name=request.user.username)
        category_name = Category.objects.get(id=category_id).name

        # Create a new order.
        Order.objects.create(member=member_obj, coffee_name=category_name)

        return JsonResponse({'success': True})

    except Member.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Member not found'})
    except Category.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Category not found'})
    
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})