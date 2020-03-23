from django.contrib import admin

# Register your models here.
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

admin.site.register(Service,ServiceAdmin)