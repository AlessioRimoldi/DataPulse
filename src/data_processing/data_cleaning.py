import os,sys
parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent)
from types.source import Data

def removenan(Data = Data):
    ''' Remove NaN values from the data. '''
    return Data

def impute(Data = Data):
    ''' Impute NaN values from the data. '''
    return Data
