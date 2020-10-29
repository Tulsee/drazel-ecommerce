from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterUserViewSet

r = DefaultRouter()
# r.register('register', RegisterUserViewSet, basename='register')

urlpatterns = [
    path('', include(r.urls)),
    path('register/', RegisterUserViewSet.as_view(), name='register')
]
