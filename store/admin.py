from django.contrib import admin

from .models import Product

#prepopulate the slug
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields={'slug':('product_name','is_available')}
admin.site.register(Product,ProductAdmin)

# Register your models here.
