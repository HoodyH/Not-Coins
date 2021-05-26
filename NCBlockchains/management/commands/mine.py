from django.core.management import BaseCommand
from NCTransactions.models import Transactions

__author__ = 'HoodyH'


class Command(BaseCommand):

    def handle(self, *args, **options):

        transactions = Transactions.objects.filter(added_to_block=False).order_by('id')
