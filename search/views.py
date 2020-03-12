from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Serial, Season, Episode

def serial_all(request):
	serials = Serial.objects.all()
	return render(request, 'serial.html', {'serials':serials})

def season(request, serial_id):
	seasons = Season.objects.filter(serial=serial_id)
	return render(request, 'season.html', {'seasons':seasons})

def episode(request, season_id):
	episodes = Episode.objects.filter(season= season_id)
	return render(request, 'episode.html', {'episodes':episodes})
	