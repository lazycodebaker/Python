
import numpy as np
from sklearn.datasets import load_boston
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pickle

boston = load_boston()

x = boston.data
y = boston.target

model = LinearRegression()

x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.2,random_state=0)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

accuracy = model.score(x_test,y_test)

with open("boston_model",'wb') as f:
    pickle.dump(model,f)

