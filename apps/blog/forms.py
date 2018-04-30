from django import forms

from blog.models import Post


class  PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder': '',
            'autocomplete': 'off',
        })
        self.fields['image'].widget.attrs.update({
            'placeholder': '',
            'class' : 'form-control',
        })
        self.fields['content'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder': '',
        })

    class Meta:
        model = Post
        fields = {
            "title",
            "image",
            "content",
        }

        widgets = {
            'password': forms.PasswordInput,
        }
