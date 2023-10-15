from django.contrib import admin
from .models import member

# Register your models here.
class memberinfo(admin.ModelAdmin):
    list_display = ('member_name', 'member_number', 'member_address', 'member_email')

admin.site.register(member, memberinfo)