''' Script to produce calendar heatmaps '''
import calmap       # https://pythonhosted.org/calmap/
import matplotlib.pyplot as plt 
from visualization.plot import Plot 

class CalendarHeatmap(Plot):

    def show(data,figsize,title,year=None, how=u'sum', vmin=None, vmax=None, cmap=u'Reds', 
                        fillcolor=u'whitesmoke', linewidth=1, linecolor=None, 
                        daylabels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], 
                        dayticks=True, monthlabels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
                        monthticks=True, ax=None, **kwargs):
        plt.figure(figsize=figsize)
        calmap.yearplot(data, year, how, vmin, vmax, cmap, fillcolor, 
                        linewidth, linecolor, daylabels, dayticks, 
                        monthlabels, monthticks, ax, **kwargs)
        plt.title(title)
        plt.show()
        