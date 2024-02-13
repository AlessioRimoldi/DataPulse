'''Script to produce bar chart visualizations'''
import os,sys
parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent)

from  plot import Plot

from bokeh.plotting import figure,show
from bokeh.palettes import Category20
from bokeh.models import ColumnDataSource

class BarChart(Plot):

    def show(data, title = '', xlabel = '', ylabel = '', figsize = (16,9), sorted = False, background_fill_color = '#ffffff', background_fill_alpha = 1.0):
        '''Function to produce bar chart visualizations
        at the moment colors are supported up to 20 categories
        Args:
            data (dict): dictionary with the data to plot keys = ['counts','categories']
            title (str): title of the plot
            xlabel (str): label of the x axis
            ylabel (str): label of the y axis
            figsize (tuple): size of the figure
            sorted (bool): if True, the data will be sorted in descending order,
            background_fill_color (str): color of the background
            background_fill_alpha (float): alpha of the background
        '''
        ncat = len(data['category'])
        M = max(data['counts'])
        source = ColumnDataSource(data= dict(category = data['category'], counts = data['counts'], color = Category20[ncat]))
        fig = figure(x_range=data['category'], y_range = (0,M+1), title=title, 
                    toolbar_location=None, tools="",x_axis_label=xlabel,y_axis_label=ylabel,
                    aspect_ratio=figsize[0]/figsize[1],background_fill_color=background_fill_color,
                    background_fill_alpha=background_fill_alpha,
                    )
        fig.vbar(x= 'category', top='counts', width=0.9, color='color',source=source)
        show(fig)
    
    
    
    
    
    
