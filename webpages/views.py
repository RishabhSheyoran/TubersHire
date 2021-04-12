from django.shortcuts import render
from .models import Slider,Team
# Create your views here.
from youtubers1.models import Youtuber

def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders': sliders,
        'teams' : teams,
        'featured_youtubers': featured_youtubers,
        'all_tubers' : all_tubers,

    }
    return render(request, 'webpages/home.html', data)

def about(request):
    return render(request, 'webpages/about.html')    

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')