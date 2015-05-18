from django import forms
#from django.admin 

class MailForm(forms.Form):
	mail = forms.EmailField();

class Newsletter(forms.Form):
	title = forms.CharField();
	pub_date = forms.DateTimeField();
	message = forms.CharField(widget=forms.Textarea)