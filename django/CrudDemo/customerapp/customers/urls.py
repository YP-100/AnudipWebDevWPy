from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('customer_edit/<int:id>/', views.customer_edit, name='customer_edit'),
    path('customer_delete/<int:id>/', views.customer_delete, name='customer_delete'),
]
