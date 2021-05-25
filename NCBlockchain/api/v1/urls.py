from rest_framework.routers import DefaultRouter
from .views import BlockchainModelViewSet

router = DefaultRouter()
router.register('view', BlockchainModelViewSet)

urlpatterns = [

] + router.urls
