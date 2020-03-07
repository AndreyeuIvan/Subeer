from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Serial, Season, Episode

def serial_all(request):
	latest_serial_list = Serial.objects.order_by('serial_name')
	context = {'latest_serial_list': latest_serial_list}
	return render(request, 'serial.html', context)
# Create your views here.

def serial_id(request, serial_id):
	serial = get_object_or_404(Serial, pk=serial_id)
	return render(request, 'serial_id.html', {'serial': serial})
