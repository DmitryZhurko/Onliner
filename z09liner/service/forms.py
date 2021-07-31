from django import forms

# Models
from service.models import Category, Service, Comment, Contractor, Rating, CommentContract


class CommentForm(forms.ModelForm):
    class Meta:

        model = Comment

        fields = ['text']

        widgets = {'text': forms.Textarea(attrs={'rows': 1, 'cols': 50})}



class ServiceForm(forms.ModelForm):
    class Meta:

        model = Service

        fields = ['category', 'title', 'description', 'price', 'address', 'date_active', 'status', 'image']

        widgets = {'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                   'category': forms.Select(attrs={'class': 'form-select', 'cols': 30}),
                   'status': forms.Select(attrs={'class': 'form-select'}),
                   'title': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
                   'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
                   'price': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
                   'date_active': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
                   }


class ContractorForm(forms.ModelForm):
    class Meta:

        model = Contractor

        fields = ['description', 'work', 'phone']

        widgets = {'work': forms.Select(attrs={'class': 'form-select'}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
                   'phone': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
                   }



class RatingForm(forms.ModelForm):


    class Meta:

        model = Rating

        fields = ['rating']

        widget = {'rating': forms.TextInput(attrs={'cols': 10})}


class CommentContractorForm(forms.ModelForm):
    class Meta:

        model = CommentContract

        fields = ['text']

        widgets = {'text': forms.Textarea(attrs={'rows': 1, 'cols': 50})}