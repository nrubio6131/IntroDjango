from dataclasses import fields
from django import forms
from .models import Post,user

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('tittle','content')
class PostCreateUser(forms.ModelForm):
    class Meta:
        model=user
        fields=('name','number','decimal','email')



