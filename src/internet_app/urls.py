from django.urls import path, include
from . import views

app_name = 'internet_app'
urlpatterns = [
    path("", views.index, name="index"),
    path("compte/", include("compte.urls")),
    path("maps/", views.maps, name="maps"),
    path("modification/", views.modification, name="modification"),

]
