
from django.http import JsonResponse
from django.views import View
from api.models import Product, Category

from django.core.serializers import serialize

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class ProductListView(View):

    def get(self, request):
        all_products = Product.objects.all()
        all_products_count = Product.objects.count()

        product_serialized = serialize('python', all_products)

        products = {
            'products': product_serialized,
            'count': all_products_count,
        }

        return JsonResponse(products)

    def get_single(request, id):
        product = Product.objects.get(id=id)

        return JsonResponse(product.to_json())

    def post(self, request):

        post_data = {
            'message': 'POST message.'
        }

        return JsonResponse(post_data)


class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        categories_serialized = serialize('python', categories)

        categories = {
            'categories': categories_serialized
        }

        return JsonResponse(categories)
