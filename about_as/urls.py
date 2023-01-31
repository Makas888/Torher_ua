from django.urls import path
from .views import about_as_view

app_name = 'about_as'

urlpatterns = [
    path('', about_as_view, name='about_as'),
]
