from django.shortcuts import render
from .models import Serial, Season, Episode
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponseNotAllowed, HttpResponse
from .forms import NameForm
from django.views.generic import ListView
from django.core.paginator import Paginator


def serial(request):
    query = request.GET.get('q')
    
    if query:
        serials = Serial.objects.filter(
            Q(serial_name__icontains=query)
            )
    else:
        serials = Serial.objects.all()
    paginator = Paginator(serials, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'serial.html', {'serials':serials, 'page_obj':page_obj})

def season(request, serial_id):
    query = request.GET.get('q')

    if query:
        seasons = Season.objects.filter(
            Q(season_name__icontains=query), serial=serial_id
            )
    else:
        seasons = Season.objects.filter(serial=serial_id)
    return render(request, 'season.html', {'seasons':seasons, 'serial_id':serial_id})

def episode(request, season_id):
    query = request.GET.get('q')

    if query:
        episodes = Episode.objects.filter(
            Q(episode_name__icontains=query), season_id=season_id
            )
    else:
        episodes = Episode.objects.filter(season= season_id)
    return render(request, 'episode.html', {'episodes':episodes, 'season_id':season_id})

def get_name(request):
    if request.method == 'GET':
        form = NameForm()
        return render(request, 'form.html', {'form': form})
    elif request.method == 'POST':
        form = NameForm(request.POST)
        feedback = form.save()
        feedback.save()
        return render(request, 'form.html', {'form': NameForm()} )
    else:
        return HttpResponseNotAllowed()