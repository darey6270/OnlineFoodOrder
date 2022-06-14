from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('payment/', views.payment_create, name='make_payment'),
]
