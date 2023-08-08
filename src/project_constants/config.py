import pathlib

current_path = pathlib.Path(__file__).resolve().parent

print(current_path)

# Root folder
PROJECT_ROOT = current_path.parent

print(PROJECT_ROOT)

# Data
DATA_DIRECTORY = pathlib.Path.joinpath(PROJECT_ROOT, "data")
MODELS_DIRECTORY = pathlib.Path.joinpath(PROJECT_ROOT, "models")

MODEL_FEATURES = ['account_amount_added_12_24m',
                  'account_days_in_dc_12_24m',
                  'account_days_in_rem_12_24m',
                  'account_days_in_term_12_24m',
                  'account_incoming_debt_vs_paid_0_24m',
                  'account_status',
                  'account_worst_status_0_3m',
                  'account_worst_status_12_24m',
                  'account_worst_status_3_6m',
                  'account_worst_status_6_12m',
                  'age',
                  'avg_payment_span_0_12m',
                  'avg_payment_span_0_3m',
                  'max_paid_inv_0_12m',
                  'max_paid_inv_0_24m',
                  'num_active_div_by_paid_inv_0_12m',
                  'num_active_inv',
                  'num_arch_dc_0_12m',
                  'num_arch_dc_12_24m',
                  'num_arch_ok_0_12m',
                  'num_arch_ok_12_24m',
                  'num_arch_rem_0_12m',
                  'num_arch_written_off_0_12m',
                  'num_arch_written_off_12_24m',
                  'num_unpaid_bills',
                  'status_last_archived_0_24m',
                  'status_2nd_last_archived_0_24m',
                  'status_3rd_last_archived_0_24m',
                  'status_max_archived_0_6_months',
                  'status_max_archived_0_12_months',
                  'status_max_archived_0_24_months',
                  'recovery_debt',
                  'sum_capital_paid_account_0_12m',
                  'sum_capital_paid_account_12_24m',
                  'sum_paid_inv_0_12m',
                  'time_hours',
                  'worst_status_active_inv']
