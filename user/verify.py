import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
from django.contrib.auth import get_user_model

class JWTAuthentication(BaseAuthentication):

    ''' 
        Authentication class to validate authorization token and return user
        or return authentication error
    '''

    def authenticate(self, request):

        User = get_user_model()
        authorization_header = request.headers.get('Authorization')
        if not authorization_header:
            return None
        try:
            access_token = authorization_header.split(' ')[1]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')
        except Exception as e:
            print(e)

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('user is inactive')

        return (user, None)
