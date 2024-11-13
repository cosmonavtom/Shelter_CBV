import datetime

from django import forms

from dogs.models import Dog, Parent
from users.forms import StyleFormMixin


class DogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ('owner', 'is_active', 'views')

    def clean_birth_date(self):
        if self.cleaned_data['birth_date']:
            cleaned_data = self.cleaned_data['birth_date']
            if cleaned_data is None:
                return None
            now_year = datetime.datetime.now().year
            if now_year - cleaned_data.year > 100:
                raise forms.ValidationError('Собака должна быть моложе 100 лет')
            return cleaned_data
        return None

class DogAdminForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Dog
        fields = '__all__'

    @staticmethod
    def clean_birth_date():
        DogForm.clean_birth_date()


class ParentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Parent
        fields = '__all__'
