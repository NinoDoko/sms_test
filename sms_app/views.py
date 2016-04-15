from django.shortcuts import render
from sms_views import *

def index(request):
    return render(request, 'sms_app/index.html', {})
