from django.contrib import admin
from django.urls import path, include
from api.views import RegisterView, LoginView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path("api/user/register/", CreateUserView.as_view(), name="register"),
    path('api/user/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/user/me/', UserDetailView.as_view(), name='user-detail'),
    
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include("api.urls"))
]
