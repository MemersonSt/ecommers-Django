from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status #Documentacion code status
from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def user_api_view(request):
    if request.method == 'GET':
        users = User.objects.all() #llama a al modelo y lo guarda en una variable
        user_serializer = UserSerializer(users, many=True) #Serializa el modelo con los datos obtenidos a un formato json
        return Response(user_serializer.data, status = status.HTTP_200_OK) #Obtenemos lo datos
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data, status=status.HTTP_201_CREATED)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST) #En caso no pasar la validación
#Una función que recibe como parametro un dato(id)
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    user = User.objects.filter(id=pk).first()
    if user:
        #Para buscar un dato solo con el id
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)

        #Realizar una actualizacion de datos con el id
        elif request.method == 'PUT':
            user = User.objects.filter(id=pk).first()
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        #Para eliminar datos con el id
        elif request.method == 'DELETE':
            user = User.objects.filter(id=pk).first()
            user.delete()
            return Response({'message':'Usuario eliminado correctamente'}, status = status.HTTP_200_OK)
    return Response({'message': 'No se ha encontrado'}, status = status.HTTP_400_BAD_REQUEST)
