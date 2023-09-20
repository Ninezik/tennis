from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.utils import timezone

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def get_session_id(request):
    session_id = request.session.session_key
    current_url = request.build_absolute_uri()
    current_timestamp = timezone.now()
    return render(request, 'dapat_session.html', {'session_id': session_id, 'current_url': current_url, 'current_timestamp':current_timestamp})