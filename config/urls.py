from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

file = open(r'static/DESCRIPTION.md', 'r')
description = file.read()
file.close()

schema_view = get_schema_view(
   openapi.Info(
      title="ProSetup API",
      default_version='0.1.0',
      description=description,
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
