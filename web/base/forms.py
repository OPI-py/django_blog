from django import forms


class InputForm(forms.Form):
	first_name = forms.CharField(max_length=200)
	last_name = forms.CharField(max_length=200)
	r_n = forms.IntegerField(help_text="Enter 6 digit number")
	password = forms.CharField(widget=forms.PasswordInput())
