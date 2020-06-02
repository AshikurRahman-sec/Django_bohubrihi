from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns  = [

     path('',views.home,name='home'),
     path('contact/',views.contact,name='contact'),
     path('about/',views.about,name='about'),
     path('get_form_with_html/',views.get_form_with_html,name='get_form_with_html'),
     path('form_process_with_html/',views.form_process_with_html,name='form_process_with_html'),
     path('get_form_django_form/',views.get_form_django_form,name='get_form_django_form'),
     path('form_process_django_form/',views.form_process_django_form,name='form_process_django_form'),
    
]