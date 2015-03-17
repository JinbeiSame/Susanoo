from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext
from django.views.generic import View
from Susanoo.app import models

class Home(View):
    def get(self, request):
        t = get_template('home/template.html')
        html = t.render(Context({'my_name': 'Keisuke'}))
        return render_to_response('home/template.html',{'my_name': 'Keisuke'}, context_instance=RequestContext(request))
        
    def post(self, request):
        pass

class Tool(View):
    def get(self, request):
        t = get_template('tool/template.html')
        k = models.Weather()
        return HttpResponse(k.x)

    def post(self, request):
        pass