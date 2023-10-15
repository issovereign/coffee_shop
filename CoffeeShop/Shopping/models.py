from django.db import models
from django.urls import reverse

# Create your models here.

class member(models.Model):
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

class order(models.Model):
    primary_key = models.CharField(max_length=200, help_text='Enter member primary key.')
    member_name = models.CharField(max_length=200, help_text='Enter member name.')
    coffee_name = models.CharField(max_length=200, help_text='Enter coffee name')

    def __str__(self):
        return self.member_name
    
    class Meta:
        ordering = ['member_name']
    