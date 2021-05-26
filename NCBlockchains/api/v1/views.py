from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

from NCBlockchains.models import Block, Chain

from .serializers import BlockSerializer


class BlockReadOnlyModelViewSet(ReadOnlyModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = BlockSerializer
    queryset = Block.objects.all()
    lookup_field = 'hash'


class BlockCreateApiView(CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = BlockSerializer

    def create(self, request, *args, **kwargs):
        serializer = BlockSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        block = Block(**serializer.validated_data)
        block.chain, _ = Chain.objects.get_or_create(name=kwargs.get('chain_name'))
        print(block.is_valid_block(block.chain.last_block))
        print("# ", request.data)

        if not block.chain.is_valid_next_block(block):
            return Response({}, status=status.HTTP_304_NOT_MODIFIED)
        try:
            block.save()
        except Exception as e:
            print(" ON SAVE ::", e)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
