from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'store/home.html', {
        'page_name': 'index'
    })

def store(request):
    books = Book.objects.all()
    book_count = books.count()
    context = {
        'books': books,
        'count': book_count,
        'page_name': 'store',
    }
    return render(request, 'store/store.html', context)

def new_book(request):
    context = {
        'page_name': 'new_book'
    }
    return render(request, 'store/new_book.html')

def new_book(request):
    if request.method == "POST":
        print(request.POST)
        new_book = Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            description=request.POST.get('description'),
            publish_date=request.POST.get('publish_date')
        )
        new_book.save()
        context = {
            'page_name': 'new_book',
            'show_form': False
        }
        return render(request, 'store/new_book.html', context)
    else: # elif request.method == "GET":
        context = {
        'page_heading': 'Create a Book',
        'page_name': 'new_book',
        'show_form': True
    }    
    return render(request, 'store/new_book.html', context)