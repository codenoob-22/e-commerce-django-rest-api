from django.contrib import admin
from django.urls import path, include

from catalogs.views import *


urlpatterns = [
    path('categories/', include(CategoryRoute.urls)),
    path('subcategories/', include(SubCategoryRoute.urls)),
    path('products/', include(ProductRoute.urls)),
]