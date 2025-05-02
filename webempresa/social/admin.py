from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ("created_on", "updated_on")

    # If the user who is accessing is not a super user, but a user who belongs to the "Staff" group, 
    # then we block some fields in addition to blocking certain models.
    # Overwriting the "readonly_fields" variable at runtime with this method
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            # return ("created_on", "updated_on", "key", "name")
            return ("key", "name")
        else:
            return ("created_on", "updated_on")

admin.site.register(Link, LinkAdmin)
