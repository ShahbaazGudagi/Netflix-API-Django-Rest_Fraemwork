from rest_framework import serializers
from .models import *


class NetflixSerializer(serializers.ModelSerializer):
    class Meta:
        model=Netflix
        fields='__all__'

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model =  User
        fields = ['id','first_name','last_name','email','username','password']
        extra_kwargs = {
            'password' : {
                'write_only' : True
            }
        }

    def create(self,validatedData):
        user = User.objects.create(
            username = validatedData['username'],
            first_name = validatedData['first_name'],
            last_name = validatedData['last_name'],
            email = validatedData['email']
        )
        user.set_password(validatedData['password'])
        user.save() 
        return user 

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
