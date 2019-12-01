from rest_framework import serializers

from optimize_performance.products.models import Product


class ProductsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)

    def to_representation(self, instance: Product):
        result = super().to_representation(instance)
        result['tags'] = ProductTagSerializer(instance.tags, many=True).data
        result['brand'] = ProductBrandSerializer(instance.brand).data
        return result

    @staticmethod
    def setup_eager_loading(queryset):
        return queryset.prefetch_related('tags').select_related('brand')


class ProductTagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)


class ProductBrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
