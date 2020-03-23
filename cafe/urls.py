"""cafe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import  include, path # con include traemos core..
from django.contrib import admin
from django.conf import settings
from service import views as services_views
from store import views as stores_views
from sample import views as samples_views

urlpatterns = [
    path('', include('core.urls')),
    path('services/',services_views.service ,name='services'),
    path('store/',stores_views.store ,name='store'),
    path('sample/',samples_views.sample ,name='sample'),
    path('admin/',admin.site.urls),
    
]

# Mapeo de archivos staticos si estamos debuggeando

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)