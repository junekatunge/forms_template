#from socket import fromshare
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from asyncio import format_helpers
from unicodedata import category
from django import forms
from .models import Snippet


class ContactForm(forms.Form): #forms inherits from class object Form
    name = forms.CharField()#normal text field
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question','Question'),('other','Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

#constructor of the contact form
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'category',
            'subject',
            'body',
            Submit('submit','Submit',css_class='btn-success')
        )

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name','body')