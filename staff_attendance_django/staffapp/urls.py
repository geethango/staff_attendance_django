from django.urls import path
from . import views

urlpatterns = [
    #path('', views.staffapp,name='staffapp'),
    #path('staffapp', views.firebase_data, name='firebase_data'),
    path('home/', views.firebase_data, name='firebase_data'),
]