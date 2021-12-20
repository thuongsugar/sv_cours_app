from rest_framework import viewsets,generics,status,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from course.serializer import UserSerializer,CategorySerializer,CourseSerializer
import requests
from .models import Category,Course
from .paginator import CoursePagination

from user.models import User
# Create your views here.
class UserViewSet(viewsets.ViewSet,
                    generics.ListAPIView,
                    generics.CreateAPIView):
    queryset = User.objects.filter(is_active = True)
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'get_current_user':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    @action(methods=['get'],detail=False,url_path='current-user')
    def get_current_user(self,request):
        return Response(self.serializer_class(request.user).data,status=status.HTTP_200_OK)

class Login(APIView):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        client_id = 'CTbiXESfyQ8c0MNdn27w6gdvSyMrbvJ2bs1RJBiu'
        client_secret = 'Jsy7F0udvJENzDQfHDJS0IkU0mGPiK1EU8tq835JCfGeIuELqvo5hPrhmqiMmEKfqNrP12081nKgSmXeg9Zv2bJtnLJPLQPQYzPjPmgTQolbGO1L7H6SKivLz0tmGE7K'
        data = {
            'username':username,
            'password': password,
            'client_secret': client_secret,
            'client_id': client_id,
            'grant_type':'password',
        }
        print(request.get_host())
        o = requests.post(f"http://{request.get_host()}/o/token/",data=data)
        print(o.__dict__)
        if o.status_code == 400 :

            return Response(o.json(),status=status.HTTP_400_BAD_REQUEST)

        return Response(o.json(),status=status.HTTP_200_OK)

class CategoryViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ViewSet,generics.ListAPIView):
    pagination_class = CoursePagination
    serializer_class = CourseSerializer

    def get_queryset(self):
        courses = Course.objects.filter(active=True)

        q = self.request.query_params.get('q')
        if q is not None :
            courses = courses.filter(subject__icontains=q)
        category_id = self.request.query_params.get('category_id')
        if category_id is not None :
            courses = courses.filter(category__id = category_id)

        return courses