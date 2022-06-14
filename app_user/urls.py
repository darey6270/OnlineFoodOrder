from django.urls import path
from . import views

app_name='app_user'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('user_login/', views.user_login.as_view(), name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),

]
