from django.shortcuts import get_object_or_404, render, redirect
from .models import Book, Author
from django.views.generic import View, DetailView
from django.db.models import Count
from .forms import ReviewForm
from .forms import BookForm
# Create your views here.


def list_books(request):

    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')

    context = {

        'books': books
    }


    return render(request, 'list.html', context)


class AuthorList(View):

    def get(self, request):

        authors = Author.objects.annotate(published_books=Count('books')).filter(published_books__gt=0)

        context = {

            'authors': authors

        }

        return render(request, 'authors.html', context)


class BookDetail(DetailView):
    model = Book
    template_name = "book.html"


class AuthorDetail(DetailView):
    model = Author
    template_name = "author.html"


def review_books(request):
    """
    List all of the books that we want to review.
    """
    books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')

    context = {
        'books': books,
    }

    return render(request, "list-to-review.html", context)

class ReviewList(View):
    """
    List all of the books that we want to review.
    """
    def get(self, request):

        books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')

        context = {
            'books': books,
            'form': BookForm,
         }

        return render(request, "list-to-review.html", context)

    def post(self, request):
        form = BookForm(request.POST)
        books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')


        if form.is_valid():
            form.save()
            return redirect('review-books')

        context = {
            'form': form,
            'books': books,

        }

        return render(request, "list-to-review.html", context)




def review_book(request, pk):
    """
    Review an individual book
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':

        form = ReviewForm(request.POST)

        if form.is_valid():
            book.is_favourite = form.cleaned_data['is_favourite']
            book.review = form.cleaned_data['review']
            book.save()

            return redirect('review-books')

    else:

        form = ReviewForm

    context = {
        'book': book,
        'form': form,
    }

    return render(request, "review-book.html", context)