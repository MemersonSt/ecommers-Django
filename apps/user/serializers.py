from rest_framework import serializers
from .models import User


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'name',
            'last_name'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # Una funciona que encripta las constraseñas y nos retorna un usuario con la constraseña encriptada
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    # Para actualizar password

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    # Una funcion que se llama para listar mostrando solo datos seleccionados en vez de todos

    def to_representation(self, instance):
        return {
            'id': instance['id'],  # se accede a la clave del valor con ['valor requerido']
            # se puede cambiar el username a usuario sin necesidad cambiar el original
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }

# class TestUserValidation(serializers.Serializer):
#     #va a serializar estos campos en especifico:
#     name = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#
#     #Una funcion que valida los datos que recibe el serializador
#     def validate_name(self, value):
#         # a custom validation
#         if 'develop' in value:
#             raise serializers.ValidationError('Error, no puedo existir un usuario con ese nombre')
#         return value
#
#     def validate_email(self, value):
#         if value == '':
#             raise serializers.ValidationError('Escribe un correo valido')
#         return value
#
#     def validate(self, data):
#         print("validacion general")
#         return data
