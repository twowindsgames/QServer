from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('results', ResultsListView.as_view()),
    path('results/mix', MixResultsListView.as_view()),
    path('detail', ResultsDetailView.as_view()),
]
