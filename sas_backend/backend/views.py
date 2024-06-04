from rest_framework import generics, pagination
from rest_framework.response import Response
from .models import SentimentAnalysis
from .serializers import SentimentAnalysisSerializer


class SentimentAnalysisPagination(pagination.PageNumberPagination):
    page_size = 10


class SentimentAnalysisList(generics.ListAPIView):
    queryset = SentimentAnalysis.objects.all().order_by('-created_at')
    serializer_class = SentimentAnalysisSerializer
    pagination_class = SentimentAnalysisPagination
