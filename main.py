import pathlib
import pickle

import pandas as pd
from flask import Flask, request

from project_constants.config import DATA_DIRECTORY, MODELS_DIRECTORY, MODEL_FEATURES
from modelling.train import create_estimator

app = Flask(__name__)


# Define a route for the root path of the API
@app.route('/')
def home():
    return 'hello from here'


@app.route('/post/new_users/predictions', methods=['POST'])
def post_new_users_prediction():
    response = request.json
    users_info = pd.DataFrame(response)
    users_id = users_info.index
    predictions_model = model.predict(users_info[numerical_features_model])
    predictions = dict(zip(users_id, predictions_model))
    return predictions, 200


@app.route('/post/trained_user/prediction', methods=['POST'])
def post_trained_user_prediction():
    response = request.json
    user_id = response['user_id']

    user = df.loc[user_id, :]  # Series type
    user_preprocessed = pd.DataFrame(user).T[numerical_features_model].fillna(0)

    prediction_model = model.predict(user_preprocessed)
    prediction = dict(zip([user_id], prediction_model))
    return prediction, 200


@app.route('/get/test_users/prediction', methods=['GET'])
def get_test_users_prediction():
    users = test_users_data()
    users_pandas = pd.DataFrame(users)
    predictions = model.predict(users_pandas)
    predictions = dict(zip(users_pandas.index, predictions))

    return predictions, 200


def test_users_data():
    user = {"account_amount_added_12_24m": {"74321": 5463, "93597": 0},
            "account_days_in_dc_12_24m": {"74321": 0.0, "93597": 0.0},
            "account_days_in_rem_12_24m": {"74321": 0.0, "93597": 0.0},
            "account_days_in_term_12_24m": {"74321": 0.0, "93597": 0.0},
            "account_incoming_debt_vs_paid_0_24m": {"74321": 0.0, "93597": 1.3312917645},
            "account_status": {"74321": 1.0, "93597": 1.0421682784},
            "account_worst_status_0_3m": {"74321": 1.0, "93597": 1.1729052913},
            "account_worst_status_12_24m": {"74321": 1.0, "93597": 1.3373475839},
            "account_worst_status_3_6m": {"74321": 1.0, "93597": 1.1852911955},
            "account_worst_status_6_12m": {"74321": 3.0, "93597": 1.2531418765},
            "age": {"74321": 48, "93597": 33},
            "avg_payment_span_0_12m": {"74321": 16.9756097561, "93597": 14.2},
            "avg_payment_span_0_3m": {"74321": 10.0, "93597": 13.5},
            "max_paid_inv_0_12m": {"74321": 26245.0, "93597": 15785.0},
            "max_paid_inv_0_24m": {"74321": 26245.0, "93597": 15785.0},
            "num_active_div_by_paid_inv_0_12m": {"74321": 0.0, "93597": 0.0},
            "num_active_inv": {"74321": 0, "93597": 0},
            "num_arch_dc_0_12m": {"74321": 0, "93597": 0},
            "num_arch_dc_12_24m": {"74321": 0, "93597": 0},
            "num_arch_ok_0_12m": {"74321": 40, "93597": 5},
            "num_arch_ok_12_24m": {"74321": 30, "93597": 2},
            "num_arch_rem_0_12m": {"74321": 1, "93597": 0},
            "num_arch_written_off_0_12m": {"74321": 0.0, "93597": 0.0},
            "num_arch_written_off_12_24m": {"74321": 0.0, "93597": 0.0},
            "num_unpaid_bills": {"74321": 0, "93597": 0},
            "status_last_archived_0_24m": {"74321": 1, "93597": 1},
            "status_2nd_last_archived_0_24m": {"74321": 1, "93597": 1},
            "status_3rd_last_archived_0_24m": {"74321": 1, "93597": 1},
            "status_max_archived_0_6_months": {"74321": 3, "93597": 1},
            "status_max_archived_0_12_months": {"74321": 3, "93597": 1},
            "status_max_archived_0_24_months": {"74321": 3, "93597": 1},
            "recovery_debt": {"74321": 0, "93597": 0},
            "sum_capital_paid_account_0_12m": {"74321": 2515, "93597": 0},
            "sum_capital_paid_account_12_24m": {"74321": 0, "93597": 0},
            "sum_paid_inv_0_12m": {"74321": 185327, "93597": 28855},
            "time_hours": {"74321": 16.4711111111, "93597": 9.8947222222},
            "worst_status_active_inv": {"74321": 1.1217622534, "93597": 1.1217622534}}
    return user


def create_user_response(response):
    user = response
    return user


if __name__ == '__main__':
    try:
        with open('./model.pkl', 'rb') as f:
            model = pickle.load(f)
        f.close()
        print('Model loaded')
    except FileNotFoundError:
        model = create_estimator()
    df = pd.read_csv('./dataset.csv', sep=';', index_col='uuid')
    print('data loaded')
    numerical_features_model = MODEL_FEATURES
    print('0.0.0.0')
    print('not exposed')

    app.run(host='0.0.0.0')

