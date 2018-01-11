"""
django2_getting_started URL Configuration
"""

from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('flix/', include('flix.urls')),
    path('admin/', admin.site.urls),
]
