from django import forms
from .models import PostProject
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, workTag

class ProjectForm(forms.Form):
    PPtitle = forms.CharField(
        label='タイトル',
        max_length=200,
        required=True,
    )

    PPcontext = forms.CharField(
        label='Context',
        max_length=1000,
        required=True,
        widget=forms.TextInput()
    )

class WorkTagForm(forms.Form):
    model = workTag
    fields = ["TagName"]
