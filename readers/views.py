from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from readers.models import Books
import json

# Create your views here.

def home_page(request):
    template = loader.get_template('home.html')
    book_objs = Books.objects.order_by('id').all()
    total_objs = book_objs.count()
    context = {
    'Books': book_objs,
    'Midpoint': total_objs/2,}
    return HttpResponse(template.render(context, request))

def book_page(request, book_id):
    template = loader.get_template('book.html')
    book_obj = get_object_or_404(Books, id = book_id)
    json_data = json.dumps(book_obj.audiofiles)
    context = {
        'Book' : book_obj,
        'json_data': json_data,}
    return HttpResponse(template.render(context, request))
