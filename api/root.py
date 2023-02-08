from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.routers import APIRootView


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
    return Response()
