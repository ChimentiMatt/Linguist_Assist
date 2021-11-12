from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spellingapp.urls')),
    
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]

