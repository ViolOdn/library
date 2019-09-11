from django.contrib.auth.models import User, Group
from rest_framework import serializers
from library.models import *


class ReaderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reader
        fields = ['username']


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['book_name', 'author', 'year', 'user_id']