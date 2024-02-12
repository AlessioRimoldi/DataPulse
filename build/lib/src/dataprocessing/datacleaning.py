from abc import ABC, abstractmethod

class DataCleaning(ABC):

    @abstractmethod
    def clean(self, X, y=None):
        pass