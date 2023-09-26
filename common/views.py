from rest_framework import generics

from common.models import Category
from common.serializers import CategoryListSerializer
from movies.models import Movie
from movies.serializers import MovieSerializer, MovieListSerializer
from paginitions import CustomPageNumberPagination
from rest_framework.filters import SearchFilter


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryMoviesListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        slug = self.kwargs['slug']
        try:
            category = Category.objects.get(slug=slug)
            movie = Movie.objects.filter(category=category)
            return movie

        except Category.DoesNotExist:
            return Movie.objects.none()


class SearchView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("name", "slug", "category__name")
    pagination_class = CustomPageNumberPagination
