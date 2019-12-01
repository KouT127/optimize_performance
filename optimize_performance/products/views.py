from rest_framework.response import Response
from rest_framework.views import APIView

from optimize_performance.products.models import Product
from optimize_performance.products.serializer import ProductsSerializer


class ProductsView(APIView):

    def get(self, request):
        query = Product.objects.all()
        query = ProductsSerializer.setup_eager_loading(query)
        result = ProductsSerializer(query, many=True).data
        return Response(result)
