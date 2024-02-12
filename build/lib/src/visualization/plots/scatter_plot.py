'''script to produce scatter plot visualizations'''
import matplotlib.pyplot as plt
import seaborn as sns
from visualization.plot import Plot

class ScatterPlot(Plot):

    def show(data, x, y, title, xlabel, ylabel, color, figsize, style):
        '''Function to produce scatter plot visualizations'''
        sns.set_style(style)
        fig = sns.scatterplot(x=x, y=y, data=data, color=color)
        fig.figure.set_size_inches(figsize)
        fig.set_title(title)
        fig.set_xlabel(xlabel)
        fig.set_ylabel(ylabel)
        plt.show()