from django import forms
from Farmer import models


# FA registering Farmer
class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.Farmer
        exclude = ()
