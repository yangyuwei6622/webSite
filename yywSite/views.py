from django.shortcuts import render
from django.http import *
from django.template import RequestContext
from django.template import loader
from yywSite.models import *


def index(requset):
    context = {'title':'hello'}
    bookList = BookInfo.objects.all()
    print(bookList)

    return render(requset,'index.html',context)
def test(request):
    return HttpResponse('test')