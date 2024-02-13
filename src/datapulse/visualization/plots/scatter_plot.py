'''script to produce scatter plot visualizations'''
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from matplotlib.pyplot import show
from seaborn import scatterplot, set_style
from plot import Plot

class ScatterPlot(Plot):

    def show(data, x, y, title, xlabel, ylabel, color, figsize, style):
        '''Function to produce scatter plot visualizations'''
        set_style(style)
        fig = scatterplot(x=x, y=y, data=data, color=color)
        fig.figure.set_size_inches(figsize)
        fig.set_title(title)
        fig.set_xlabel(xlabel)
        fig.set_ylabel(ylabel)
        show()