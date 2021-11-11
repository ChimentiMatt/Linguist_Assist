from django.urls import path
from .views import BaseView

app_name = 'spellingapp'
urlpatterns = [
    path('', BaseView, name="base")
]