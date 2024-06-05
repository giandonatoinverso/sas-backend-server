from textblob import TextBlob
from .sentiment_analyzer import SentimentAnalyzer


class TextBlobSentimentAnalyzer(SentimentAnalyzer):
    def analyze(self, text):
        analysis = TextBlob(text)
        return {
            'polarity': analysis.sentiment.polarity,
            'subjectivity': analysis.sentiment.subjectivity
        }
