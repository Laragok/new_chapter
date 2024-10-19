#!/usr/bin/env python3

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data=pd.read_csv("random.csv")


X = data.drop("temperature", axis=1)
y = data['humidity']

X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.2)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print( "Accuracy:", accuracy)
