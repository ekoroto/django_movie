from django.views.generic import DetailView, ListView

from .models import Movie


class MovieView(ListView):
    """List of all movies"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Full description of the movie"""

    model = Movie
    slug_field = 'url'
