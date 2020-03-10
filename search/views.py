from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Serial, Season, Episode

def serial_all(request):
	latest_serial_list = Serial.objects.all()[:5]
	context = {'latest_serial_list': latest_serial_list}
	return render(request, 'serial.html', context)


def serial_id(request, serial_id):
	serial = get_object_or_404(Serial, pk=serial_id)
	return render(request, 'serial_id.html', {'serial': serial })


'''Defining Seasons below'''
def season_all(request):
	latest_season_list = Season.objects.order_by('season_name')
	context ={'latest_season_list': latest_season_list}
	return render(request, 'season.html', context)


def season_id(request, season_id):
	season = get_object_or_404(Serial, pk=season_id)
	return render(request, 'season_id.html', {'season': season })

'''Defining Episodes below'''
def episode_all(request):
	latest_episode_list = Episode.objects.order_by('episode_name')
	context = {'latest_episode_list': latest_episode_list}
	return render(request, 'episode.html', context)

def episode_id(request, episode_id):
	episode = get_object_or_404(Episode, pk=episode_id)
	return render(request, 'episode_id.html', {'episode': episode })