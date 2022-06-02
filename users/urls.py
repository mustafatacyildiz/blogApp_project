from django.urls import path
from .views import user_logout, register, user_login, profile
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logout/',user_logout,name='logout'),
    path('register/',register,name='register'),
    path('login/',user_login,name='user_login'),
    path('profile/', profile, name='profile'),
    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='change-password'),
    path('reset-password/', auth_views.PasswordResetView.as_view(template_name='registration/reset-password.html'), name='reset-password'),
]
