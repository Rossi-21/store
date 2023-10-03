from django.urls import path
from . import views
from .views import (
    loginRequiredViews,
)
    


urlpatterns = [
    path('register', views.registerPage, name="register"),
    path('login', views.loginPage, name="login"),
    path('logout', views.logoutUser, name="logout"),

    path('', loginRequiredViews.as_view(), name="home"),
    path('products', loginRequiredViews.as_view(), name="products"),
    #path('customer/<int:id>', views.customer, name="customer"), is another way to make the URL dynamic
    path('customer/<str:id>', loginRequiredViews.as_view(), name="customer"),

    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:id>', views.updateOrder, name="update_order"),
    path('delete_order/<str:id>', views.deleteOrder, name="delete_order"),  
]