
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Author
from .serializers import AuthorSerializer

# Create your views here.

class AuthorViewSet(ViewSet, PageNumberPagination):
    def list(self, request):
        authors = Author.objects.all()
        page = self.paginate_queryset(queryset=authors, request=request)
        serializer = AuthorSerializer(instance=page, many=True)
        return self.get_paginated_response(data=serializer.data)
