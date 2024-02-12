''' Test script for Sqlretrieval class '''
import os, sys
current = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
parent = os.path.dirname(current)
sys.path.append(parent)
import unittest
from src.datasource.static.sql import Sql


class TestSqlRetrieval(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.dialect = 'postgresql'
        self.db_name = 'olist'
        self.user = 'postgres'
        self.password = 'test_pass'
        self.host = 'localhost'
        self.port = 5432

        self.SqlRetrieval = Sql(self.dialect, self.db_name, self.user, self.password, self.host, self.port)    
        
    def test_get_data(self):
        sql = "select * from customers limit 100;"
        data = self.SqlRetrieval.get_data(sql)
        print(data)

if __name__ == '__main__':
    unittest.main()