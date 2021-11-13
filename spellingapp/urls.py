from django.urls import path
from . import views
from .views import BaseView, HomeView, StudyView

app_name = 'spellingapp'
urlpatterns = [
    path('', BaseView, name="home"),
    path('HomeView/', views.HomeView, name="HomeView" ),
    path('study/', StudyView.as_view(), name="study_page" )
]