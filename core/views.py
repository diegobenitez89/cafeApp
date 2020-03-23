from django.shortcuts import HttpResponse, render

# Create your views here.
def home(request):
    return render(request, 'core/index.html')
def about(request):
    return render(request, 'core/about.html')
def contact(request):
    return render(request, 'core/contact.html')
def blog(request):
    return render(request, 'core/blog.html')

