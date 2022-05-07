from django.urls import path
from .import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('products/', views.Products, name='products'),
    path('customer/<int:pk>/', views.Customerpage, name='customer'),
    path('update_order/<int:pk>/', views.Update_order, name='update_order'),
    path('create_order/<int:pk>/', views.Create_Order, name='create_order'),
    path('delete_order/<int:pk>/', views.Delete_order, name='delete_order'),
    path('signin/', views.SigninUser, name='signin'),
    path('login/', views.LoginUser, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    path('profile/', views.UserProfile, name='profile'),
    path('update_profile/', views.Update_profile, name='update_profile'),

]