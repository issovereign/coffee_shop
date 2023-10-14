from django.shortcuts import render
from .models import coffee
from django.views import generic
# Create your views here.

def index(request):
    num_coffee = coffee.objects.all().count()

    context = {
        'num_coffee' : num_coffee,
    }

    return render(request, 'index.html', context=context)


class CoffeeListView(generic.ListView):
    model = coffee
    context_object_name = 'coffee_list'
