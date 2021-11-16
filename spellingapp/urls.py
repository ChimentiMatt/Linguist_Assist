from django.urls import path
from . import views
from .views import BaseView

app_name = 'spellingapp'
urlpatterns = [
    path('', BaseView, name="home"),
    path('HomeView/', views.HomeView, name="HomeView" ),
    path('study/', views.study_view, name="study_view" ),
    path('learning/', views.learning_view, name="learning_view"),
    path('remove_key_val/<int:pk>/', views.remove_key_val, name='remove_key_val'),
    path('add_key_val/', views.add_key_val, name='add_key_val')
]