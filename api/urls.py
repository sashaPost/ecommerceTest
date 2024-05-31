from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AttributeViewSet,
    CategoryViewSet,
    ImageViewSet,
    ProductAttributeViewSet,
    ProductViewSet,
    sign_in,
    SignUpView,
)


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'images', ImageViewSet)
router.register(r'attributes', AttributeViewSet)
router.register(r'product-attributes', ProductAttributeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', sign_in, name='signin'),
]
