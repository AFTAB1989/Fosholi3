from django import forms 
from UpChairman import models


class registerForm(forms.ModelForm):
    class Meta: 
        model = models.UpChairman
        exclude = ()
 