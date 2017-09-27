import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import HttpRequest

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())

def getip(request):
    ip = request.META['REMOTE_ADDR']
    return render(request, 'welcome/getip.html', {
        'ip': ip
    })
