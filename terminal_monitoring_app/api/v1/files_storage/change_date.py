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
        date_list = transaction['Date Logged'].split(' ')
        if (i < 100):
            date_list[0] = '09-Nov-2023'
            print(date_list)
            transaction['Date Logged'] = ' '.join(date_list)
        elif (i >= 100 and i <= 226):
            date_list[0] = '10-Nov-2023'
            transaction['Date Logged'] = ' '.join(date_list)
        elif (i >= 227 and i <= 323):
            date_list[0] = '11-Nov-2023'
            transaction['Date Logged'] = ' '.join(date_list)
        elif (i >= 324 and i <= 417):
            date_list[0] = '12-Nov-2023'
            transaction['Date Logged'] = ' '.join(date_list)
        elif (i >= 418 and i <= 556):
            date_list[0] = '13-Nov-2023'
            transaction['Date Logged'] = ' '.join(date_list)
        elif (i >= 557 and i <= 623):
            date_list[0] = '14-Nov-2023'
            transaction['Date Logged'] = ' '.join(date_list)
        else:
            date_list[0] = '15-Nov-2023'
            transaction['Date Logged'] = ' '.join(date_list)
    print(transactions[:10])
    print(transactions[-10:-1])
    write_json(path_to_transactions, transactions)
