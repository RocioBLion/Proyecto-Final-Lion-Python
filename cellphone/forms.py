from django import forms

from cellphone.models import Cellphone

class CellphoneForm(forms.Form):
    brand = forms.CharField(
        label="Brand:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cellphone-brand",
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
                "class": "cellphone-model",
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
                "class": "cellphone-description",
                "placeholder": "Characteristics",
                "required": "True",
            }
        ),
    )    
    price = forms.IntegerField(
        label="Price:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cellphone-price",
                "placeholder": "Value",
                "required": "True",
            }
        ),
    )     
