from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


from product.models import Product


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    if model_data := Product.objects.all().order_by('?').first():
        data = model_to_dict(model_data)
    else:
        data = {"Error": "Product not available"}
    return Response(data)
