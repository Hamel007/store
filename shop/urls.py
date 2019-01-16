from django.urls import path

# from .views import post
from . import views


urlpatterns = [
    path("", views.ProductsList.as_view(), name="product_all"),
    path('detail/<slug:slug>', views.ProductDetail.as_view(),
         name='product_detail'),
    # path('product-detail/', post, name="products_detail"),
]