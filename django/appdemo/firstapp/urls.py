from django.urls import path
from . import views

urlpatterns = [
    path('home2', views.home,name="home"),
    path('contact2', views.contact, name="contact")
]