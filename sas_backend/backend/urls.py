from django.urls import path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from backend.views import SentimentAnalysisList, SentimentAnalysisCreate

from backend.views import SentimentAnalysisList, SentimentAnalysisCreate

schema_view = get_schema_view(
    openapi.Info(
        title="Sentiment Analysis API",
        default_version='v1',
        description="Sentiment Analysis API",
        terms_of_service="https://www.example.com",
        contact=openapi.Contact(email="example@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True
)

urlpatterns = [
    path('sentiment-analysis/', SentimentAnalysisList.as_view(), name='sentiment_analysis_list'),
    path('sentiment-analysis/create/', SentimentAnalysisCreate.as_view(), name='sentiment_analysis_create'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]