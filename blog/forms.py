from django import forms

from .models import Article

#inherit the class forms.ModelForm
class ArticleForm(forms.ModelForm):
	#adjusting the form 
	text = forms.CharField(
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
		model = Article
		fields = [ 
			"text"
		]

	#can do validation with def clean_<fieldname>, validation on the form
	def clean_text(self):
		text = self.cleaned_data.get("text")
		if text.lower() == "abc":
			raise forms.ValidationError("WRONG")
		return text