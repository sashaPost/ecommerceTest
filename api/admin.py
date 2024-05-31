from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product


admin.site.register(Category, MPTTModelAdmin)
# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    list_filter = ('categories',)
    search_fields = ('name', 'description')
