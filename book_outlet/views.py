from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Book
from django.db.models import Avg
# Create your views here.
def index(request):
    books=Book.objects.all().order_by("-rating")
    return render(request,"book_outlet/index.html",{
        "books":books,
        "total_number_of_books":len(books),
        "average_rating":Book.objects.aggregate(Avg("rating"))
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
    