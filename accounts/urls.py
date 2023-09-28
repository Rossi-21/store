from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('products', views.products, name="products"),
    #path('customer/<int:id>', views.customer, name="customer"),
    path('customer/<str:id>', views.customer, name="customer"),
    #path('logout/', views.logoutUser, name="logout"),
]