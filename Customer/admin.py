from django.contrib import admin

from Customer.models import C_address, Customer, History

admin.site.register(Customer)
admin.site.register(C_address)
admin.site.register(History)
