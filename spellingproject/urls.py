from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('spellingapp.urls')),
    path('admin/', admin.site.urls),

]