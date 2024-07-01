import random
from .models import Transaction


def random_transaction_id():
    while True:
        random_transaction_id = random.randint(1000000000, 9999999999)
        if Transaction.objects.filter(transaction_id=random_transaction_id).exists() == False:
            return random_transaction_id
