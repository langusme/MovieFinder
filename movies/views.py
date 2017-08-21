from django.views import generic
from simple_search import search_filter
from django.shortcuts import render
from .models import Movie
import datetime

class IndexView(generic.ListView):
    template_name = 'movies/index.html'
    context_object_name = 'all_movies'

    def get_queryset(self):
        query = self.request.GET.get("q")
        cday = datetime.datetime.now().day
        if query:
            return Movie.objects.all().filter(movie_name__icontains=query)
        else:
            return Movie.objects.all().filter(air_date__day=cday)

class PreviousView(generic.ListView):
    template_name = 'movies/previous.html'
    context_object_name = 'all_movies'

    def get_queryset(self):
        return Movie.objects.all()


class DetailView(generic.DetailView):
    model = Movie
    template_name = 'movies/detail.html'
