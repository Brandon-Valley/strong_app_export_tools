
import plotly
import plotly.graph_objs as go
import datetime as dt

from plotly import tools
import plotly.plotly as py





def default_trace(name, x, y):
    trace = go.Scatter( name = name,
                        x    = x,
                        y    = y,
                        mode = 'lines+markers' )
    return trace


def plot_single_trace(title, filename, trace):    

    plotly.offline.plot({"data": [trace],
                          "layout": go.Layout(title=title)}, filename=filename, auto_open=True)
    
    
def plot_trace_list(title, filename, trace_list):    

    plotly.offline.plot({"data": track_list,
                          "layout": go.Layout(title=title)}, filename=filename, auto_open=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import main
if __name__ == '__main__':
    main.main()