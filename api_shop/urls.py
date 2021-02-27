from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='api.get_token'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='api.token_refresh'),
    path('user/change/', views.UserChange.as_view(), name='api-change'),
    path('user/create/', views.UserCreate.as_view(), name='api-create')
]
