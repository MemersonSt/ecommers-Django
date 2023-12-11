from rest_framework.routers import DefaultRouter
from apps.product.view.general_view import MeasureUnitViewSet, CategoryViewSet, IndicadorViewSet
from apps.product.view.product_view import ProductViewSet

router = DefaultRouter()
router.register(r'measure_unit', MeasureUnitViewSet, basename='measure_unit')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'indicador', IndicadorViewSet, basename='indicador')
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = router.urls