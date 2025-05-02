from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_on", "updated_on")

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created_on", "updated_on") # # Model's fields to be only-read in the panel
    list_display = ("title", "author", "published_on", "post_categories") # Model's fields to be displayed as columns
    ordering = ("author", "published_on") # To give an order by field and subfield. The second one is optional, but use ("something", )
    search_fields = ("title", "content", "author__username", "categories__name") # To create a search form
    date_hierarchy = "published_on" # To define a date hierarchy
    list_filter = ("author__username", "categories__name") # Filtering post by author or category

    # To display many-to-many fields as columns
    # "obj" refers to each row displayed in the list
    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias" # To rename our created field

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
