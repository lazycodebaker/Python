
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

data = load_breast_cancer()

df = pd.DataFrame(np.c_[data.data,data.target],columns=[list(data.feature_names) + ['target']])

x = df.iloc[:,0:-1]
y = df.iloc[:,-1]

X_train , X_test ,Y_train , Y_test = train_test_split(x,y,test_size = 0.2,random_state = 42)

model_classifier = DecisionTreeClassifier(criterion='gini')

sc = StandardScaler()
sc.fit(X_train)

X_train = sc.fit_transform(X_train)
X_test  = sc.fit_transform(X_test)

model_classifier.fit(X_train,Y_train)

with open("cancer_tree_model.pkl",'wb') as f:
    pickle.dump(model_classifier,f)
    
 
 y_pred = model.predict(X_test)
 
 
 print(mean_squared_error(y_test,y_pred))

