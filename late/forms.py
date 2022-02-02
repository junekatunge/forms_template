#from socket import fromshare
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from asyncio import format_helpers
from unicodedata import category
from django import forms
from .models import Snippet
from django.core.validators import RegexValidator# for letters only
 
 #widget for creating the other field for lname
class NameWidget(forms.MultiWidget):

    def __init__(self, attrs=None):
        super().__init__([
            forms.TextInput(),
            forms.TextInput()
         ],attrs )# to pass the atttributes

    def decompress(self, value):
        if value:
            return value.split(' ')
        return ['','']


#to create the multi-value field - one field with many other subfields
class NameField(forms.MultiValueField):

    widget = NameWidget

    def __init__ (self,*args,**kwargs):

        fields = (
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+','Enter a valid first name (only letters)')
            ]),#fname
            forms.CharField(validators=[
                RegexValidator(r'[a-zA-Z]+','Enter a valid second name (only letters)')
            ])#sname
        )
        #calling __init__ for the parent class which is MultiValueField
        super().__init__(fields,*args,**kwargs)

    def compress(self,data_list):
        
        return f'{data_list[0]},{data_list[1]}'




class ContactForm(forms.Form): #forms inherits from class object Form
    name = NameField()
    email = forms.EmailField(label='E-Mail')
    category = forms.ChoiceField(choices=[('question','Question'),('other','Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

#constructor of the contact form to allocate memory for the objects
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