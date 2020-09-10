from django import forms
from .validators import validate_url_endings, validate_url_starting


class SubmiUrlForm(forms.Form):

    url = forms.URLField(
        label="",
        validators=[validate_url_endings, validate_url_starting],
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "type": "url",
                "placeholder": "Enter Long URL",
            }
        ),
    )
    shortcode = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "type": "text",
                "placeholder": "Enter custom shortcode",
                "name": "shortcode",
                "id": "ifYes",
                "style": "display : none",
            }
        ),
        required=False,
    )
