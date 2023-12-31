from apps.product.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state','create_date','modified_date','delete_date')