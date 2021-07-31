from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import SaleFlat, Photo, Rent, VARIANT
from django.forms import ModelForm, IntegerField, NumberInput, Textarea, TextInput, CheckboxInput, \
    CheckboxSelectMultiple


class SaleFlatForm(ModelForm):
    class Meta:
        model = SaleFlat
        fields = ['cost', 'cost_dollar', 'floor', 'total_area', 'living_space',
                  'kitchen_area', 'ceiling_height', 'number_of_rooms',
                  'description', 'telephone',  'address', 'flat_or_apartment']


class FullFlatForm(SaleFlatForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control col-md-2'}),label='')

    class Meta(SaleFlatForm.Meta):
        fields = SaleFlatForm.Meta.fields + ['images',]
        widgets = {
            'cost': NumberInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите цену',


            }),
            'cost_dollar': NumberInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите курс доллара',

            }),
            'floor': NumberInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите этаж'
            }),
            'number_of_rooms': NumberInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите количество комнат'
            }),
            'description': Textarea(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите описание'
            }),
            'telephone': TextInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите телефон'
            }),
            'address': TextInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите адрес'
            }),
            'total_area': TextInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите общую площадь'
            }),
            'living_space': TextInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите жилую площадь'
            }),
            'kitchen_area': TextInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите площадь кухни'
            }),
            'ceiling_height': TextInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите высоту потолка'
            }),
        }


class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = ['cost', 'cost_dollar', 'floor', 'number_of_rooms',
                  'description', 'telephone', 'address', 'tv', 'furniture', 'plate', 'refrigerator', 'internet', 'conditioning', 'washer', 'flat_or_apartment']


class FullRentForm(RentForm):
    photos = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control col-md-2',
                                                                    }), label='')

    class Meta(RentForm.Meta):
        fields = RentForm.Meta.fields + ['photos',]
        widgets = {
            'cost': NumberInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите цену',

            }),
            'cost_dollar': NumberInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите курс доллара',
            }),
            'floor': NumberInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите этаж'
            }),
            'number_of_rooms': NumberInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите количество комнат'
            }),
            'description': Textarea(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите описание',
                # 'cols': 30,
                # 'rows': 2,
            }),
            'telephone': TextInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите телефон'
            }),
            'address': TextInput(attrs={
                'class': 'form-control col-md-2',
                'placeholder': 'введите адрес'
            }),

        }

