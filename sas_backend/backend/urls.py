from django.urls import path
from backend.views import SentimentAnalysisList, SentimentAnalysisCreate

urlpatterns = [
    path('sentiment-analysis/', SentimentAnalysisList.as_view(), name='sentiment_analysis_list'),
    path('sentiment-analysis/create/', SentimentAnalysisCreate.as_view(), name='sentiment_analysis_create'),
]