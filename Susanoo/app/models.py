from django.db import models
from django.template import Template
import sys
import urllib
import json
from Susanoo import settings

# Create your models here.

class Weather(models.Model):
    x=settings.API_KEY