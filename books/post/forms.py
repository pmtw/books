
from django import forms
from post.models import Post, Comment
from django.test import TestCase

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('created', 'modified')
        
'''        
    def valid_content(self):
        content = self.cleaned_data['content']
        try:
            Post.self.get(content=content)
        except Post.DoesNotExist:
            self.content = Post.title.get()
        else:
            Post.content.save()
'''        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('','')
        
    def clean_content(self):
        vulgars = ["fuck","pipa","dupa","kurwa"]
        content = self.cleaned_data['content']
        for vulgar in vulgars:
            if vulgar in content:
                raise forms.ValidationError(" Vulgars is not allowed!")
        return content
        