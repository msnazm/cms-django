from django import forms
from .models import Comment
from django.core.exceptions import ValidationError

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "نام شما"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "پیام بگذارید!"
        })
    )
    
    def clean_author(self):
        super().clean()
        author = self.cleaned_data.get('author')
        if not author:
            raise ValidationError("test")
        return author
        
