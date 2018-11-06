
import plotly
import plotly.graph_objs as go
import datetime as dt

from plotly import tools
import plotly.plotly as py


NEW_LINE = '<br>'


def default_trace(name, x, y, hover_info_l = []):
    if hover_info_l == []:
        trace = go.Scatter( name = name,
                            x    = x,
                            y    = y,
                            mode = 'lines+markers' )
    else:
        trace = go.Scatter( name = name,
                            x    = x,
                            y    = y,
                            mode = 'lines+markers',
                            text = hover_info_l,
                            hoverinfo = 'text' )
    return trace


def plot_single_trace(title, filename, trace):    

    plotly.offline.plot({"data": [trace],
                          "layout": go.Layout(title=title)}, filename=filename, auto_open=True)
    
    
def plot_trace_list(title, filename, trace_list):    

    plotly.offline.plot({"data": trace_list,
                          "layout": go.Layout(title=title)}, filename=filename, auto_open=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import main
if __name__ == '__main__':
    main.main()