from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Book
# Create your views here.
def index(request):
    books=Book.objects.all()
    return render(request,"book_outlet/index.html",{
        "books":books
    })

def book_detail(request,slug):
    try:
        book=Book.objects.get(slug=slug)
        return render(request, "book_outlet/book_detail.html",{
            "title":book.title,
            "author":book.author,
            "rating":book.rating,
            "is_bestselling_book":book.is_bestselling_book,
            "slug":slug
        })
    except Exception:
        raise Http404()
    