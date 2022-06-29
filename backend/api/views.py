from django.forms.models import model_to_dict
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view


from product.models import Product
from product.serializers import ProductSerializer


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    Get data from the database.
    """
    if instance := Product.objects.all().order_by('?').first():
        data = ProductSerializer(instance).data
    else:
        data = {"detail": "no product available"}
    return Response(data)


@api_view(['POST'])
def addData(request, *args, **kwargs):
    """
    Add data to the database.
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response({"invalid": "Not a valid data"}, status=400)
