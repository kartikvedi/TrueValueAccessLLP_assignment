from django.urls import path, include
from .views import (
    BooksApiView,
    BooksApiEditView
)

urlpatterns = [
    path('', BooksApiView.as_view()),
    path('<int:bookId>', BooksApiEditView.as_view())
]
