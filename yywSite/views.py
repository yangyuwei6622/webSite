from django.shortcuts import render,redirect
from django.http import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.template import loader
from yywSite.models import *
import os
from django.conf import settings


def index(requset):
    context = {'title':'hello'}
    bookList = BookInfo.objects.all()
    print(bookList)

    return render(requset,'index.html',context)
def test(request):
    return HttpResponse('test')

def getTest1(request):

    return render(request,'getTest/getTest1.html')
def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1,'b1':b1,'c1':c1}
    return render(request ,'getTest/getTest2.html',context)
def getTest3(request):
    return render(request ,'getTest/getTest3.html')
def postTest1(request):
    return render(request,'getTest/postTest1.html')
def postTest2(request):
    name = request.POST['uname']
    pwd = request.POST['upwd']
    ugender = request.POST['ugender']
    gender = 'gender'

    context = {'name':name,'pwd':pwd,gender:ugender}

    return render(request,'getTest/postTest2.html',context)

def cookieTest(request):
    response = HttpResponse()
    cookie = request.COOKIES
    response.write(cookie['t1'])

    response.set_cookie('t1','abc')

    return response

#重定向
def redirectTest(requset):
    #test 前面的/必须有，如果没有他就在原来的url后面拼接，有的话就在端口后面拼接,简写是redirect
    #response = HttpResponseRedirect('/test/')
    return redirect('/test/')
#session
def session1(requset):
    #get可以赋默认值,如果键不存在可以设置默认值
    myname = requset.session.get('uname','未登录')
    context = {'uname':myname}
    return render(requset,'getTest/session1.html',context)
def session2(requset):

    return render(requset,'getTest/session2.html')
def session2_handle(request):
    name = request.POST['uname']
    request.session['uname'] = name
    #设置session失效时间
    request.session.set_expiry(0)
    return redirect('/test/')
def session3(request):
    #删除session
    del request.session['uname']

    return redirect('/yyw/session1/')
#图片
def image(request):

    return render(request,'getTest/image.html')
#上传图片
def uploadImage(request):

    return render(request,'getTest/uploadImage.html')
def uploadHandle(request):

    file = request.FILES['pic1']
    #构造存储路径
    # path = os.path.join(settings.MEDIA_ROOT, file.name)
    path = os.path.join(settings.MEDIA_ROOT, 'touxiang.jpg')
    with open(path,'wb+') as pic:
        for c in file.chunks():
            pic.write(c)
    return HttpResponse()

