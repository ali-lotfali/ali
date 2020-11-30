from django.shortcuts import render , HttpResponse
from  . import models

def articles_list(request ):

    articles = models.Articles.objects.all().order_by('date')

    return render (request ,'articles/articles_list.html' ,{'articles':articles})


def articles_show(request ,id):
    return  HttpResponse(id)
# Create your views here.
