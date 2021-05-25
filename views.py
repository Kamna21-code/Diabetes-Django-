import numpy as np
import pandas as pd
import sklearn
import pickle
from django.shortcuts import render
from sklearn.preprocessing import MinMaxScaler
from .forms import *
pk_model = pickle.load(open('app/dia_model.pkl', 'rb'))

data = pd.read_csv('app/diabetes.csv')

data_X = data.iloc[:,[1, 4, 5, 7]].values


sc = MinMaxScaler(feature_range = (0,1))
data_scaled = sc.fit_transform(data_X)

# Create your views here.
def homepage(request):
    df = DiabletesForm()
    return render(request, "app/index.html", {'form': df})

def predict(request):
    form = DiabletesForm(request.POST)
    if form.is_valid():
        ls = list()
        ls.append(form.cleaned_data['glucose'])
        ls.append(form.cleaned_data['insulin'])
        ls.append(form.cleaned_data['bmi'])
        ls.append(form.cleaned_data['age'])

    diab_features = [np.array(ls)]
    diab_prediction = pk_model.predict( sc.transform(diab_features) )

    if diab_prediction == 1:
        p = "You have Diabetes, please consult a Doctor."
    elif diab_prediction == 0:
        p = "You don't have Diabetes."
    result = p

    return render(request,'app/index.html', {'prediction_text':'{}'.format(result)})

