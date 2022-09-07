from django.db import models

class Books(models.Model):

    class BookStatus(models.TextChoices):
        BORROWED = 'BR',
        AVAILABLE = 'AV'
    
    bookId = models.IntegerField()
    bookName = models.CharField(max_length = 50)
    bookAuthor = models.CharField(max_length = 50)
    bookBorrowed = models.CharField(
        max_length = 2,
        choices = BookStatus.choices,
        default = BookStatus.AVAILABLE
    )
    bookBorrower = models.IntegerField(default = -1)
    
class Librarian(models.Model):
    libId = models.IntegerField()
    libName = models.CharField(max_length = 100)
    libPassword = models.CharField(max_length = 15)

class Member(models.Model):
    memberId = models.IntegerField()
    memberName = models.CharField(max_length = 100)
    memberPassword = models.CharField(max_length = 15)

class Roles(models.Model):
    roleId = models.IntegerField()
    roleName = models.CharField(max_length = 20)

class LibRoles(models.Model):
    libId = models.ForeignKey(Librarian, related_name="libIds", on_delete = models.DO_NOTHING)
    libRole = models.ForeignKey(Roles, related_name="libRoleIds", on_delete = models.DO_NOTHING)

class MemberRoles(models.Model):
    memberId = models.ForeignKey(Member, related_name="memberIds", on_delete = models.DO_NOTHING)
    memberRole = models.ForeignKey(Roles, related_name="MemRoleIds", on_delete = models.DO_NOTHING)
