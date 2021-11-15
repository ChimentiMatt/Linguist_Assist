from django.urls import path
from . import views
from .views import BaseView, HomeView, StudyView, DeleteKeyVal

app_name = 'spellingapp'
urlpatterns = [
    path('', BaseView, name="home"),
    path('HomeView/', views.HomeView, name="HomeView" ),
    path('study/', StudyView.as_view(), name="study_page" ),
    path('study/<int:pk>', DeleteKeyVal.as_view(), name="delte_view")
]