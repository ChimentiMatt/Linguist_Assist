from django.urls import path
from . import views

app_name = 'spellingapp'
urlpatterns = [
    path('myview/', views.myview, name='myview')
]