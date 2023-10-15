from django.db import models
from django.urls import reverse

# Create your models here.

class Member(models.Model):
    member_name = models.CharField(max_length=200, help_text='Enter Member name')
    member_number = models.CharField(max_length=10, help_text='Enter phone number')
    member_address = models.CharField(max_length=200, help_text='Enter address')
    member_email = models.EmailField(max_length=200, help_text='Enter email')

    def __str__(self):
        return self.member_name

    class Meta:
        ordering = ['member_name']

    def get_absolute_url(self):
        return reverse("member_detail", args=[str(self.id)])

class Order(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    coffee_name = models.CharField(max_length=200, help_text='Enter coffee name')

    def __str__(self):
        return self.member.member_name
    
    permissions = [
            ("can_add_order", "Can add order"),
            # Other permissions...
        ]