from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    BlockReadOnlyModelViewSet,
    BlockCreateApiView,
)

router = DefaultRouter()
router.register('', BlockReadOnlyModelViewSet)

urlpatterns = [

    path('<chain_name>/mine-block', BlockCreateApiView.as_view(), name='mine-block'),

] + router.urls
