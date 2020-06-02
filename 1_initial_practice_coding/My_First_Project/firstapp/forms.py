from django import forms

### we dont need to use html to create form
### and each form is a each class
## and the attribute is a input type


## every class is a form
## and every attribue in a class is a
## every attribue is a input field

class user_form(forms.Form):
    
    ## plaecholder is not a argiment providd by django
    ## you need to manually configure it
    ## you need to add widget with form

    ## you can add any attribute with widgtet attribute
    ##  you can add bootstrap and also the css attribute


    first_name = forms.CharField(label = "User First Name",widget = forms.TextInput(attrs={
        "placeholder":"Enter your First name","class":"form-control"
    }))
    last_name  = forms.CharField(label ="User Last Name",widget = forms.TextInput(attrs={
        "placeholder":"Enter your Last Name","class":"form-control"
    }))

    ## adding minimum and maximum length for the instrument
    instrument = forms.CharField(label = "User instrument",max_length=5,min_length=2,widget = forms.TextInput(attrs={
        "placeholder":"Enter the instrument","class":"form-control"
    }))

    ## adding html email validation
    user_email = forms.EmailField(label = "User Email",widget = forms.TextInput(attrs={
        "placeholder":"Enter the email","class":"form-control","type":"email"
    }))

    password = forms.CharField(label = "Password",widget = forms.TextInput(attrs={
        "placeholder":"Enter the password","class":"form-control","type":"password"
    }))


    ## for the ttribute data it will create a calender
    ## now weare add a date of bith colum
    ## and add a calender so eveyone can put the value of data
    ##  adding  adate column in the form

    date_of_birth = forms.DateField(label = "Date Of borth",widget = forms.TextInput(attrs={
        "placeholder":"Enter the instrument","class":"form-control","type":"date"
    }))

    boolean_filed = forms.BooleanField(label = "Currently worked in Band :",required = False,widget=forms.CheckboxInput(attrs={
    }))

    ## adding choice for the band
    ## choices will be dict of tuple
    mychoice = {(1,"Rock"),(2,"Rap"),(3,"folk"),(4,"R&B")}
    band_choice = forms.ChoiceField(widget=forms.Select(attrs={
        "class" :"btn btn-danger"
    }),choices=mychoice)

    gender_choice = {('male','Male'),('Female','Female'),('Other','Other')}

    gender = forms.ChoiceField(widget=forms.RadioSelect,choices=gender_choice)


    ### adding multiple form value
    ### you can select multiple choice
    ## and it will be passed as a list
    other_hobby = {('rap','Rap'),('base_guiter','Base guiter'),('song_writing','Song Writing')}

    hobby = forms.MultipleChoiceField(choices=other_hobby,required=False)



    ### you can use multiple checkbox select
    ## option

    fav_vocal = {("cbenington","CBenington"),("eminem","Eminem"),("Imagine_dragon","Imagine Dragon"),("dua_ipa","Dua Lipa"),("Ann_Marie","Ann Marie")}

    f_vocal = forms.MultipleChoiceField(choices=fav_vocal,widget=forms.CheckboxSelectMultiple)



    
    ## now go to viwes.py and import it





    ## we make another form to test other things

class second_form(forms.Form):

    ## make another form to test it

    ## we make a bolean field
    ## this value will either will be true and faulr
    
    boolean_filed = forms.BooleanField()
    ## this will use to make a checkbox
