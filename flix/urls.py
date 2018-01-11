from django.urls import path

from .views.home_page import home_page

urlpatterns = [
    path('', home_page, name='home_page'),
]