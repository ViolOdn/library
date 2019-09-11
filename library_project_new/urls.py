from django.urls import include, path
from library.views import *
from django.contrib import admin

urlpatterns = [
    path('', main_page),
    path('successful_register', add_user),
    path('list_of_books/<query>', generate_list_of_books, name='generate_list_of_books'),
    path('edit_book/<query>', open_edit_book_form, name='open_edit_book_form'),
    path('successful_editing', editing_book)
]