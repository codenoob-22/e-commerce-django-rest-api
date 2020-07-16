from django.db import models
from django.db.models import TextField, ForeignKey


class Category(models.Model):
    name        = TextField(default="")

    def __str__(self):
        return self.name

    def get_json(self):
        return { "name": self.name }
    
    def get_sub_categories(self):
        return self.subcategory_set.all().values_list('name', flat=True)

    def get_products(self):
        queryset = self.subcategory_set.prefetch_related('product_set')
        result = []
        for sub in queryset:
            result += (sub.product_set.all().values_list('name', flat=True))
        
        return result

class SubCategory(models.Model):
    name        = TextField(default="")
    category    = ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_json(self):
        return { "name": self.name }

    def get_products(self):
        return self.product_set.all().values_list('name', flat=True)

class Product(models.Model):
    name        = TextField(default="")
    subcategory = ForeignKey(SubCategory, on_delete=models.CASCADE)

    def get_json(self):
        return { "name": self.name }

    def __str__(self):
        return self.name