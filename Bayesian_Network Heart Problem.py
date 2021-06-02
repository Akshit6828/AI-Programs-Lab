import pandas as pd
import numpy as np
from urllib.request import urlopen
from pgmpy import models
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination


names="Age,Sex,CP,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,heartdisease" 
names=names.split(",")
#names=names is used to make Alphabets as title
#data = pd.read_csv('heart.csv') --- Older Data.
data=pd.read_csv(urlopen("https://bit.do/heart-disease"),names=names) #Source of CSV File
data = data.replace('?',np.nan)

#Displaying DATA
print('Few examples from the dataset are given below\n')
print(data.head())

#Model Bayesian Network
model =BayesianModel(([('Age','trestbps'),('Age','fbs'),('Sex','trestbps'),('exang','trestbps'),('trestbps','heartdisease'),('fbs','heartdisease'),('heartdisease','restecg'),
('heartdisease','thalach'),('heartdisease','chol')]))


print('\n Learning CPD using Maximum likelihood estimators')
model.fit(data,estimator=MaximumLikelihoodEstimator)

# Inferencing with Bayesian Network
print('\n Inferencing with Bayesian Network:')
HeartDisease_infer = VariableElimination(model)

#computing the Probability of HeartDisease given Age
print('\n 1. Probability of HeartDisease given Age=30')
q=HeartDisease_infer.query(variables=['heartdisease'],evidence={'Age':30})
print(q)


#computing the Probability of HeartDisease given cholesterol
print('\n 2. Probability of HeartDisease given cholesterol=100')
q=HeartDisease_infer.query(variables=['heartdisease'],evidence={'chol':100})
print(q)
