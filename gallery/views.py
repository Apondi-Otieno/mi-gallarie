from django.shortcuts import render
from .models import Category, Picture
from django.http import HttpResponse,Http404

# Create your views here.



def home(request):
    pictures=Picture.objects.all()   
    return render(request, 'index.html',{'pictures':pictures})



def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        category = request.GET.get("category")
        searched_articles = Picture.search_by_category( category)
        message = f"{ category}"

        return render(request, 'search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})