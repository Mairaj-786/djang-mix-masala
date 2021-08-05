from django.shortcuts import render,HttpResponseRedirect
from .models import Book,Reserved_Book,Student
from django.http import HttpResponse
# Create your views here.

def book(request):
    if request.user.is_authenticated:
        bk = Book.objects.all()
        return render(request, "book.html", {"book":bk})
    else:
        return HttpResponseRedirect('login')

def book_detail(request, id=None):
    if request.user.is_authenticated:
        bk = Book.objects.get(id=id)
        if request.method == "POST":
            Student_id = 1
            Book_id = Book.id
            rb = Reserved_Book.objects.create( Book_id=Book_id)
            if rb:
                return HttpResponse('reserve Done')
            else:
                return HttpResponse('reserve fail')
                

        return render(request, "book_detail.html", {"book":bk})
    else:
        return HttpResponseRedirect('login')