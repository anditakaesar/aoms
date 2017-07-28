from django.conf.urls import url, include
from aomswork import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'colors', views.ColorViewSet)
router.register(r'productcolor', views.ProductColorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
