import graphene
from .models import Category, SubCategory, Product




class ProductType(graphene.ObjectType):
    name = 'product'

    item_name = graphene.String()

class SubCategoryType(graphene.ObjectType):
    name = 'subcategory'
    




class QueryType(graphene.ObjectType):
    name = 'query'
    description = '...'

    category = graphene.Field(
        CategoryType,
        id = graphene.Int()
    )

    sub_category = graphene.Field(
        SubCategoryType,
        id = graphene.Int()
    )

    product = graphene.Field(
        ProductType,
        id= graphene.Int()
    )

    def resolve_category(root, args, info):
        id = args.get('id')
        return Category.objects.get(pk=id)
    
    def resolve_sub_category(root, args, info):
        id = args.get('id')
        return SubCategory.objects.get(pk=id)

    def resolve_product(root, args, info):
        id = args.get('id')
        return Product.objects.get(pk=id)

schema = graphene.Schema(
    query= QueryType
)