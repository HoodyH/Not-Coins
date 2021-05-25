from django.db import models
from django.utils import timezone


class BlockchainBlock(models.Model):

    timestamp = models.DateTimeField(default=timezone.now)
    nonce = models.TextField(max_length=256)
    previous_hash = models.TextField()
