from django import forms
from UNO import models


# From to register new upchaiman by upchairman model
class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.UNO
        exclude = ()
