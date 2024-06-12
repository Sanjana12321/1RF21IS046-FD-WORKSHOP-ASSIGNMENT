from django.urls import path
from . import views

urlpatterns = [
    path('factorial/',views.factorial,name='factorial'),
    path('square/',views.square,name='square' ),
    path('index/',views.index,name='index'),
    path('home',views.home,name='home'),
    path('factorials',views.factorials,name='factorials'),
]