from django.urls import path
from . import views

urlpatterns = [
    path('', views.custom_login, name="login"),
    path('logout/', views.logoutUserView, name="logout"),
    path('update/<pk>/', views.updateUserView, name="update"),
    path('home/', views.homePageView2, name="home"),
    path('register/', views.registerPage, name="register"),
]