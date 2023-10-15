"""
URL configuration for CoffeeShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from NeoCoffee import views as neo_views
from django.views.generic import RedirectView
from Shopping import views as shp_views

urlpatterns = [
    path('', RedirectView.as_view(url='/categories/')),
    path('admin/', admin.site.urls),
    path('categories/', neo_views.show_categories, name='show_categories'),
    path('api/topcategories/', neo_views.top_categories, name='top_categories'),
    path('api/subcategories/<int:parent_id>/', neo_views.sub_categories, name='sub_categories'),
    path('Shopping/', include('Shopping.urls')),
    path('api/place_order/', shp_views.place_order, name='place_order'),
]

