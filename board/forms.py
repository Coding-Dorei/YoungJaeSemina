from django import forms
from .models import Document, Comment


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'title',
            'content'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content'
        ]