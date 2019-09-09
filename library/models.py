from django.db import models


class Reader(models.Model):
    username = models.CharField(max_length=50)


class Book(models.Model):
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.IntegerField(default=1)
    user_id = models.ForeignKey(Reader, on_delete=models.CASCADE, null = True)
