from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter

from catalogs.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer
from catalogs.models import Category, SubCategory, Product

class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SubCategoryView(ModelViewSet):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


CategoryRoute = DefaultRouter()
SubCategoryRoute = DefaultRouter()
ProductRoute = DefaultRouter()

CategoryRoute.register(r'', CategoryView, basename='categories')
SubCategoryRoute.register(r'', SubCategoryView, basename='subcategories')
ProductRoute.register(r'', ProductView, basename='products')