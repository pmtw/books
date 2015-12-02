
from django import forms
from post.models import Post, Comment
from django.test import TestCase

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('created', 'modified')
    
    """    
    Validator obecnosci contentu we wpisie ksiazki     
    """    
    def valid_book_content(self):
        content = self.cleaned_data['content']
        try:
            self.Post.content.get(content=content)
        except Post.DoesNotExist:
            self.content = Post.title.get()
        else:
            Post.content.save()
       


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('','')
        
    '''
    Validator obecnosci slow niedozwolonych w komentarzu
    '''
    def clean_content(self):
        vulgars = ["fuck","pipa","dupa","brzydkieslowa"]
        content = self.cleaned_data['content']
        for vulgar in vulgars:
            if vulgar in content:
                raise forms.ValidationError(" Vulgars is not allowed!")
        return content
        