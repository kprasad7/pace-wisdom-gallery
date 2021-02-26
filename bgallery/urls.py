from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index,name="homee"),
    path('u', views.Indexu,name="u"),
    path("a" , views.Viewimagea,name="a"),
    path("b" , views.Viewimageb,name="b"),
    path("c" , views.Viewimagec,name="c"),
    path("g" , views.Notfilter, name="g")

   
]