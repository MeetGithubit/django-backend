from django.contrib import admin

from .models import Users,Homemaker, Item,orders

admin.site.register(Users)
admin.site.register(Homemaker)
admin.site.register(Item)
admin.site.register(orders)
