from django import forms

from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, AuthenticationForm

from users.models import User
from users.validators import validate_password


class StyleFormMixin:
    ''' Миксин для форм '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(StyleFormMixin, forms.ModelForm):
    ''' Форма пользователя '''
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'avatar',)


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    ''' Форма регистрации пользователя и проверка на соответствие паролей'''
    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        temp_data = self.cleaned_data
        validate_password(temp_data['password1'])
        if temp_data['password1'] != temp_data['password2']:
            raise forms.ValidationError('password_mismatch')
        return temp_data['password2']


class UserLoginForm(StyleFormMixin, AuthenticationForm):
    ''' Форма для авторизации юзера '''
    pass


class UserUpdateForm(StyleFormMixin, forms.ModelForm):
    ''' Форма для изменения юзера '''
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'telegram', 'avatar',)


class UserPasswordChangeForm(StyleFormMixin, PasswordChangeForm):
    ''' Форма для изменения пароля с проверкой '''
    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        validate_password(password1)
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        password_validation.validate_password(password2, self.user)
        return password2
