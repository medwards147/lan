from __future__ import unicode_literals

from django import forms
#from django.core.urlresolvers import reverse


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)