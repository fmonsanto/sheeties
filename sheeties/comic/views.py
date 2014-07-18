__author__ = 'francisco'

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from sheeties.comic.models import Comic
from django.template import RequestContext, loader



def index(request):
    comics = Comic.objects.all()
    context = RequestContext(request, {
        'comics':comics,
    })
    return render(request, 'comic/index.html', context)

def detail(request, comic_id):
    comic = get_object_or_404(Comic, id=int(comic_id))
    return render(request, 'comic/detail.html', {'comic':comic})