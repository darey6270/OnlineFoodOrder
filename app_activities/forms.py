from django import forms
from django.utils.translation import gettext_lazy as _
from FoodOrdering.models import Category, Product


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price')