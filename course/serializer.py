from rest_framework.serializers import ModelSerializer
from user.models import User
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email']
        extra_kwargs = {
            'password':{'write_only' : 'true'}
        }
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user