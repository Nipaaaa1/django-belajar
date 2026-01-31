from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(max_length=16, required=True, label="Name")
    age = forms.IntegerField(label="Age")
    job = forms.CharField(max_length=16, required=False, label="Job")
