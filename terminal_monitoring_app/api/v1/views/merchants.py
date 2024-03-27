#!/usr/bin/python3

import os
from api.v1.views import views
from api.v1.utils import *
from api.v1.authents import *
from flask import jsonify

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)
path_to_merchants = os.path.join(parent_directory, 'files_storage', 'merchants.json')


@views.route('/merchants')
@login_required
def merchants():
    count = request.args.get('count', 10, type=int)
    offset = request.args.get('offset', 0, type=int)
    merchants = read_json(path_to_merchants)
    try:
        return [merchant for merchant in merchants[offset : offset + count]]
    except IndexError:
        return [merchant for merchant in merchants[offset : -1]]

@views.route('/merchants/<string:unq_field>')
@login_required
def merchant_by_unique_field(unq_field):
    merchants = read_json(path_to_merchants)
    if (len(unq_field) < 11):
        for merchant in merchants:
            if(merchant['Merchant_ID'] == unq_field):
                return merchant
            else:
                continue
    if (len(unq_field) >= 11):
        if ('@' in unq_field):
            for merchant in merchants:
                if(merchant['Email'] == unq_field):
                    return merchant
                else:
                    continue
        else:
            for merchant in merchants:
                if(merchant['Contact Number'] == unq_field):
                    return merchant
                else:
                    continue
    return jsonify({"error": "no merchant with any unique field: {}".format(unq_field)})
