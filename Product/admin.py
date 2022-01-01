from django.contrib import admin

from Product.models import Category, Product ,Property,Details

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Property)
admin.site.register(Details)

