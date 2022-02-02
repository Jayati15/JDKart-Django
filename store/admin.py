from django.contrib import admin
from .models import Product,Variation,ReviewRating,ProductGallery
from django.utils.safestring import mark_safe
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
#prepopulate the slug

class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    

    
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields={'slug':('product_name','is_available')}
    inlines = [ProductGalleryInline,]
    
    
class VariationAdmin(admin.ModelAdmin):
    list_display=('product','variation_category','variation_value','is_active')
    list_editable= ('is_active',)
    list_filter=('product','variation_category','variation_value',)
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Variation,VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)
# Register your models here.
