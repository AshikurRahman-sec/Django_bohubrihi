from django.shortcuts import render
from django.http import HttpResponse
from .models import Album,Musician
from .forms import user_form

# def index(request):
#     return HttpResponse("Hello world")


## from the home page we go to contact page
def home(request):
    ''' this is coming from first app so you need 
    to add the first app first'''
    ##return HttpResponse("this is home page <a href='/firstapp/contact/'> Contacts <a/>")

    ## we take all the alnum and post it on a table
    musician_list = Musician.objects.order_by('id')


    diction = {'text1':"Tanvir Rahman is called from views.py",'musician_list':musician_list}
    return render(request,'firstapp/index.html',context = diction)

def contact(request):
    ''' you need to put the / before other wise
    it will add it after the curent 
    if you put / beforenthen it will start from the 
    home page'''
    return HttpResponse("this is contact page  <a href='/firstapp/about/'> go to about <a/>")

def about(request):
    return HttpResponse("this is about page <a href='/firstapp/'> go to Home <a/>")



##### display form


### we need atlest two function for the form
### one for rendeering
### and one for getting
### and one url pattern



def get_form_with_html(request):
    return render(request,'firstapp/form.html')
    ## now add url

def form_process_with_html(request):
    return HttpResponse("hello")


def get_form_django_form(request):
    ##  to the same form
    # with django form
    ## we will use django form module
    ## create a file forms.py in the app
    new_form = user_form()
    diction = {'new_form':new_form,"heading_1":"this is Django Form module"}

    return render(request,"firstapp/another_form.html",context=diction)

def form_process_django_form(request):
    ##return HttpResponse("hello")

    ## take the input
    if request.method == "POST":
        ## create a form object
        new_form = user_form(request.POST)
        ## now do the validation
        if new_form.is_valid():
            ## make a dictionary
            data = {}
            ## you have to use the variable name
            ## in the format not the label
            
            data["first_name"] = new_form.cleaned_data['first_name']    
            data["last_name"] = new_form.cleaned_data['last_name']
            data["instrument"] = new_form.cleaned_data['instrument']
            data["user_email"] = new_form.cleaned_data['user_email']
            data["password"] = new_form.cleaned_data['password']
            data["date_of_birth"] = new_form.cleaned_data['date_of_birth']
            data["currently_working"] = new_form.cleaned_data['boolean_filed']
            data["band_choice"] = new_form.cleaned_data['band_choice']
            data["hobby"] = new_form.cleaned_data['hobby']
            data["vocal"] = new_form.cleaned_data['f_vocal']

            ## add another key value pair
            data["form_submitted"] = True
            ## this key value pair will be used to evaluate the form
            ## if this key does not generated  that means the form
            ## is not submitted yet
            print(data)
            ## now we need to render this in another url
    return render(request,"firstapp/result.html",context=data)
        
        


        
