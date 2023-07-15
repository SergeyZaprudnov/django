from django.forms import ModelForm, ValidationError, BaseInlineFormSet
from my_home.models import Product, Version

stop_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('last_modified_date', 'date_of_creation', 'last_modified_date')

        def cleaned_name(self):
            cleaned_name = self.cleaned_data('name')

            if cleaned_name in stop_words:
                raise ValidationError('Вы используете запрещенные слова')
            return cleaned_name

        def clean_description(self):
            cleaned_description = self.cleaned_data['description']

            if cleaned_description in stop_words:
                raise ValidationError('Вы используете запрещенные слова')
            return cleaned_description


class VersionProduct(BaseInlineFormSet):
    def clean(self):
        super().clean()
        count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_active') is True:
                count += 1

        if count > 1:
            raise ValidationError('Вы имеете больше одной версии')
