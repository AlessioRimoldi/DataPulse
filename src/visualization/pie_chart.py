''' Script to produce pie chart visualizations'''
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

def pie_chart(data,labels,title,figsize,style,radius=1,shadow = False):
    ''''''
    colors = plt.cm.get_cmap('hsv',len(set(labels)))
    color_list = [mcolors.rgb2hex(colors(i)) for i in range(colors.N)]
    sns.set_style(style)
    fig = plt.figure(figsize=figsize)
    plt.pie(data,labels=labels, colors=color_list, radius=radius, shadow= shadow)
    plt.title(title)
    plt.legend()
    plt.show()
    