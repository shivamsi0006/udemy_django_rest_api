from django import forms

from .models import update 


class UpdateModelForm(forms.ModelForm ):
    class Meta:
        model=update
        fields=[
            'user',
            'content',
            'image'
        ]

