from django.shortcuts import render
from .models import Store

def store(request):
    stores = Store.objects.all()
    return render(request, "store/store.html", {'stores':stores})