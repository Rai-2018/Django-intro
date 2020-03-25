from django import forms

from .models import Product

#inherit the class forms.ModelForm
class ProductForm(forms.ModelForm):
	#adjusting the form 
	description = forms.CharField(
				required = False,
				widget = forms.Textarea(
							attrs = {
								"class" : "new-class",
								"placeholder":"HI",
								"rows" : 20,
								"column" : 50
							}))

	#Class meta is inner class in djnago model - with some options attached, etc.. associated db table name ..
	#reqired in ModelForm
	class Meta: 
		model = Product
		fields = [ 
			"title",
			"description",
			"price"
		]
	#Post django form cleaning, django clean the form itself initially and trigger clean_title
	def clean_title(self,*args,**kwargs):
		title = self.cleaned_data.get("title")
		if not "CFE" in title:
			raise forms.ValidationError("Not valid title")
		return title

class RawProductForm(forms.Form):
	#required is default to true, hence thats why it says its required on the form for html
	#look at widget under django form
	title = forms.CharField()
	description = forms.CharField(
					required = False,
					widget = forms.Textarea(
								attrs = {
									"class" : "new-class",
									"rows" : 20,
									"column" : 50
								}))
	price = forms.DecimalField()