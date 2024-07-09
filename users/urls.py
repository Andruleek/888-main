from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.exit, name='exit'),
    path('login/', views.login, name='login'),
    path('reset-password/', views.reset_password_view, name='reset_password'),

]