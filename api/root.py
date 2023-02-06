from django.middleware.csrf import get_token
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.routers import APIRootView
from django.views.decorators.csrf import ensure_csrf_cookie


class APIRoot(APIRootView):
    permission_classes = [AllowAny]
    api_root_dict = {
        "user": "user-list",
        "group": "group-list",
        'get-csrf-token': 'get-csrf-token',
    }


@ensure_csrf_cookie
@api_view(["GET"])
def get_csrf_token(request):
    csrf_token = get_token(request)
    return Response(data={'csrf_token': csrf_token})
