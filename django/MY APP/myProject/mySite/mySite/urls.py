"""
URL configuration for mySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.http import HttpResponse
from mySite.views import about, contact, home



def test(request):
    print("test function called")
    return HttpResponse("<h1>Hello Django</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index', test),  # this is the new view
    
    path("about/",about),
    path("contact/",contact),
    path("home/",home),
]