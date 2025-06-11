from django.urls import path
from . import views

urlpatterns = [
    path('indexi/<str:room_name>/', views.index),
    path('login/', views.login),
    path('signup/', views.signup),


    
]


