import os,sys
import unittest,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.tasks.estimate import Estimate
from src.tasks.tlsTask import TLS
from src.tasks.dsl import DSL
from src.tasks.parameterstudy import ParameterStudy
from src.tasks.routing import Routing
unittest.TestLoader.sortTestMethodsUsing = None

class TestEstimate(unittest.TestCase):

    def setUp(self) -> None:
        with open('./dep/sumo_files/grid8by8/simparams/test.json','r') as file:
            self.taskparams = json.load(file)

    def test_run(self):
        if self.taskparams['taskname'] == 'estimate':
            self.task = Estimate(self.taskparams)
            self.assertIsInstance(self.task,Estimate)
            print('Creation Test Passed')
        elif self.taskparams['taskname'] == 'tls':
            self.task = TLS(self.taskparams)
            self.assertIsInstance(self.task,TLS)
            print('Creation Test Passed')
        elif self.taskparams['taskname'] == 'dsl':
            self.task = DSL(self.taskparams)
            self.assertIsInstance(self.task,DSL)
            print('Creation Test Passed')
        elif self.taskparams['taskname'] == 'routing':
            self.task = Routing(self.taskparams)
            self.assertIsInstance(self.task,Routing)
            print('Creation Test Passed')
        elif self.taskparams['taskname'] == 'parameterstudy':
            self.task = ParameterStudy(self.taskparams)
            self.assertIsInstance(self.task,ParameterStudy)
            print('Creation Test Passed')
        else:
            raise ValueError('Taskname not recognized')
        
        self.task.runtask()
        print('Task runned successfully')


if __name__ == '__main__':
    unittest.main()