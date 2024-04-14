#!/usr/bin/env python3
import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
parent_directory = os.path.dirname(parent_directory)
parent_directory = os.path.dirname(parent_directory)
print(parent_directory)
sys.path.append(parent_directory)
from api.v1.utils import read_json, write_json

if __name__ == "__main__":
    i = 0
    path_to_transactions = os.path.join(current_directory, 'transactions.json')
    transactions = read_json(path_to_transactions)
    for transaction in transactions:
        i += 1
        if (i % 4 == 0):
            transaction['Status'] = 'Unsuccessful'
        else:
            transaction['Status'] = 'Successful'
    print(transactions[:10])
    write_json(path_to_transactions, transactions)
