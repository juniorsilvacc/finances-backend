from rest_framework import generics
from categories.models import Category
from categories.serializers import CategorySerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Categories"])
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=["Categories"])
class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
