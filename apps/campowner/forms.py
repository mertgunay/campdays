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
            'placeholder': 'Açık Adres',
            'class' : 'form-control',
        })
        self.fields['web_site'].widget.attrs.update({
            'placeholder': 'Web Site',
            'class' : 'form-control',
        })
        self.fields['phone_number'].widget.attrs.update({
            'placeholder': 'Telefon Numarası',
            'class' : 'form-control',
        })
        self.fields['desc'].widget.attrs.update({
            'placeholder': 'Açıklama',
            'class' : 'form-control',
        })

        self.order_fields(sorted(self.fields.keys()))

    class Meta:
        model = CampOwner
        fields = {
            'image',
            'address',
            'name',
            'desc',
            'phone_number',
            'web_site',
        }

        widgets = {
            'desc': forms.Textarea,
        }

    def save(self, commit=True):
        form = super(CampOwnerRegisterForm, self).save(commit=False)
        if commit:
            form.save()
        return form
