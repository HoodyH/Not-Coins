from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from NCBlockchain.models import BlockchainBlock

from .serializers import BlockchainBlockSerializer


class BlockchainModelViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = BlockchainBlockSerializer
    queryset = BlockchainBlock.objects.all()


class IsBlockValidApiView(APIView):

    def get(self, request, *args, **kwargs):
        pass
