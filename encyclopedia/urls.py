from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('create', views.create),
    path('send',views.send),
    path('show',views.show),
    path('edit',views.edit),
    path('editrecord',views.editRecord),
    path('randompage',views.randompage),
    path('aboutDevloper',views.aboutDevloper),
    path('aboutWebapp',views.aboutWebapp),
    path('search',views.search),
]