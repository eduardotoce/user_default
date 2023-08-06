import pathlib
import pickle
from time import time

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, f1_score, make_scorer
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

from src.config.config import DATA_DIRECTORY, MODELS_DIRECTORY, MODEL_FEATURES


def create_estimator():

    df = pd.read_csv(pathlib.Path.joinpath(DATA_DIRECTORY, 'dataset.csv'), sep=';', index_col='uuid')

    numerical_features = df.select_dtypes(include=np.number).columns

    # TODO: do this inside the pipeline
    for f in numerical_features:
        df[f] = df[f].fillna(df[f].mean())

    numerical_features_model = MODEL_FEATURES

    y = df['default'].apply(lambda x: 0 if x != 1 else x)
    X = df[numerical_features_model]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, stratify=y)
    assert 'default' not in X.columns

    start = time()

    rf = RandomForestClassifier(random_state=1506)

    param_grid = {'max_features': ['auto', 'log2'],
                  'n_estimators': [20, 50, 100],
                  'min_impurity_decrease': [0, 0.01, 0.03]}
    scoring = {'score': make_scorer(f1_score)}

    # TODO: do stratified cv folds
    cross_val_rf = GridSearchCV(rf, param_grid, scoring=make_scorer(f1_score), cv=3, verbose=1)
    cross_val_rf.fit(X_train[numerical_features_model], y_train)

    print("This took %0.3fs" % (time() - start))

    predictions_rf = cross_val_rf.best_estimator_.predict(X_test[numerical_features_model])
    prob_predictions_rf = cross_val_rf.best_estimator_.predict_proba(X_test[numerical_features_model])
    cm_rf = confusion_matrix(y_test, predictions_rf)

    print(cm_rf)

    estimator = cross_val_rf.best_estimator_

    with open(pathlib.Path.joinpath(MODELS_DIRECTORY, 'model.pkl'), 'wb') as f:
        pickle.dump(estimator, f)
    f.close()

    return estimator

