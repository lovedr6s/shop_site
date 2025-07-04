from django.shortcuts import render, get_object_or_404
from .models import Shoes

# Create your views here.

def catalog(request):
    items = Shoes.objects.all()
    context = {
        'items': items
    }
    return render(request, 'catalog.html', context)

def shoe_detail(request, id):
    shoe = get_object_or_404(Shoes, id=id)
    return render(request, 'shoe_detail.html', {'shoe': shoe})
