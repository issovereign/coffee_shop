from django.shortcuts import render
from .models import member
from django.views import generic
from django.shortcuts import redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse

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
            _member = member(member_name=member_name, 
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

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')  #重新導向到首頁
                
    context = {
        'form' : form
    }

    return render(request, 'accounts/login.html', context)

def log_out(request):
    logout(request)

    return render(request, 'accounts/logout.html')



