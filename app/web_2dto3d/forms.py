from django import forms
from .models import UsersGLB


class UsersGLBForm(forms.ModelForm):
    class Meta:
        model = UsersGLB
        fields = ["glb_file"]


# Path: app/web_2dto3d/models.py
