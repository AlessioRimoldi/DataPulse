from pipeline import Pipeline

class StaticPipeline(Pipeline):

    def fit_transform(self, X, y=None):
        return super().fit_transform(X, y)