from rest_framework import serializers
from NCBlockchains.models import (
    Block,
    Chain,
)


class BlockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Block
        exclude = []


class ChainSerializer(serializers.ModelSerializer):

    block_set = BlockSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = Chain
        fields = [
            'name',
            'block_set'
        ]
