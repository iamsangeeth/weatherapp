from datetime import datetime, timedelta
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView, settings, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
import jwt

from .serializers import *

class RegisterView(APIView):

    ''' view to create user '''

    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

class LoginView(APIView):

    ''' View to verify user with email/password and return access token'''

    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()
        if not user:
            raise AuthenticationFailed('User not found')
        if not user.check_password(password):
            raise AuthenticationFailed('Invalid Password')

        token  = jwt.encode({'id': user.id, 'email': user.email, 'exp': datetime.utcnow() + timedelta(hours=1), 'iat': datetime.utcnow()}, settings.SECRET_KEY , algorithm='HS256')

        token = {
                'token': token,
                'status': 'success',
                }
        return Response(token)


 

