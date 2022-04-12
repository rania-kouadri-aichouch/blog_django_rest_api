from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from . import models, serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from shared.permissions import IsAdminOrReadOnly


# Pagination
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = models.Category.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAdminOrReadOnly,)
    queryset = models.Post.objects.all()
    http_method_names = ['get', 'post', 'patch', 'delete']
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category',)
