from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import get_user_model

from .serializers import JWTSerializer, UserSignupSerializer, UserSerializer

User = get_user_model()

# Create your views here.

class LoginViewset(TokenObtainPairView):
    serializer_class = JWTSerializer


class SignupViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSignupSerializer


class UserViewset(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication, SessionAuthentication )
    serializer_class = UserSerializer
