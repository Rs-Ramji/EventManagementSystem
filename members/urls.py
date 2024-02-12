from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name="login"),
    path('user_registration', views.user_registration, name="registration"),
    path('user_logout', views.user_logout, name="logout")
]