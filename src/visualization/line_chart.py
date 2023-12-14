'''Script to produce line chart visualizations'''
import seaborn as sns
import matplotlib.pyplot as plt

def line_chart(data, x, y, title, xlabel, ylabel, color, figsize, style):
    '''Function to produce line chart visualizations'''
    sns.set_style(style)
    fig = sns.lineplot(x=x, y=y, data=data, color=color)
    fig.figure.set_size_inches(figsize)
    fig.set_title(title)
    fig.set_xlabel(xlabel)
    fig.set_ylabel(ylabel)
    plt.show()