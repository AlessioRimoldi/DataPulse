'''Script to produce bar chart visualizations'''

from bokeh.plotting import figure,show
from bokeh.palettes import Category20
from bokeh.models import ColumnDataSource
import matplotlib.pyplot as plt
from numpy import arange

    
def bar_chart(data, title = '', xlabel = '', ylabel = '', figsize = (16,9), sorted = False):
    '''Function to produce bar chart visualizations
    at the moment colors are supported up to 20 categories
    Args:
        data (dict): dictionary with the data to plot keys = ['counts','categories']
        title (str): title of the plot
        xlabel (str): label of the x axis
        ylabel (str): label of the y axis
        figsize (tuple): size of the figure
        sorted (bool): if True, the data will be sorted in descending order
    '''
    ncat = len(data['categories'])
    M = max(data['counts'])
    source = ColumnDataSource(data= dict(categories = data['categories'], counts = data['counts'], color = Category20[ncat]))
    fig = figure(x_range=data['categories'], y_range = (0,M+1), title=title, 
                 toolbar_location=None, tools="",x_axis_label=xlabel,y_axis_label=ylabel)
    fig.vbar(x= 'categories', top='counts', width=0.9, color='color',source=source)
    # fig.set_xlabel(xlabel)
    # fig.set_ylabel(ylabel)
    show(fig)
    
    
    
    
    
    
