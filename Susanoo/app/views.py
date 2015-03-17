from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext
from django.views.generic import View
from Susanoo.gmapi.forms.widgets import GoogleMap
from django import forms
from Susanoo import settings

class Home(View):
    def get(self, request):
        t = get_template('home/template.html')
        html = t.render(Context({'my_name': 'Keisuke'}))
        return render_to_response('home/template.html',{'my_name': 'Keisuke'}, context_instance=RequestContext(request))
        
    def post(self, request):
        pass

class Tool(View):
    def get(self, request):
        '''gmap = maps.Map(opts = {
        'center': maps.LatLng(34.687428,133.916473),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 6,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
             },
        })
        marker = maps.Marker(opts = {
                                     'map': gmap,
                                     'position': maps.LatLng(34.687428,133.916473),
                                     })
        maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
        maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
        info = maps.InfoWindow({'content': 'Hello!',
        'disableAutoPan': True
        })
        info.open(gmap, marker)'''
        
        map_key = settings.MAP_KEY
        context = RequestContext(request, {'map_key': map_key})
        return render_to_response('tool/template.html', context)
    
        '''t= get_template('tool/template.html')
        k = models.Weather()
        return HttpResponse(k.response)
        '''
    
class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':900, 'height':600}))
 
 
    def post(self, request):
        pass