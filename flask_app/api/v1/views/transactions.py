#!/usr/bin/python3

import os
from api.v1.views import views
from api.v1.utils import *
from api.v1.authents import *
from flask import jsonify

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
path_to_transactions = os.path.join(parent_directory, 'files_storage', 'transactions.json')
print(path_to_transactions)

@views.route('/transactions')
#@auth.login_required
#@login_required
def transactions():
    count = request.args.get('count', 10, type=int)
    offset = request.args.get('offset', 0, type=int)
    transactions = read_json(path_to_transactions)
    return [transaction for transaction in transactions[offset:count + offset]]


@views.route('/transactions/<string:unq_field>')
@login_required
def transaction_by_code(unq_field):
    transactions = read_json(path_to_transactions)
    if (len(unq_field) < 11):
        for transaction in agents:
            if(transaction['Code'] == unq_field):
                return transaction
            else:
                continue
    if (len(unq_field) >= 11):
        if ('@' in unq_field):
            for transaction in transactions:
                if(transaction['Email'] == unq_field):
                    return transaction
                else:
                    continue
        else:
            for transaction in transactions:
                if(transaction['Phone Number'] == unq_field):
                    return transaction
                else:
                    continue
    return jsonify({"error": "no agent with code {}".format(unq_field)})
