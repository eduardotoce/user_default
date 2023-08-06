import pathlib
import pickle

import pandas as pd

from src.config.config import DATA_DIRECTORY, MODELS_DIRECTORY, MODEL_FEATURES

df = pd.read_csv(pathlib.Path.joinpath(DATA_DIRECTORY, 'dataset.csv'), index_col=0)

# TODO: create preprocessing pipeline
with open(pathlib.Path.joinpath(MODELS_DIRECTORY, 'model.pkl'), 'rb') as f:
    model = pickle.load(f)
f.close()

# TODO: create train_test_split for defaulters
predictions_rf = model.predict(df[MODEL_FEATURES])
prob_predictions_rf = model.predict_proba(df[MODEL_FEATURES])

# TODO: generate csv with results
print(prob_predictions_rf)

