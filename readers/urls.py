from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page),
    path("book/<int:book_id>/", views.book_page, name = 'book_page')
]