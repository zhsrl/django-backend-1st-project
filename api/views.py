
from math import prod
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.views import View
from api.models import Product

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'api/index.html')


@method_decorator(csrf_exempt, name='dispatch')
class ProductListView(View):

    def get(self, request):

        all_products = Product.objects.all()
        all_products_count = Product.objects.count()

        product_serialized = []

        for product in all_products:
            product_serialized.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'description': product.decription,
                'count': product.count,
                'category': product.category,
                'is_active': product.is_active
            })

        products = {
            'products': product_serialized,
            'count': all_products_count,
        }

        return JsonResponse(products)

    def get_by_id(self, request, pk):
        obj = get_object_or_404(Product, pk=pk)

        return JsonResponse(obj)

    def post(self, request):

        post_data = {
            'message': 'POST message.'
        }

        return JsonResponse(post_data)
