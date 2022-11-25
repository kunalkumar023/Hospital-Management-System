from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signin',views.signin,name="login"),
    path('other',views.other,name="other"),
    path('doc',views.doc,name="doc"),
    path('about',views.about,name="about"),
    path('patient1',views.patient1,name="patient"),
    path('contact',views.contact,name="contact"),
    path('appoint',views.appoint,name="appoint"),
    path('bills',views.bills,name="bills")
]