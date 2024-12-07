from django.core.management.base import BaseCommand
from django.db.models import (Sum, Avg, Count, Min, Max)
from typing import Any
from shop.models import Tag, Item, Category

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        count_items = Category.objects.aggregate(Count('items'))
        print(count_items)

        categories = Category.objects.annotate(items_count=Count('items'), items_price_sum=Sum('items'))
        for category in categories:
            print(f"Count-{category.items_count}, Price Sum-{category.items_price_sum}")

        items = Item.objects.select_related('category')

        for item in items:
            print(item.category.name)

        items = Item.objects.prefetch_related("tags")
        for item in items:
            print(item.tags.all())
