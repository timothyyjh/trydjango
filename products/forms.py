from django import forms
from django.forms.widgets import Textarea
from .models import Product

class ProductForm(forms.ModelForm):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Your Title'}))
	description = forms.CharField(
		required=False, 
		widget=Textarea(attrs={
			'placeholder' : 'Your Description',
			'rows':20,
			'cols':150
		}))
	price = forms.DecimalField(initial=0.00)
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price',
		]
		
class RawProductForm(forms.Form):
	title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder' : 'Your Title'}))
	description = forms.CharField(
		required=False, 
		widget=Textarea(attrs={
			'placeholder' : 'Your Description',
			'rows':20,
			'cols':150
		}))
	price = forms.DecimalField(initial=0.00)

