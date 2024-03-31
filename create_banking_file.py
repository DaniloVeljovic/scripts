# Structure: transaction_id, transfer_date, sender_account_id, receiver_account_id, amount, currency
from typing import List
import csv
from datetime import datetime as dt
import random

NUMBER_OF_RECORDS: int = 10_000

class TransactionRecord:
    def __init__(self, transaction_id, transfer_date, sender_account_id, receiver_account_id, amount, currency) -> None:
        self.transaction_id = transaction_id
        self.transfer_date = transfer_date
        self.sender_account_id = sender_account_id
        self.receiver_account_id = receiver_account_id
        self.amount = amount
        self.currency = currency

def create_transaction_record(transaction_id: int) -> TransactionRecord:
    return TransactionRecord(
        transaction_id=transaction_id,
        transfer_date=dt.today().strftime('%Y-%m-%d'),
        sender_account_id=random.randint(0, 1000),
        receiver_account_id=random.randint(0, 1000),
        amount=random.randint(50, 1000),
        currency='EUR'
    )

if __name__ == "__main__":
    transactions: List = []

    for i in range(NUMBER_OF_RECORDS):
        transaction_record: TransactionRecord = create_transaction_record(i)
        transactions.append([transaction_record.transaction_id, transaction_record.transfer_date, transaction_record.sender_account_id, transaction_record.receiver_account_id, transaction_record.amount, transaction_record.currency])

    with open(f'xbank-transactions-{dt.today().strftime('%Y-%m-%d')}.csv', 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['transaction_id', 'transfer_date', 'sender_account_id', 'receiver_account_id', 'amount', 'currency'])
        writer.writerows(transactions)
