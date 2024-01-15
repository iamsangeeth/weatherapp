from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'password']

        extra_kwargs = {
                'password': {'write_only': True}
                }
        
    def create(self, validated_data):

        '''
            create user with validated data
            and return error if email already exists 
        '''

        password = validated_data.pop('password', None)
        if User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({'email': 'email already exists'})
        user_obj = self.Meta.model(**validated_data)

        if password is not None:
            user_obj.set_password(password)
        user_obj.save()
        return user_obj

