from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
# Create your views here.

def home(request):
    searchTerm = request.GET.get("searchMovie")

     
    movies = Movie.objects.all()
    filteredMovies = movies

    if searchTerm:
        filteredMovies = Movie.objects.filter(title__icontains=searchTerm)
        

    return render(request, 'home.html', {"allMovies":movies, "searchTerm":searchTerm,'filteredMovies':filteredMovies})

def about(request):
    return render(request, 'about.html')

