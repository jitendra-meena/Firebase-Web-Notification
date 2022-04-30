from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('' , index),
    path('send/' , send),
    path('firebase-messaging-sw.js',showFirebaseJS,name="show_firebase_js"),
]