from django import forms
from main import models

class ContactUsForm(forms.ModelForm):

	class Meta:
		model = models.ContactUs

	def __init__(self, *args, **kwargs):
        super(ContactUsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Name'})