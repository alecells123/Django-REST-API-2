from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 5,
            'title': 'Spiderman: Attack of the Clones',
            'year': 2026
        },
        {
            'id': 6,
            'title': 'Superman: A New Hope',
            'year': 2027
        },
        {
            'id': 7,
            'title': 'Batman: Phantom Menace',
            'year': 2028
        }
    ]
}

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Home page")