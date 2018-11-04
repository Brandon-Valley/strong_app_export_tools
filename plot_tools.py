
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


def plot_single(title, filename, trace):    
#     fig.append_trace(trace)
    
#     fig['layout'].update(height=700, width=1500, title = title)
    
    plotly.offline.plot([trace], filename=filename, auto_open=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import main
if __name__ == '__main__':
    main.main()