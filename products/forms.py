from django import forms
from django.forms.widgets import Textarea
from .models import Product

class RawProductForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField(required=False, widget=Textarea)
	price = forms.DecimalField(initial=0.00)

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price',
		]
