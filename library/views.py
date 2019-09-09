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
    s = books_list
    final_list = []
    for book in books_list:
        final_list.append(book.book_name)
    return render(request, 'list_of_books.html', {'books': final_list})

