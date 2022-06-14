from django.urls import path
from .views import *

urlpatterns = (
    # urls for Main
    path('about/', AboutMainWebsite.as_view(), name="Main_about"),
    path('contact/', ContactMainWebsite.as_view(), name="Main_contact"),
    path('service/', ServiceWebsite.as_view(), name="Main_service"),
    path('remark/', ClientRemarkWebsite.as_view(), name="Main_remark"),
    path('team/', TeamMainWebsite.as_view(), name="Main_team"),
    #
    path('products', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/product_detail/', product_detail, name='product_detail'),

    # urls for Product
    path('', HomeWebsite.as_view(), name='Main_home'),
    path('product/detail/<slug:slug>/', ProductDetailView.as_view(), name='Product_product_detail'),

)
