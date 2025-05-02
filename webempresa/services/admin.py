from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ("created_on", "updated_on")

admin.site.register(Service, ServiceAdmin) # Registering the model and its configuration
