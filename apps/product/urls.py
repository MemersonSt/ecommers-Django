from django.urls import path
#from .views import ProductAPIView
from .views import product_api_view

urlpatterns = [
    # path('product/', ProductAPIView.as_view(), name = 'product_api')
    path('product/', product_api_view, name = 'producto_api')
]