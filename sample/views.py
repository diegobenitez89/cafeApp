from django.shortcuts import render
from .models import Sample

def sample(request):
    samples = Sample.objects.all()
    return render(request, "sample/sample.html", {'samples':samples})