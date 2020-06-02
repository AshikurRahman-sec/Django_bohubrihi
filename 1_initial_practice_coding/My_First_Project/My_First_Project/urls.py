from django.contrib import admin
from django.urls import path
## import all the views from the firstapp
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    ## setting up the app based path
    path('firstapp/',include('firstapp.urls')),
    # ## it take three pattern 
    # ## url view and name


]
