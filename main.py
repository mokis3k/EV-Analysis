import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Input data from Power BI
df = dataset.copy()

# Characteristics and target variable
features = ['Length (mm)', 'Width (mm)', 'Height (mm)', 'Car Body Type', 'Torque (Nm)']
target = 'Towing Capacity (kg)'

# Separate data with filled target and with null in target
df_train = df[df[target].notnull()]
df_predict = df[df[target].isnull()]

if len(df_predict) > 0:

    X_train = df_train[features]
    y_train = df_train[target]

    X_predict = df_predict[features]

    categorical_features = ['Car Body Type']
    numeric_features = ['Length (mm)', 'Width (mm)', 'Height (mm)', 'Torque (Nm)']

    # Transformer for coding categories
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
        ], remainder='passthrough')

    # Model with preprocessing in pipelines
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    # Training the model
    model.fit(X_train, y_train)

    # Predictions for strings with null
    y_pred = model.predict(X_predict)

    # Filling gaps with predicted values
    df.loc[df[target].isnull(), target] = y_pred

# Return the final DataFrame to Power BI
dataset = df
