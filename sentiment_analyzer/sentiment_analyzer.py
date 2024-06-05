# To increase reuse, this should be a dependency, with its own repo etc to be placed in requirements.txt
from abc import ABC, abstractmethod


class SentimentAnalyzer(ABC):
    @abstractmethod
    def analyze(self, text):
        pass
