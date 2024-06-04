from django.db import models


class SentimentAnalysis(models.Model):
    class Meta:
        app_label = 'backend'
        db_table = 'sentiment_analysis_results'
    text_content = models.TextField()
    polarity = models.DecimalField(max_digits=5, decimal_places=2)
    subjectivity = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sentiment Analysis for '{self.text_content}...'"
