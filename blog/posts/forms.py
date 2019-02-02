from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']

    def clean_title(self):
        cleaned_data = self.cleaned_data
        if len(cleaned_data["title"]) <= 2:
            raise forms.ValidationError("Введте заголовок > 2")
        return cleaned_data['title']
