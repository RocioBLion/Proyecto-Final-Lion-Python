from django import forms

from accessorie.models import Accessorie

class AccessorieForm(forms.Form):
    brand = forms.CharField(
        label="Brand:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "accessorie-brand",
                "placeholder": "Brand",
                "required": "True",
            }
        ),
    )
    model = forms.CharField(
        label="Model:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "accessorie-model",
                "placeholder": "Model",
                "required": "True",
            }
        ),
    )    
    description = forms.CharField(
        label="Description:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "accessorie-description",
                "placeholder": "Characteristics",
                "required": "True",
            }
        ),
    )    
    