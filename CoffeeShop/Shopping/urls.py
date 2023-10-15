from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'Shopping'

urlpatterns = [
    path('', RedirectView.as_view(url='/Shopping/login'), name="index"),
    path('register', views.sign_up, name='Register'),
    path('login', views.sign_in, name='Login'),
    path('logout', views.log_out, name='Logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

