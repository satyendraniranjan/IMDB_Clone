from django.db import models

# Create your models here.

CATEGORY_CHOICE = (
    ('A','ACTION'),
    ('D','DRAMA'),
    ('C','COMEDY'),
    ('R','ROMANCE'),

)

LANGUAGE_CHOICE = (

    ('EN','ENGLISH'),
    ('GE','GERMAN'),
    ('HI','HINDI'),
    ('FR','FRENCH'),
)

STATUS_CHOICE = (
    ('RA','RECENTLY ADDED'),
    ('MW','MOST WATCHED'),
    ('TR','TOP RATED'),
)

class Movie(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICE,max_length=2)
    status = models.CharField(choices=STATUS_CHOICE,max_length=2)
    year_of_production = models.DateField()
    view_count = models.IntegerField(default=0)


    def __str__(self):
        return self.title



#    -tags

#    -download
#    links
