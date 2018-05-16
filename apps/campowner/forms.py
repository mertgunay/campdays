from django import forms
from campowner.models import CampOwner

class CampOwnerRegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CampOwnerRegisterForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder': 'Kamp Alanı Adı',
            'autocomplete': 'off',
        })
        self.fields['address'].widget.attrs.update({
            'placeholder': 'Adress',
            'class' : 'form-control',
        })

    class Meta:
        model = CampOwner
        fields = {
            'name',
            'address',
            'image',
            'desc',
            'phone_number',
            'web_site',
        }

    def save(self, commit=True):
        form = super(CampOwnerRegisterForm, self).save(commit=False)
        if commit:
            form.save()
        return form
