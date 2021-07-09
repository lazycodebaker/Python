
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import activations # convert cate3goriea to binary

from sklearn.preprocessing import MinMaxScaler

data = pd.DataFrame(pd.read_csv("car_datasets.csv"))

data = data.drop("Car_Name",axis=1)

y = data['Selling_Price']
x = data.drop("Selling_Price",axis=1)

input_cols = ["Year","Present_Price","Kms_Driven","Owner"]
categorical_cols = ["Fuel_Type","Seller_Type","Transmission"]
output_cols = ["Selling_Price"]

for col in categorical_cols:
    x[col] = pd.factorize(x[col])[0]

x = np.array(x)
y = np.array(y)

min_max_scaler = MinMaxScaler()
X_scale = min_max_scaler.fit_transform(x)

x_train , x_test , y_train , y_test = train_test_split(X_scale,y,test_size=0.1,random_state=42)

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32,input_shape=(7,),activation='relu'),
    tf.keras.layers.Dense(32,activation='relu'),
    tf.keras.layers.Dense(1,activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='mae',
              metrics=['accuracy'])

model.fit(x_train,y_train,epochs=100)

print(model.evaluate(x_test,y_test))

y_pred = model.predict(x_test)

print(y_pred[:5],y_test[:5])
