from django.urls import path

from . import views


urlpatterns = [

    path('', views.list_books, name='books'),
    path('authors/', views.AuthorList.as_view(), name='authors')



]