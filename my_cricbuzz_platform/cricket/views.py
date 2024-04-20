from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def base_view(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def news_detail(request, pk):
    
    news_article = get_object_or_404(News, pk=pk)
    
    context = {
        'news_article': news_article,
        
    }
    return render(request, 'news_detail.html', context)

def profile_view(request):
    
    profile = User.objects.get(user=request.user)

    # Pass the profile data to the template
    context = {
         'profile': profile
    }
    return render(request, 'profile.html', context)

def series_list(request):
    series_list = series_list.objects.all()
    context = {
        'series_list': series_list
    }
    return render(request, 'series_list.html', context)

def news_list(request):
    news_list = News.objects.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'news_list.html', context)

def all_players(request):
    
    players = Player.objects.all()
    
    context = {
        'players': players,
        
    }
    return render(request, 'base.html', context)

def all_matches(request):
    
    matches = Match.objects.all()
    
    context = {
        
        'matches': matches
    }
    return render(request, 'base.html', context)