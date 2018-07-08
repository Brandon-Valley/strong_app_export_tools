import plotly
import plotly.graph_objs as go

plotly.offline.plot({
    "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1]), go.Scatter(x=[12, 22, 32, 24], y=[4, 32, 22, 1])],
    "layout": go.Layout(title="hello world"),
}, auto_open=False, filename = 'folder1/test_file_111')
print('done!')