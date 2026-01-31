from django import forms

from .models import Todo

class PersonForm(forms.Form):
    name = forms.CharField(max_length=16, required=True, label="Name")
    age = forms.IntegerField(label="Age")
    job = forms.CharField(max_length=16, required=False, label="Job")

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "done", "datetime", "priority"]

        widgets = {
            "datetime": forms.DateInput(attrs={ "type": "date" })
        }
