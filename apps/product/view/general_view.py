from apps.product.models import MeasureUnit, Indicador, CategoryProduct
from apps.product.serializadores.general_serializers import MeasureUnitSerializer, IndicadorSerializer, CategoryProductSerializer
from rest_framework import generics

# Utilizamos una clase para mostrar el listado categorias
class MeasureUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer
    def get_queryset(self):
        return MeasureUnit.objects.filter(state = True)