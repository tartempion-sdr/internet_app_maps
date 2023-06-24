from django.urls import path
from . import views

app_name = 'internet_app'
urlpatterns = [
    path("", views.index, name="index"),
    path("maps/", views.maps, name="maps"),
    path("modification/", views.modification, name="modification"),

]
