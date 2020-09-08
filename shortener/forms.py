from django import forms
from .validators import validate_url_endings


class SubmiUrlForm(forms.Form):
    url = forms.URLField(
        label="",
        validators=[validate_url_endings],
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "type": "text",
                "placeholder": "Enter Long URL",
            }
        ),
    )
