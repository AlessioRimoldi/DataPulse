'''Script to produce line chart visualizations'''
from bokeh.plotting import figure,show
from visualization.plot import Plot

class LineChart(Plot):

    def show(data, title = '', xlabel = '', ylabel = '', figsize = (16,9), 
                background_fill_color = '#ffffff', background_fill_alpha = 1.0,
                    line_colors = [], line_widths = []
                ):
        '''Function to produce line chart visualizations'''
        fig = figure(title=title, x_axis_label=xlabel, y_axis_label=ylabel, 
                    aspect_ratio = figsize[0]/figsize[1],
                    background_fill_color=background_fill_color, 
                    background_fill_alpha=background_fill_alpha)
        ys = list(data.columns)
        ys.remove("x")
        i = 0
        for y in ys:
            fig.line(data['x'], data[y], legend_label=ys[i], line_width=line_widths[i],color = line_colors[i])
            i+=1
        show(fig)