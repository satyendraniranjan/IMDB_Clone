from django.db import models
from django.utils.text import slugify
# Create your models here.

CATEGORY_CHOICE = (
    ('action','ACTION'),
    ('drama','DRAMA'),
    ('comedy','COMEDY'),
    ('romance','ROMANCE'),

)

LANGUAGE_CHOICE = (

    ('english','ENGLISH'),
    ('german','GERMAN'),
    ('hindi','HINDI'),
    ('french','FRENCH'),
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
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICE,max_length=10)
    status = models.CharField(choices=STATUS_CHOICE,max_length=2)
    cast = models.CharField(max_length=100)
    year_of_production = models.DateField()
    view_count = models.IntegerField(default=0)
    movie_trailer = models.URLField()

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

LINK_CHOICES = (

    ('D','Download Link'),
    ('W','Watch Link'),

)

class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_watch_link')
    type = models.CharField(max_length=1, choices=LINK_CHOICES)
    link = models.URLField()

    def __str__(self):
        return (self.movie | self.type)
