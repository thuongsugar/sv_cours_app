from rest_framework import viewsets,generics,status,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from course.serializer import UserSerializer

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
