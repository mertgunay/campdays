from django import forms
from comment.models import Comment

class CommentForm(forms.ModelForm):

    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.CharField(widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder': 'Yorum Yaz',
        })

    class Meta:
        model = Comment
        fields = {
            "content",
        }

    #parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
