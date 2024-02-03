from abc import ABC, abstractmethod

class Plot(ABC):
    
    def __init__(self,title = '',size = (16,9)):
        self.title = title
        self.size = size

    def show(self):
        pass
    