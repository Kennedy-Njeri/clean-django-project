from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [

    path('', views.list_books, name='books'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    url(r'^books/(?P<pk>[-\w]+)/$', views.BookDetail.as_view(), name="book-detail"),
    url(r'^authors/(?P<pk>[-\w]+)/$', views.AuthorDetail.as_view(), name="author-detail"),
    path('add', views.CreateAuthor.as_view(), name="add"),
    url(r'^review/$', views.ReviewList.as_view(), name='review-books'),
    #url(r'^review/$', views.review_books, name='review-books'),
    url(r'^review/(?P<pk>[-\w]+)/$', views.review_book, name='review-book'),



]