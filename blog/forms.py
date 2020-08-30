from django import forms
from .models import Post
from .models import Add

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

class AddForm(forms.ModelForm):
    class Meta:
        model = Add
        fields = ('title', 'text',)
