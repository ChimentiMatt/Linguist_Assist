from django.urls import path
from .views import BaseView, HomeView, StudyView

app_name = 'spellingapp'
urlpatterns = [
    path('', BaseView, name="base"),
    path('home/', HomeView.as_view(), name="user_home" ),
    path('study/', StudyView.as_view(), name="study_page" )
]