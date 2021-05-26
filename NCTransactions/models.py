from django.db import models


class Transactions(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    time_stamp = models.DateTimeField(auto_now_add=True)
    added_to_block = models.BooleanField(default=False)

    def __str__(self):
        return f'Transaction of {self.amount} | {self.sender} to {self.receiver}'
