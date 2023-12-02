from django.urls import path
from .views import user_api_view, user_detail_api_view

urlpatterns = [
    # path('product/', ProductAPIView.as_view(), name = 'product_api')
    path('user/', user_api_view, name = 'user_api'),
    path('user/<int:pk>/', user_detail_api_view, name= 'user_detail_api')
]