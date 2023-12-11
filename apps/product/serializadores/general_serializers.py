from apps.product.models import MeasureUnit, CategoryProduct, Indicador

from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('state','create_date','modified_date','delete_date')

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ('state','create_date','modified_date','delete_date')

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        exclude = ('state','create_date','modified_date','delete_date')