from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings
# Create your views here.


class NetflixView(ModelViewSet):
    http_method_names=['get']
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=Netflix.objects.all()
    serializer_class=NetflixSerializer


class LoginView(ObtainAuthToken):
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES

class SignupView(ModelViewSet):
    serializer_class=SignupSerializer
    queryset=User.objects.filter(is_superuser=False,is_staff=False)