from django.urls import path

import sys

sys.path.append("D:/джанго/newsite/mywiki")
sys.path.append("D:/джанго/newsite/mywiki/templates/mywiki")

import views
app_name = 'mywiki'
urlpatterns = [
    path("",views.index,name="index"),
    path("something",views.something,name="something"),
    path("tagbody",views.tagbody,name="tagbody"),
    path("taghead",views.taghead,name="taghead"),
    path("taghtml",views.taghtml,name="taghtml"),
    path("<str:a>",views.nopage,name="nopage"),
]

