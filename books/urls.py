from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.list_books, name='books'),
    path('authors/', views.AuthorList.as_view(), name='authors'),
    url(r'^books/(?P<pk>[-\w]+)/$', views.BookDetail.as_view(), name="book-detail"),
    url(r'^authors/(?P<pk>[-\w]+)/$', views.AuthorDetail.as_view(), name="author-detail"),
    path('add', login_required(views.CreateAuthor.as_view()), name="add"),
    url(r'^review/$', login_required(views.ReviewList.as_view()), name='review-books'),
    #url(r'^review/$', views.review_books, name='review-books'),
    url(r'^review/(?P<pk>[-\w]+)/$', views.review_book, name='review-book'),



]