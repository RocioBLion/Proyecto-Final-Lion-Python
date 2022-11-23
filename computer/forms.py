from django import forms
from ckeditor.widgets import CKEditorWidget

from computer.models import Computer

class ComputerForm(forms.ModelForm):
    brand = forms.CharField(
        label="brand the Computer",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "computer-brand",
                "placeholder": "Brand the computer",
                "required": "True",
            }
        ),
    )

    model = forms.IntegerField(
        label="Model:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "computer-model",
                "placeholder": "Model the computer",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(),
    )

    image = forms.ImageField()

    class Meta:
        model = Computer
        fields = ["brand", "model", "description", "price"]


class CommentForm(forms.Form):
    comment_text = forms.CharField(
        label="",
        required=False,
        max_length=500,
        min_length=10,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "comment-text",
                "placeholder": "Enter a Comment...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )


     
