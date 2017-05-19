from django import forms
from .models import SingUp

class ContactForm(forms.Form):
	fullname = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

class SingUpForm(forms.ModelForm):
	class Meta:
		model = SingUp
		fields = ['fullname', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extention = provider.split('.')
		#if not domain == 'USC':
		#	raise forms.ValidationError("Please use USC email")
		if not extention == "edu":
			raise forms.ValidationError("Please, use a valid .edu email address")
		#if not ".edu" in email:
		#	raise forms.ValidationError("Please, use a valid .edu email address")
		return email

	def clean_fullname(self):
		fullname = self.cleaned_data.get('fullname')
		return fullname
