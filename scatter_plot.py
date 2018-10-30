import cntk
import plotly as py
import plotly.graph_objs as go

import numpy as np

#x, y, z = np.random.multivariate_normal(np.array([0,0,0]), np.eye(3), 200).transpose()
x = [6, 9, 12, 15, 18, 21, 24, 27, 30, 33]
y = [500] * 10
z = [16.031254289210725, 15.208714527291558, 15.748302192973492, 14.747761385175243, 15.772085679081844, 16.352750927367822, 15.441187428949691, 15.103125534149871, 15.922154480675175, 16.03687067944525]
trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=12,
        line=dict(
            color='rgba(217, 217, 217, 0.14)',
            width=0.5
        ),
        opacity=0.8
    )
)
'''
x2, y2, z2 = np.random.multivariate_normal(np.array([0,0,0]), np.eye(3), 200).transpose()
trace2 = go.Scatter3d(
    x=x2,
    y=y2,
    z=z2,
    mode='markers',
    marker=dict(
        color='rgb(127, 127, 127)',
        size=12,
        symbol='circle',
        line=dict(
            color='rgb(204, 204, 204)',
            width=1
        ),
        opacity=0.9
    )
)'''
data = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)
fig = go.Figure(data=data, layout=layout)
py.offline.plot(fig, filename='simple-3d-scatter.html')
