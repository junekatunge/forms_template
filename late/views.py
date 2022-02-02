from http.client import HTTPResponse
from django.shortcuts import render
#from django.http import HttpResponse #for the view
from .forms import ContactForm, SnippetForm
# Create your views here.

def home(request): 
    return render(request, 'home.html',{'name':"june"})# render used for templates

def contact(request):

    if request.method == 'POST':
        
        form = ContactForm(request.POST)#user details are inputed in the form
        if form.is_valid():# to check if the form is valid to the user

          name = form.cleaned_data['name']
          email = form.cleaned_data['email']

          print(name)
    else:
        form = ContactForm()
    return render(request,'form.html',{'form':form})#pass a form

def snippet_detail(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)#user details are inputed in the form
        if form.is_valid():# to check if the form is valid to the user
                form.save()

    form = SnippetForm()
    return render(request,'form.html',{'form':form})#pass a form