''' Script to produce pie chart visualizations'''
from bokeh.plotting import figure, show
from bokeh.palettes import Category20c
from bokeh.transform import cumsum
from math import pi
from visualization.plot import Plot

class PieChart(Plot):

    def show(data,title,figsize,radius=0.4,background_fill_color = '#ffffff', background_fill_alpha = 1.0):
        ''' Function to produce pie chart visualizations'''
        
        ncat = len(data['category'])
        data['colors'] = Category20c[ncat]
        data['angle'] = data['counts']/data['counts'].sum()*2*pi
        fig = figure(x_range = (-0.5,1.0),title = title, aspect_ratio = figsize[0]/figsize[1],
                    tools = 'hover', tooltips = '@category: @counts', toolbar_location = None,
                    background_fill_color = background_fill_color, background_fill_alpha = background_fill_alpha,
                    )
        fig.wedge(x=0, y=1, radius=radius, start_angle=cumsum('angle', include_zero=True), 
                end_angle=cumsum('angle'), fill_color = 'colors',line_color = background_fill_color, legend_field = 'category',
                source = data
                )    
        fig.axis.axis_label = None
        fig.axis.visible = False
        fig.grid.grid_line_color = None
        show(fig)
        
    def donout_chart():
        ''' Function to produce donout chart visualizations'''
        pass