from django import forms
from FieldAgent import models


# From to register new upchaiman by upchairman model
class registerForm(forms.ModelForm):
    class Meta:
        model = models.SeasonalServey
        exclude = ()
