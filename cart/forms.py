# forms.py
from django import forms

class AddToCartForm(forms.Form):
    selected_date = forms.DateField(label='Select a date', input_formats=['%Y-%m-%d'])
