from datetime import datetime
from django.core.management import BaseCommand
from my_home.models import Product
import media


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {
                'name': 'Peach',
                'description': 'Персик',
                'image': 'image/Peach.jpg',
                'category': 'Fruits',
                'purchase_price': '140',
                'date_of_creation': datetime.now()
            },
            {
                'name': 'Cherries',
                'description': 'Черешня',
                'image': 'image/Cherries.jpg',
                'category': 'Berry',
                'purchase_price': '250',
                'date_of_creation': datetime.now()
            },
            {
                'name': 'Watermelon',
                'description': 'Арбуз',
                'image': 'image/Watermelon.jpg',
                'category': 'Fetus',
                'purchase_price': '29',
                'date_of_creation': datetime.now()
            },
            {
                'name': 'Melon',
                'description': 'Дыня',
                'image': 'image/Melon.jpg',
                'category': 'Fetus',
                'purchase_price': '37',
                'date_of_creation': datetime.now()
            },
            {
                'name': 'Apples',
                'description': 'Яблоки',
                'image': 'image/Apples.jpg',
                'category': 'Fruits',
                'purchase_price': '109',
                'date_of_creation': datetime.now()
            },
        ]
        products_for_add = []
        for product in product_list:
            products_for_add.append(Product(**product))
        Product.objects.all().delete()
        Product.objects.bulk_create(products_for_add)
