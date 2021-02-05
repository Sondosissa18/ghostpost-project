from django import forms

from ghostpost_app.models import GhostPost



class CreatePostForm(forms.Form):

    text = forms.CharField(max_length=100)

    ROAST_CHOICES = [
    (True, 'Boast'),
    (False, 'Roast'),
    ]

    ghostpost = forms.ChoiceField(
        choices=ROAST_CHOICES,
        widget=forms.Select(),
        label='Is roast? ')
   




    