from django import forms

class DiabletesForm(forms.Form):
    glucose = forms.FloatField()
    insulin  = forms.FloatField()
    bmi = forms.FloatField()
    age =  forms.IntegerField()