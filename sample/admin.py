from django.contrib import admin

# Register your models here.
from .models import Sample

class SampleAdmin(admin.ModelAdmin):
    readonly_fields = ('created','update')

admin.site.register(Sample,SampleAdmin)