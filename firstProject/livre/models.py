from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Borrowing(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_borrowed = models.DateField()
    book_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} a emprunté {self.book}"
class User(models.Model):
    login = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.login        
