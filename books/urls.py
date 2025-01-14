from django.urls import path

from .views import BookListView, BookDetailView, SearchResultsListView

urlpatterns = [
    path("search/", SearchResultsListView.as_view(), name="search_results"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("", BookListView.as_view(), name="book_list"),
]
