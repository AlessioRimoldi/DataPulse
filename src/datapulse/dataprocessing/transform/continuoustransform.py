import os,sys
parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent)

from datatransform import DataTransform

class ContinuousTransform(DataTransform):

    def transform(self, X, y=None):
        '''Function to transform continuous data
        Args:
            X (pandas.DataFrame): dataframe with the data to transform
            y (pandas.Series): series with the target variable
        Returns:
            X (pandas.DataFrame): transformed dataframe
        '''
        # drop duplicates
        X = X.drop_duplicates()
        return X