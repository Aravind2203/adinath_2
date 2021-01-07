from django.contrib import admin
from .models import Product,Category,Carousel,Order
# Register your models here.
from .models import Invitations


'''
class ProductAdmin(admin.ModelAdmin):
    #fields=['product_code','product_name','product_description','product_prize','productimage_1']
    search_fields=['product_name','product_code']
    list_filter=['product_category','product_name','product_sub_category']
    list_display=['product_code','product_name','product_prize','product_category','product_customization']
    list_editable=['product_prize','product_customization']

class CategoryAdmin(admin.ModelAdmin):
    search_fields=['category_name']
    list_display=['category_name']
    #list_editable=['category_name']
    '''

class OrderAdmin(admin.ModelAdmin):
    
    list_display=['product','customer_name','customer_email','customer_number','order_completed']
    list_editable=['order_completed']
    list_filter=['order_completed']



admin.site.register(Product)
admin.site.register(Order,OrderAdmin)
admin.site.register(Category)
admin.site.register(Carousel)
admin.site.register(Invitations)