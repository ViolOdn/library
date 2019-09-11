from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from library.models import *


def main_page(request):
    return render_to_response('library_home.html', {'readers_list': Reader.objects.all()})


@csrf_exempt
def add_user(request):
    name = request.POST['username']
    Reader(username=name).save()
    return HttpResponseRedirect('/')


def generate_list_of_books(request, query):
    current_reader = Reader.objects.filter(username=query).first()
    books_list = Book.objects.filter(user_id=current_reader)
    return render(request, 'list_of_books.html', {'books': books_list, 'reader': current_reader})


def open_edit_book_form(request, query):
    current_book = Book.objects.filter(id=query).first()
    return render(request, 'edit_book.html', {'book': current_book})


@csrf_exempt
def editing_book(request):
    new_book_name = request.POST['book_name']
    new_book_author = request.POST['author']
    new_book_year = request.POST['year']
    Book.objects.filter(id=request.POST['id']).update(book_name=new_book_name, author=new_book_author, year=new_book_year)
    return HttpResponseRedirect('/')



