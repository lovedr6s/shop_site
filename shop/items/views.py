from django.shortcuts import render
from .models import Shoes

# Create your views here.

def catalog(request):
    items = Shoes.objects.all()
    context = {
        'items': items
    }
    return render(request, 'catalog.html', context)
