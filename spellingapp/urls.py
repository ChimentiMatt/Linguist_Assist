from django.urls import path
from . import views
from .views import BaseView

app_name = 'spellingapp'
urlpatterns = [
    path('', BaseView, name="home"),
    path('HomeView/', views.HomeView, name="HomeView" ),
    path('study/', views.studyView, name="study_view" ),
    path('remove_key_val/<int:pk>', views.remove_key_val, name='remove_key_val'),
]