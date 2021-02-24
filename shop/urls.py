from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login1, name='login'),
    path('register/', views.register, name='register'),
    path('register/confirm/', views.register, name='confirm')

]
