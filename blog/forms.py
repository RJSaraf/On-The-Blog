from django import forms
from blog.models import Post, Comment
from django.contrib.auth.models import User

#blog

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','text','postimage')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'postcontent w3-container editable'}),            
            'postimage':forms.FileInput(attrs={'class':'w3-button'}),
        }
        

class CommentForm(forms.ModelForm):

        class Meta:
            model = Comment
            fields = ('text',)

            widgets = {
                
                'text':forms.Textarea(attrs={'class':'postcontent editable'})
    
            }


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password','first_name','last_name','email')

        widgets = {

            'username':forms.TextInput(attrs={'class':'textinputclass'}),
            'password':forms.TextInput(attrs={'class':'textinputclass'}),
            'first_name':forms.TextInput(attrs={'class':'textinputclass'}),
            'last_name':forms.TextInput(attrs={'class':'textinputclass'}),
            'email':forms.TextInput(attrs={'class':'textinputclass'}),

        }