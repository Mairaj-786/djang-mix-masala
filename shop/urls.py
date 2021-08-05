from django.urls import path
from .views import book,book_detail

urlpatterns =[
    path('book', book, name="book"),
    path('book_detail/<int:id>', book_detail, name="book_detail"),
]