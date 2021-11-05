from rest_framework import routers
from .api import ImgViewSet

router = routers.DefaultRouter()
router.register('api/images', ImgViewSet, 'imgs')

urlpatterns = router.urls
