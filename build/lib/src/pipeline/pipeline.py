from abc import ABC, abstractmethod
from sklearn.pipeline import Pipeline

class Pipeline(ABC):

    @abstractmethod
    def fit_transform(self, X, y=None):
        pass