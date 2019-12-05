from django import forms
from FieldAgent import models


# From to register new fieldAgent by UNO model
class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.FieldAgent
        exclude = ()
