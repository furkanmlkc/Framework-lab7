from django import forms

class NumForm(forms.Form):
    number1 = forms.IntegerField(label='number 1')
    number2 = forms.IntegerField(label='number 2')
    number3 = forms.IntegerField(label='number 3')
