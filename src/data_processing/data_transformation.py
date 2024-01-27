import os,sys
parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))   
sys.path.append(parent)
from types.source import Data

def mean(Data = Data,column = 'all'):
    ''' Calculate the mean of the data. '''
    return Data

def ma(Data = Data, window = 3):
    ''' Calculate the moving average of the data. '''
    return Data
