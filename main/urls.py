from django.urls import path, include
from .views import main_list_view

urlpatterns = [
    path('', main_list_view, name='main')
]
