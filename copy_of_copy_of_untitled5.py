# -*- coding: utf-8 -*-
"""Copy of Copy of Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EfBlzLbyAnAgh_DzRRTSw7yk2cZ366XF
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline

import os
print(os.listdir())

import warnings
warnings.filterwarnings('ignore')

dataset = pd.read_csv("Heart_Disease_Prediction.csv")

type(dataset)

dataset.shape

dataset.head(5)

dataset.sample(7)

dataset.describe()

dataset.info()

info = ["age","1: male, 0: female","chest pain type, 1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic","resting blood pressure"," serum cholestoral in mg/dl","fasting blood sugar > 120 mg/dl","resting electrocardiographic results (values 0,1,2)"," maximum heart rate achieved","exercise induced angina","oldpeak = ST depression induced by exercise relative to rest","the slope of the peak exercise ST segment","number of major vessels (0-3) colored by flourosopy","thal: 3 = normal; 6 = fixed defect; 7 = reversable defect"]



for i in range(len(info)):
    print(dataset.columns[i]+":\t\t\t"+info[i])

dataset["Heart Disease"].describe()

dataset["Heart Disease"].unique()

y = dataset["Heart Disease"]

sns.countplot(y)

print("Percentage of patience without heart problems: "+str(round(Heart Disease[Absence]*100/303,2)))
print("Percentage of patience with heart problems: "+str(round(Heart Disease[Presence]*100/303,2)))

#Alternatively,
# print("Percentage of patience with heart problems: "+str(y.where(y==1).count()*100/303))
# print("Percentage of patience with heart problems: "+str(y.where(y==0).count()*100/303))

# #Or,
# countNoDisease = len(df[df.target == 0])
# countHaveDisease = len(df[df.target == 1])

dataset["Sex"].unique()

sns.barplot(dataset["Sex"],y)

dataset["Chest pain type"].unique()

sns.barplot(dataset["Chest pain type"],y)

sns.countplot(dataset["Chest pain type"])

dataset["FBS over 120"].describe()

dataset["FBS over 120"].unique()

sns.barplot(dataset["FBS over 120"],y)

sns.countplot(dataset["FBS over 120"])

dataset["EKG results"].unique()

sns.barplot(dataset["EKG results"],y)

sns.countplot(dataset["EKG results"])

dataset["Exercise angina"].unique()

sns.barplot(dataset["Exercise angina"],y)

sns.countplot(dataset["Exercise angina"])

sns.countplot(dataset["Cholesterol"])

sns.countplot(dataset["BP"])

sns.countplot(dataset["Age"])

dataset["Slope of ST"].unique()

sns.barplot(dataset["Slope of ST"],y)

sns.countplot(dataset["Slope of ST"])

dataset["Number of vessels fluro"].unique()

sns.countplot(dataset["Number of vessels fluro"])

sns.barplot(dataset["Number of vessels fluro"],y)

sns.distplot(dataset["Thallium"])