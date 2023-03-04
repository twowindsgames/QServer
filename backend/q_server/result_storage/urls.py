from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('results', ResultsListView.as_view()),
]
