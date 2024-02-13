from abc import ABC, abstractmethod

class Tab(ABC):

    def __init__(self, title: str, plots: dict):
        self.title = title
        self.plots = {
            'title': '',
            'size': (16,9),
            'position': (0,0),
            'plot': None,
        }
        
    @abstractmethod
    def show(self):
        pass