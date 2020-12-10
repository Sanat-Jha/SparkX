from django import forms
from .models import Post
class POST(forms.ModelForm):
    class Meta:
        model = Post
        fields=  ["Image","Caption"]