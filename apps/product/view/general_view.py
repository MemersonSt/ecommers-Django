from apps.product.serializadores.general_serializers import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer
from rest_framework import viewsets

# Utilizamos una clase para mostrar el listado categorias
class MeasureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer
    queryset = MeasureUnitSerializer.Meta.model.objects.filter(state=True)

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    queryset = CategoryProductSerializer.Meta.model.objects.filter(state=True)

class IndicadorViewSet(viewsets.ModelViewSet):
    serializer_class = IndicadorSerializer
    queryset = IndicadorSerializer.Meta.model.objects.filter(state=True)