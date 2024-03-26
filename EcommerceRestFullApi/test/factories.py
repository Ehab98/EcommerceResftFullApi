import factory

from EcommerceRestFullApi.product.models import Category, Product, Brand

class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = "test_category"
    

