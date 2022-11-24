from django import forms
from ckeditor.widgets import CKEditorWidget

from cellphone.models import Cellphone

class CellphoneForm(forms.ModelForm):
    brand = forms.CharField(
        label="Cellphone brand",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cellphone-brand",
                "placeholder": "Cellphone brand",
                "required": "True",
            }
        ),
    )

    model = forms.IntegerField(
        label="Model:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "cellphone-model",
                "placeholder": "Cellphone model",
                "required": "True",
            }
        ),
    )

    description = forms.CharField(
        label="Description:",
        required=False,
        widget=CKEditorWidget(),
    )

    image = forms.ImageField()

    class Meta:
        model = Cellphone
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
                "placeholder": "Enter a comment...",
                "required": "True",
                "max_length": 500,
                "min_length": 10,
                "rows": 2,
                "cols": 10,
                "style":"min-width: 100%",
            }
        ),
    )
       