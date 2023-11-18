from django.shortcuts import render
from django.http import HttpResponse
import sys

sys.path.append("D:/джанго/newsite/mywiki/templates/mywiki")
sys.path.append("D:/джанго/newsite/mywiki/static/styles")
sys.path.append("D:/джанго/newsite/mywiki/static")

def index(request):
    return render(request,"mywiki/title.html")

def nopage(request,a):
    return render(request,"mywiki/nopage.html")

def something(request):
    return HttpResponse("<h1>Something</h1>")

def tagbody(request):
    return render(request,"mywiki/tagbody.html",{"name":"Tag Body"})

def taghead(request):
    return render(request,"mywiki/taghead.html",{"name":"Tag Head"})

def taghtml(request):
    return render(request,"mywiki/taghtml.html",{"name":"Tag HTML"})
