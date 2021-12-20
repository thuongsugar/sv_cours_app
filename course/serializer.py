from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from user.models import User
from .models import Category,Course
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

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['id','subject','image','created_date','category']
