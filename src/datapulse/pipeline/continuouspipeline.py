from pipeline import Pipeline

class ContinuousPipeline(Pipeline):

    def __init__(self):
        self.pastdata = None
        
    def fit_transform(self, X, y=None):
        return super().fit_transform(X, y)