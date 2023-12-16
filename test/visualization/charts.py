'''Test script for bar_chart visualization'''
import os, sys
parent = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent)
from src.visualization.bar_chart import bar_chart
from src.visualization.scatter_plot import scatter_plot
from src.visualization.line_chart import line_chart
from src.visualization.pie_chart import pie_chart
from src.visualization.calendar import calendar_heatmap
import unittest
from pandas import DataFrame, date_range
import random
import datetime


class TestVis(unittest.TestCase):
    ''' Test class for visualization '''
    @classmethod
    def setUpClass(self):
        ''' Set up class for TestBarChart '''
        #General
        self.style = 'darkgrid'
        self.data = DataFrame({'x': [i + random.random() for i in range(100)],
                               'y': [i + random.random() for i in range(100)],
                               'z': [i + random.random() for i in reversed(range(100))]})
        self.x = 'x'
        self.y = 'y'
        self.title = 'My wowo graph'
        self.xlabel = 'x axis'
        self.ylabel = 'y axis'
        self.color = 'green'
        self.figsize = (16,9)
        
        # bar chart
        self.counts =DataFrame({'counts' : [random.randint(0,10) for _ in range(10)],
                      'category' : [f'{i}' for i in range(10)]})
        self.sorted = True
        # Pie chart
        self.labels = [random.randint(0,5) for _ in range(len(self.data['x']))]
        self.radius = 0.3
        self.shadow = True
        # Calendar
        dates = date_range('20230101',periods=365)
        data = [random.randint(0,5) for _ in range(len(dates))]
        self.caledar_data = DataFrame({'data':data},index=dates)
  
    def test_bar_chart(self):
        ''' Test bar_chart method '''
        bar_chart(self.counts,title = self.title, xlabel = self.xlabel, ylabel = self.ylabel, figsize = self.figsize, sorted = self.sorted)
    
    def test_scatter_plot(self):
        ''' Test scatter_plot method '''
        scatter_plot(self.data, self.x, self.y, self.title, self.xlabel, self.ylabel, self.color, self.figsize,self.style)
    
    def test_line_plot(self):
        ''' Test line plot visualization'''
        line_chart(data= self.data, title = self.title, xlabel=self.xlabel, ylabel= self.ylabel, figsize=self.figsize,
                   line_colors = ['green','red'], line_widths = [2,2])
    
    def test_pie_chart(self):
        '''Test pie_chart visualization'''
        pie_chart(data=self.counts,title = self.title,figsize=self.figsize,radius = self.radius)
    
    # def test_calendar(self):
    #     '''Test calendar_headmap visualization'''
    #     calendar_heatmap(self.caledar_data, year = 2023, figsize=self.figsize, title=self.title)
        
    
        
if __name__ == '__main__':
    unittest.main()
    