from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import permissions
from .models import Books, Librarian, Member, LibRoles, MemberRoles
from django.db.models import Max
from .serializers import BookSerializer

class BooksApiView(APIView):

    #permission_classes = [permissions.IsAuthenticated]

    #List all books
    def get_desc_order_books(self):
        return Books.objects.all().order_by('-bookId')
    
    #1.	http://127.0.0.1:8000/books/showBooks	:   Show all books
    def get(self, request):
        books = Books.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    #2.	http://127.0.0.1:8000/books/add		:   Add book
    def post(self, request, *args, **kwargs):
        bookMaxId = int(self.get_desc_order_books().only('bookId').aggregate(Max('bookId'))[0])
        data = {
            'bookId': bookMaxId + 1,
            'bookName': request.data.get('bookName'),
            'bookAuthor': request.data.get('bookAuthor')
        }
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BooksApiEditView(APIView):

    def get_object(self, bookId, *args, **kwargs):
        try:
            return Books.objects.get(bookId = bookId)
        except Books.DoesNotExist:
            return None

    def get(self, request, bookId, *args, **kwargs):
        book = self.get_object(bookId)
        if not book:
            return Response(
                {"res": "Book does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, bookId, *args, **kwargs):
        book = self.get_object(bookId)
        if not book:
            return Response(
                {"res": "Book does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        book.delete()
        return Response(
            {"res": "Book removed!"},
            status=status.HTTP_200_OK
        )

    def put(self, request, bookId, *args, **kwargs):
        book = self.get_object(bookId)
        if not book:
            return Response(
                {"res": "Book does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'bookId': request.data.get('bookId'), 
            'bookName': request.data.get('bookName'), 
            'bookAuthor': request.data.get('bookAuthor')
        }
        serializer = TodoSerializer(instance = book, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
