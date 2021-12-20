from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('user',views.UserViewSet)
router.register('category',views.CategoryViewSet,'category')
router.register('courses',views.CourseViewSet,'course')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.Login.as_view()),
]