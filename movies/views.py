from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movie, Review
from movies.serializers import MovieSerializer, MovieListSerializer, ReviewSerializer
from paginitions import CustomPageNumberPagination


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.order_by('-id')
    serializer_class = MovieListSerializer
    pagination_class = CustomPageNumberPagination


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT', 'PATCH']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class ProductLikedView(APIView):
    def post(self, request, pk):
        try:
            product = Movie.objects.get(id=pk)
            user = request.user
            if not user.is_authenticated:
                return Response({'error': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)

            if user in product.liked.all():
                product.liked.remove(user)
                liked = False
            else:
                product.liked.add(user)
                liked = True

            product.save()

            return Response({'liked': liked}, status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)


class ReviewsView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        movie = get_object_or_404(Movie, pk=kwargs.get('pk'))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
