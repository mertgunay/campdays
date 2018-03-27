from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext, gettext_lazy as _

User = get_user_model()

class UserRegisterForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder': 'Kullanıcı Adı',
            'autocomplete': 'off',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'E-Posta',
            'class' : 'form-control',
        })
        self.fields['password'].widget.attrs.update({
            'class' : 'form-control',
            'placeholder': 'Şifre',
        })

    class Meta:
        model = User
        fields = {
            'username',
            'email',
            'password',
        }

        widgets = {
            'password': forms.PasswordInput,
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 6 or len(username) > 30:
            raise forms.ValidationError(_(
                'Kullanıcı adı en az 6 en çok 30 karakter içerlemidir'
            ))
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Bu email adresi kullanımda")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6 or len(password) > 30:
            raise forms.ValidationError(_(
                'Şifre adı en az 6 en çok 30 karakter içerlemidir'
            ))
        return password

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(
        label='Şifre oluşturun', widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Şifrenizi onaylayın', widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = {
            'email',
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Şifreler eşleşmiyor")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(
        label='Password',
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"../password/\">this form</a>."
        ),
    )

    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
