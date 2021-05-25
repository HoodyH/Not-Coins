from rest_framework import serializers
from NCBlockchain.models import BlockchainBlock


class BlockchainBlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlockchainBlock
        exclude = []
