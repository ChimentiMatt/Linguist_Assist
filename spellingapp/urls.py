from django.urls import path
from . import views


app_name = 'spellingapp'
urlpatterns = [
    path('', views.BaseView, name="home"),
    path('HomeView/', views.HomeView, name="HomeView" ),
    path('study/', views.study_view, name="study_view" ),
    path('learning/', views.learning_view, name="learning_view"),
    path('remove_key_val/<int:pk>/', views.remove_key_val, name='remove_key_val'),
    path('add_key_val/', views.add_key_val, name='add_key_val'),
    path('learning_add_key_val/', views.learning_add_key_val, name='learning_add_key_val'),

    path('fetch_get', views.fetch_get, name='fetch_get'),
    

]