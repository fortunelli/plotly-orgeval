import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Importing Dataset
Data = pd.read_csv('./Desktop/AllData-Nehuen.csv')

# Transforming from object to datetime
Data.DateHeure = pd.to_datetime(Data.DateHeure,format='%Y-%m-%d %H:%M:%S')


# Scatter plot
fig = go.Figure(data=go.Scattergl(
    x = Data.Na,
    y = Data.Cl,
    mode='markers+text',
    marker=dict(
        color=Data.PZ2,
        colorscale='Rainbow',
        line_width=1, showscale=True)
    ))



# Update plot sizing
fig.update_layout(
    width=700,
    height=500,
    autosize=False,
    margin=dict(t=50, b=1, l=100, r=1),
    # template="plotly_white",
)

# Add dropdown menus


# Determing tickers
tickers = []

for cols in Data:
    tickers.append(cols)

# Create dictionaries (dropdown menu options)
botones = []
for i in range(len(tickers)):
    a = dict(args=["visible", tickers[i]],
                    label=tickers[i],
                    method="update")
    botones.append(a)



# Add drowdowns
button_layer_1_height = 1.08

fig.update_layout(
    updatemenus=[
        dict(buttons= botones)
    ]
)

"""
fig.update_layout(
    annotations=[
        dict(text="X", x=0, xref="paper", y=1.06, yref="paper",
                             align="left", showarrow=False),
        dict(text="Y", x=0.25, xref="paper", y=1.07,
                             yref="paper", showarrow=False),
        dict(text="Colorbar", x=0.54, xref="paper", y=1.06, yref="paper",
                             showarrow=False)
    ])
"""

fig.show()