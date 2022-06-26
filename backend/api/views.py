from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    if instance := Product.objects.all().order_by('?').first():
        data = ProductSerializer(instance).data
    else:
        data = {"detail": "no product available"}
    return Response(data)
