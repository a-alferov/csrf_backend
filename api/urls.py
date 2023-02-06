from django.urls import include, path
from rest_framework import routers

from api.root import APIRoot, get_csrf_token
from api.views import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', APIRoot.as_view()),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('get-csrf-token/', get_csrf_token, name='get-csrf-token')
]
