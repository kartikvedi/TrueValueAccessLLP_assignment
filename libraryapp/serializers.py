from rest_framework import serializers
from .models import Books, Librarian, Member, Roles, LibRoles, MemberRoles

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ["bookId", "bookName", "bookAuthor", "bookBorrowed", "bookBorrower"]

