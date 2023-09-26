from django.urls import path

from common.views import CategoryView, CategoryMoviesListView, SearchView

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category-list'),
    path('category/<str:slug>/', CategoryMoviesListView.as_view(), name='category-movies-list'),
    path('search/', SearchView.as_view(), name='search'),
]