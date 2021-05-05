from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from api_app.views import PollListViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'polls', PollListViewSet)

# rest api
urlpatterns += [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# open-api schema
urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
