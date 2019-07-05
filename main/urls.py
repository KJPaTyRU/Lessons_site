from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('kingdom', views.kingdom),
    path('accounts/login', views.login_page),
    path('accounts/register', views.register),
]


