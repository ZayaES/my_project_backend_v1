#!/usr/bin/python3

import os
from api.v1.views import views
from api.v1.utils import *
from api.v1.authents import *
from flask import jsonify

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
path_to_transactions = os.path.join(parent_directory, 'files_storage', 'transactions.json')

@views.route('/transactions')
#@auth.login_required
@login_required
def transactions():
    count = request.args.get('count', 10, type=int)
    offset = request.args.get('offset', 0, type=int)
    transactions = read_json(path_to_transactions)
    return [transaction for transaction in transactions[offset:count + offset]]


@views.route('/transactions/<string:reference>')
@login_required
def transaction_by_code(reference):
    transactions = read_json(path_to_transactions)
    for transaction in transactions:
        if(transaction['Transaction Reference'] == reference):
            return transaction
        else:
            continue
    return jsonify({"error": "no transaction with reference number {}".format(reference)}), 404


@views.route('/transactions/role/<string:role>')
@login_required
def transaction_by_role(role):
    count = request.args.get('count', 10, type=int)
    offset = request.args.get('offset', 0, type=int)
    role_transactions = []
    transactions = read_json(path_to_transactions)
    if (role == 'merchants'):
        print('merchant')
        for transaction in transactions:
            if "Merchant Name" in transaction:
                role_transactions.append(transaction)
            else:
                #print('else')
                continue
        return role_transactions[offset:offset + count]
    elif (role == "agents"):
        for transaction in transactions:
            if "Agent Name" in transaction:
                role_transactions.append(transaction)
            else:
                continue
        return role_transactions[offset:offset + count]
    else:
        return jsonify({"error": "no role {} found".format(role)}), 404