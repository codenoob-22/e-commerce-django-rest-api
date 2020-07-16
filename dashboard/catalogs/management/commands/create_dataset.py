from django.core.management.base import BaseCommand
from catalogs.models import Product, Category, SubCategory


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Command(BaseCommand):
    """ this class creates test data for testing the app """


    def handle(self, *args, **options):

        Category.objects.all().delete()

        #creating 2 categories
        categories = [Category(name='category {}'.format(i)) for i in range(1, 3)]
        Category.objects.bulk_create(categories)

        start = 1
        for i in Category.objects.all():
            subcategories = [SubCategory(name='subcategory {}'.format(index), category=i) for index in range(start, start + 4)]
            SubCategory.objects.bulk_create(subcategories)
            start += 4
        
        start = 1
        for i in SubCategory.objects.all():
            products = [Product(name='product {}'.format(index), subcategory=i) for index in range(start, start + 5)]
            Product.objects.bulk_create(products)
            start += 5
        
        print(bcolors.OKBLUE + "create sample data" + bcolors.ENDC + '.....' + bcolors.OKGREEN + 'OK' + bcolors.ENDC)

        