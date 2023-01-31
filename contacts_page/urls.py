from django.urls import path
from .views import contacts_page_view

app_name = 'contacts_page'

urlpatterns = [
    path('', contacts_page_view, name='contacts_page'),
]
