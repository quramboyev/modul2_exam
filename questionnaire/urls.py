from django.urls import path
from .views import questionnaire_view, contest_view

urlpatterns = [
    path('anketa/', questionnaire_view, name='anketa'), #contest/anketa
    path('', contest_view, name='contest')
]
