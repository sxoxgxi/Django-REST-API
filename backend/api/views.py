# import contextlib
# import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

from product.models import Product


def api_home(request, *args, **kwargs):
    if model_data := Product.objects.all().order_by('?').first():
        data = model_to_dict(model_data)
    else:
        data = {}
    return JsonResponse(data)
