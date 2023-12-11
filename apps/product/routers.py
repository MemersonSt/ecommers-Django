from rest_framework.routers import DefaultRouter
from apps.product.view.general_view import MeasureUnitListAPIView
from apps.product.view.product_view import ProductViewSet

router = DefaultRouter()
router.register(r'measure_unit', MeasureUnitListAPIView, basename='measure_unit')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = router.urls