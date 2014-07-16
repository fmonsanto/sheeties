__author__ = 'francisco'

from django.http import HttpResponse

def homepage(request):
    return HttpResponse('Welcome to the Sheeties Website!')