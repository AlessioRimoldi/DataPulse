from abc import ABC, abstractmethod

class DataTransform(ABC):
    
    @abstractmethod
    def transform(self, X, y=None):
        pass
