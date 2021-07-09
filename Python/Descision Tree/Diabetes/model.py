

from sklearn.datasets import load_diabetes
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

data = load_diabetes()

df = pd.DataFrame(np.c_[data.data,data.target],columns=[list(data.feature_names) + ['target']])

x = df.iloc[:,0:-1]
y = df.iloc[:,-1].map(lambda x : 0 if x > 152 else 1 )

X_train , X_test , Y_train , Y_test = train_test_split(x,y,test_size=0.2,random_state=4500)

sc = StandardScaler()

X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

dt = DecisionTreeClassifier(criterion='gini',max_depth=3)

dt.fit(X_train,Y_train)

with open("diabetes_model.pkl",'wb') as f:
    pickle.dump(dt,f)

print(dt.predict(X_test))