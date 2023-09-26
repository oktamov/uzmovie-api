from django.urls import path

from movies.views import MovieListView, MovieDetailView, ProductLikedView, ReviewsView

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('<str:slug>/', MovieDetailView.as_view(), name='movie-slug'),
    path('<int:pk>/like', ProductLikedView.as_view(), name='product-like-unlike'),
    path('movies/<int:pk>/reviews-create/', ReviewsView.as_view(), name='reviews-create'),
]

