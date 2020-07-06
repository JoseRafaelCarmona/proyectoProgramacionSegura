from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from servicios.views import ServidorViewSet
from django.conf.urls import include,url

router = DefaultRouter()
router.register(r'servidor', ServidorViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    url(r'rest-auth/', include('rest_auth.urls')),
    #url(r'rest-auth/registration/', include('rest_auth.registration.urls')),
]
