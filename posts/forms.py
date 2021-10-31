from django import forms
from .models import Post

MAX_LEN = 200

class PostForm(forms.ModelForm):
    class Meta: #describing form
        model=Post
        fields=['content']

    def clean_content(self): #validating content that is coming through (e.g. limit length)
        content=self.cleaned_data.get('content')
        if len(content)>MAX_LEN:
            raise forms.ValidationError('Too long')
        return content