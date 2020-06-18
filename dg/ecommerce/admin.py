from django.contrib import admin
from .models import Product,ProductImag,Category,Product_Alternative,Product_Accessories,Profile,Cart,CartProduct



# Register your models here.

admin.site.register(Product)
admin.site.register(ProductImag)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)
admin.site.register(Profile)
admin.site.register(CartProduct)
admin.site.register(Cart)
