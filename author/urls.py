
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet

author_router = DefaultRouter()
author_router.register('', AuthorViewSet, 'author')

urlpatterns = [
    path('', include(author_router.urls)),
]
