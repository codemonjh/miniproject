from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),#로그인
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),#토큰연장
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
    path('user/', views.UserView.as_view(), name='usercreate'),

               ]

