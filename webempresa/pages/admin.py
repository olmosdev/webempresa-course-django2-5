from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ("created_on", "updated_on")
    list_display = ("title", "order")

admin.site.register(Page, PageAdmin)
