from django.urls import path
from movies import views

urlpatterns = [
    path('', views.index, name='index'),
]
