from django import forms


class ListnameForm(forms.ModelForm):
	listname = forms.CharField(initial='Your fancy list name', label='listname', max_length=100)
