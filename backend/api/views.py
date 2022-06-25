import contextlib
import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    with contextlib.suppress(Exception):
        data = json.loads(body)
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    return JsonResponse(data)
