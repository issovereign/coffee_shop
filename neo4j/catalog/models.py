from django.db import models
from django.urls import reverse

# Create your models here.

# class country(models.model):
#     name = models.CharField(max_length=200, help_text='Enter a country')

#     def __str__(self):
#         return self.name

class coffee(models.Model):
    
    coffee_name = models.CharField(max_length = 200, help_text='Enter Coffee Name')
    coffee_country = models.CharField(max_length = 200, help_text='Enter country')
    coffee_type = models.CharField(max_length=200, help_text="Enter the coffee type")
    
    def __str__(self):
        return self.coffee_name

    # def get_absolute_url(self):
    #     return reverse('coffee-detail', args=[str(self.id)])
    


