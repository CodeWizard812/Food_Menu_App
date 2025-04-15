from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm

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

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form': form})

def edit_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-form.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    context = {
        'item': item,
    }
    return render(request, 'food/item-delete.html', context)