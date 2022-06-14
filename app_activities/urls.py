from django.urls import path
from . import views

app_name = 'app_activities'

urlpatterns = [
    #path('food_info_list/', views.FoodInfoListView.as_view(), name='food_info_list'),
    # path('user_car_info_list/', views.UserCarInfoListView.as_view(), name='user_car_info_list'),
    #path('create/', views.FoodInfoCreateView.as_view(), name='food_info_create'),
    path('<slug:slug>/<int:pk>/update/', views.FoodInfoUpdateView.as_view(), name='food_info_update'),
    path('<slug:slug>/<int:pk>/', views.FoodInfoDetailView.as_view(), name='food_info_detail'),
    # path('detail/<int:pk>/', views.UserCarInfoDetailView.as_view(), name='user_car_info_detail'),
    path('<slug:slug>/<int:pk>/delete/', views.FoodInfoDeleteView.as_view(), name='food_info_delete'),

    path('index/', views.AdminAboutPage.as_view(), name="admin_home"),
    path('service/', views.AdminServicePage.as_view(), name="admin_service"),
    #
    path('<int:pk>/<int:id>/payment/', views.PaymentDeleteView.as_view(), name='admin_delete_payment'),
    path('products/', views.product_list, name='admin_product_list'),
    path('transaction/', views.transaction_list, name='admin_transaction'),
    path('<slug:category_slug>/', views.product_list, name='admin_product_list_by_category'),
    path('<int:id>/<slug:slug>/admin_product_detail/', views.product_detail, name='admin_product_detail'),

    # urls for Product
    #path('product/detail/<slug:slug>/', ProductDetailView.as_view(), name='Product_product_detail'),
]
