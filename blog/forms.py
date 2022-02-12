from django import  forms
from django.forms import fields
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = 'title' , 'content', 'image' ,'category', 'status'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields='name', 'body'
        
        widgets={
            'Name':forms.TextInput(),
            'body': forms.Textarea()
        }
        # attrs={'class':'form-control'}