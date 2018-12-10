from django.conf import settings
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


router = routers.DefaultRouter()

urlpatterns = [
    url(r'^auth/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/api-token-auth', obtain_jwt_token),
    url(r'^auth/api-token-refresh', refresh_jwt_token),
    url(r'^auth/api-token-verify', verify_jwt_token),
    url(r'^', include("account.urls")),
    # url(r'^', include(router.urls)),
]

# if settings.DEBUG:
#     # This allows the error pages to be debugged during development, just visit
#     # these url in browser to see how these error pages look like.
#     urlpatterns += [
#         url(r'all', APIRootView.as_view(), name='all_api'),
#     ]
