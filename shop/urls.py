from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('register/confirm/', views.confirm, name='confirm'),
    path('change/user/', views.Change.as_view(), name='user_change'),
    path('logout/', views.logout_user, name='logout'),
    path('category/', views.category, name='category'),
    path('category/<int:id>', views.category_category, name='category_category')
]
