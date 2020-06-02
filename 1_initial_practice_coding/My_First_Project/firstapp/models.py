from django.db import models

# Create your models here.

class Musician(models.Model):
    ##id = models.AutoField(Primary_key=True)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length=150)
    instrument = models.CharField(max_length=150)

    def __str__(self):
        return self.first_name + " " + self.last_name



class Album(models.Model):
    ## django can autometically create
    ## primary key
    ## even you dont mention 
    ##id = models.AutoField(Primary_key=True)
    artist = models.ForeignKey(Musician,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    release_date = models.DateField()
    ## adding fixed rating with the num_starts
    rating = (
        (1,"Very Bad"),
        (2,"Bad"),
        (3,"Good"),
        (4,"Very Good"),
        (5,"Excelent!!!"),
    )

    num_starts = models.IntegerField(choices=rating)

    def __str__(self):
        return "{} Album Name: {} ".format(self.artist,self.name)