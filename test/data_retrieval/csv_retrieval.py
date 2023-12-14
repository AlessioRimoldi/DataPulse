''' Test script for Csvretrieval class '''

import os, sys
parent = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent)
import unittest
from src.data_retrieval.csv_retrieval import CsvRetrieval
from pandas import read_csv,read_excel

class TestCsvRetrieval(unittest.TestCase):
    ''' Test class for Csvretrieval class '''
    @classmethod
    def setUpClass(self):
        ''' Set up class for TestCsvRetrieval '''
        self.path = 'put your path here'
        self.CsvRetrieval = CsvRetrieval(self.path)
        self.extension = self.path.split('/')[-1].split('.')[-1]
        self.data = read_csv(self.path) if self.extension == 'csv' else read_excel(self.path)
    
    def test_get_data(self):
        ''' Test get_data method '''
        self.assertEqual(self.CsvRetrieval.get_data().equals(self.data),True)