from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializar

# Create your views here.
@api_view(['GET', 'POST'])
def product_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all() #llama a al modelo y lo guarda en una variable
        products_serializer = ProductSerializar(products, many=True) #Serializa el modelo con los datos obtenidos a un formato json
        return Response(products_serializer.data) #Obtenemos lo datos
    elif request.method == 'POST':
        product_serializer = ProductSerializar(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data)
        return Response(product_serializer.errors) #En caso no pasar la validación


# class ProductAPIView(APIView):
#     def get(self, request):
#         products = Product.objects.all() #llama a al modelo y lo guarda en una variable
#         products_serializer = ProductSerializar(products, many=True) #Serializa el modelo con los datos obtenidos a un formato json
#         return Response(products_serializer.data) #Obtenemos lo datos
