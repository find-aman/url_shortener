from django import forms
from .validators import validate_url_endings


class SubmiUrlForm(forms.Form):
    url = forms.URLField(label="Submit URL", validators=[validate_url_endings])
