
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import pickle


model = pickle.load(open("gre_model.pkl",'rb'))

data =[
        {
            'GRE Score' : 327,
            "TOEFL Score" : 111,
            "University Rating" : 4,
            "SOP" : 2.5,
            "LOR":2,
            "CGPA" : 8.5,
            "Research" : 1
        },
        {
            'GRE Score' : 345,
            "TOEFL Score" : 115,
            "University Rating" : 10,
            "SOP" : 2.5,
            "LOR":2,
            "CGPA" : 9,
            "Research" : 1
        },
        {
            'GRE Score' : 330,
            "TOEFL Score" : 115,
            "University Rating" : 3,
            "SOP" : 2.7,
            "LOR":2.4,
            "CGPA" : 8.7,
            "Research" : 1
        }
]
    

sample = pd.DataFrame(data)
print(sample.iloc[:,:])

print(model.predict(sample))