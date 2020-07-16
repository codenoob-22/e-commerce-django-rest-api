from rest_framework.serializers import ModelSerializer, ReadOnlyField, PrimaryKeyRelatedField
from catalogs.models import Category, SubCategory, Product 

class CategorySerializer(ModelSerializer):
    sub_categories = ReadOnlyField(source='get_sub_categories')
    products       = ReadOnlyField(source='get_products')
    class Meta:
        model = Category
        fields = ('id', 'name', 'sub_categories', 'products')


class SubCategorySerializer(ModelSerializer):
    products = ReadOnlyField(source='get_products')

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'products')

class ProductSerializer(ModelSerializer):
    subcategory = PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Product
        fields = ('name', 'subcategory')