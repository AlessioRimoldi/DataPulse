import os,sys
parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent)

from datacleaning import DataCleaning

class ContinuousCleaning(DataCleaning):
    '''Class to clean continuous data'''

    def clean(self, X, y=None):
        '''Function to clean continuous data
        Args:
            X (pandas.DataFrame): dataframe with the data to clean
            y (pandas.Series): series with the target variable
        Returns:
            X (pandas.DataFrame): cleaned dataframe
        '''
        # drop duplicates
        X = X.drop_duplicates()
        return X