from django.db import models
from django.contrib import admin


# Create your models here.
class Serial(models.Model):
	serial_name = models.TextField()

	class Meta():
		verbose_name_plural = 'serial'
		
	def __str__(self):
		return self.serial_name 

class Season(models.Model):
	season_name = models.TextField()
	serial = models.ForeignKey(Serial, on_delete=models.CASCADE, blank=False)

	def __str__(self):
		return self.season_name
		
class Episode(models.Model):
	
	episode_name = models.TextField()
	season = models.ForeignKey(Season, on_delete=models.CASCADE, blank=False)

	def __str__(self):
		return self.episode_name		


admin.site.register(Serial)
admin.site.register(Season)
admin.site.register(Episode)
