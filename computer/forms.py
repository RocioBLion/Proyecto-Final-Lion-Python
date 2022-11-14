from django import forms

from computer.models import Computer

class ComputerForm(forms.Form):
    brand = forms.CharField(
        label="Brand:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "computer-brand",
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
                "class": "computer-model",
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
                "class": "computer-description",
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
                "class": "computer-price",
                "placeholder": "Value",
                "required": "True",
            }
        ),
    )       
