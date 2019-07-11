from django import forms

class ConvertSmiles(forms.Form):
    smiles = forms.CharField(label='smiles', max_length=10000)

    