from django.contrib import admin
from .models import Member, Order

# Register your models here.
class Memberinfo(admin.ModelAdmin):
    list_display = ('member_name', 'member_number', 'member_address', 'member_email')

class Ordersinfo(admin.ModelAdmin):
    list_display = ('member', 'coffee_name')

admin.site.register(Member, Memberinfo)
admin.site.register(Order, Ordersinfo)