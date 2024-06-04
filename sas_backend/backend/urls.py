from django.urls import path
from backend.views import SentimentAnalysisList

urlpatterns = [
    path('sentiment-analysis/', SentimentAnalysisList.as_view(), name='sentiment_analysis_list'),
]