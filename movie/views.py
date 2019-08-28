from django.shortcuts import render
from .models import Movie, MovieLinks
from django.views.generic import ListView, DetailView
# Create your views here.

class MovieList(ListView):
    model = Movie
    paginate_by = 1


class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        object.view_count+=1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        return context
