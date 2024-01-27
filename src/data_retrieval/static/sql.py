''' This file contains the engine to connect and retrieve data from a database using SQL. '''

''' Imports'''
import os,sys
parent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent)
from types.source import Data
import sqlalchemy as sa
from sqlalchemy.sql import text
from pandas import DataFrame
from data_retrieval.datasource import DataSource

class Sql(DataSource):
    """
    This class is used to retrieve data from a database using SQL.
    """
    
    def __init__(self,dialect = '', db_name = '', user = '', password = '', host = 'localhost', port = 5432 ):
        """
        Constructor for the SqlRetrieval class.
        
        Args:
            dialect (str): The dialect of the database to connect to.
            db_name (str): The name of the database to connect to.
            user (str): The user name to use when connecting to the database.
            password (str): The password to use when connecting to the database.
            host (str): The host name to use when connecting to the database.
            port (int): The port to use when connecting to the database.
        """
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.engine = sa.create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}",echo=True)
    
    def get_data(self, sql):
        """
        Retrieve data from the database using the provided SQL.
        
        :param sql: The SQL to use to retrieve data from the database.
        :return: The data retrieved from the database.
        """
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(sql))
                self.data = Data(f'SQL DB : {self.db_name}',DataFrame(result.fetchall()))
            
            return self.data
        except:
            print("Couldn't retrieve data from the database.")
    
    def display_data(self):
        """Display the data retrieved from the database.
        """
        try:
            print(self.data)
        except:
            print("Couldn't display data.")

    
