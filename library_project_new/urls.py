from django.urls import include, path
from library.views import *
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from library import views

router = routers.DefaultRouter()
router.register(r'readers', views.ReaderViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', main_page),
    path('successful_register', add_user),
    path('list_of_books/<query>', generate_list_of_books, name='generate_list_of_books'),
    path('edit_book/<query>', open_edit_book_form, name='open_edit_book_form'),
    path('successful_editing', editing_book),
    path('successful_adding_book', add_book),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

