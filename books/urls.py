from django.urls import path

from .views import BookListView, BookDetailView

urlpatterns = [
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("", BookListView.as_view(), name="book_list"),
]