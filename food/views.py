from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader


# Create your views here.
def index(request):
    items_list = Item.objects.all()
    context = {
        'items_list': items_list,
    }
    return render(request, 'food/index.html', context)

def item(request):
    return HttpResponse("Hello, world. You're at the food item.")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)