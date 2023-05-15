from django.urls import path
from . import views

urlpatterns=[
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('e_list', views.e_list, name='e_list'),
    path('', views.index, name='index')
]