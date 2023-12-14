'''Script to produce bar chart visualizations'''
import seaborn as sns
import matplotlib.pyplot as plt

def bar_chart(data, x, y, title, xlabel, ylabel, color, figsize, style):
    '''Function to produce bar chart visualizations'''
    sns.set_style(style)
    fig = sns.barplot(x=x, y=y, data=data, color=color)
    fig.figure.set_size_inches(figsize)
    fig.set_title(title)
    fig.set_xlabel(xlabel)
    fig.set_ylabel(ylabel)
    plt.show()
    
    
    
    
    
    
