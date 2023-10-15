from django.contrib import admin
from .models import member, order

# Register your models here.
class memberinfo(admin.ModelAdmin):
    list_display = ('member_name', 'member_number', 'member_address', 'member_email')

class ordersinfo(admin.ModelAdmin):
    list_display = ('primary_key', 'member_name', 'coffee_name')

admin.site.register(member, memberinfo)
admin.site.register(order, ordersinfo)