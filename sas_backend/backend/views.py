from rest_framework import generics, pagination, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SentimentAnalysis
from .serializers import SentimentAnalysisSerializer
from sentiment_analyzer.textblob_sentiment_analyzer import TextBlobSentimentAnalyzer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class SentimentAnalysisPagination(pagination.PageNumberPagination):
    page_size = 10


class SentimentAnalysisList(generics.ListAPIView):
    queryset = SentimentAnalysis.objects.all().order_by('-created_at')
    serializer_class = SentimentAnalysisSerializer
    pagination_class = SentimentAnalysisPagination

    @swagger_auto_schema(
        operation_description="Retrieve a list of sentiment analysis",
        responses={200: SentimentAnalysisSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class SentimentAnalysisCreate(APIView):
    @swagger_auto_schema(
        operation_description="Create a new sentiment analysis",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['text'],
            properties={
                'text': openapi.Schema(type=openapi.TYPE_STRING, description='Text to analyze'),
            },
        ),
        responses={201: SentimentAnalysisSerializer, 400: 'Bad Request'}
    )
    def post(self, request, format=None):
        text = request.data.get('text')

        if not text:
            return Response({'error': '"text" field is mandatory.'}, status=status.HTTP_400_BAD_REQUEST)

        analyzer = TextBlobSentimentAnalyzer()
        sentiment_data = analyzer.analyze(text)

        sentiment_analysis = SentimentAnalysis(text_content=text, **sentiment_data)
        sentiment_analysis.save()

        serializer = SentimentAnalysisSerializer(sentiment_analysis)
        return Response(serializer.data, status=status.HTTP_201_CREATED)