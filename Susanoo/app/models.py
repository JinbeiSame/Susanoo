from django.db import models
from django.template import Template
import sys
import urllib2
import json
from Susanoo import settings

# Create your models here.

class Weather(models.Model):
    token = "http://api.openweathermap.org/data/2.5/forecast/city?id="
    cityid= "524901"
    token = token + cityid + "&APPID="
    weather_key=settings.WEATHER_KEY
    token = token +  weather_key
    response = urllib2.urlopen(token)
    
    
