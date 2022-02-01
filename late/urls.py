from django.urls import path

from .import views

urlpatterns = [

    path('home/',views.home,name = 'home'),
    path('snippet',views.snippet_detail),
    path('',views.contact),#view is Contact view

]
    
    
