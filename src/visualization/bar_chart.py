'''Script to produce bar chart visualizations'''
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import arange

def bar_chart(data, x, y, title, xlabel, ylabel, color, figsize, style):
    '''Function to produce bar chart visualizations'''
    sns.set_style(style)
    fig = sns.barplot(x=x, y=y, data=data, color=color)
    fig.figure.set_size_inches(figsize)
    fig.set_title(title)
    fig.set_xlabel(xlabel)
    fig.set_ylabel(ylabel)
    M = int(max(data['x']))+1
    m = int(min(data['x']))
    step = (M-m)/5
    fig.set_xticks(arange(m,M,step))
    plt.show()
    
    
    
    
    
    
