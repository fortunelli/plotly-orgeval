import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Importing Dataset
Data = pd.read_csv('./Desktop/AllData-Nehuen.csv')

# Transforming from object to datetime
Data.DateHeure = pd.to_datetime(Data.DateHeure,format='%Y-%m-%d %H:%M:%S')

"""
# Determing colname
colname = []

for cols in Data:
    a = 'Data.' + cols
    colname.append(a)
"""

# Scatter plot

fig = go.Figure(data=go.Scattergl(
    x = Data['SO4/Na'],
    y = Data['Ca/Na'],
    mode='markers+text',
    marker=dict(
        color=Data.PZ2,
        colorscale='Rainbow',
        line_width=1, showscale=True)
    ))


# Determing tickers
tickers = []

for cols in Data:
    tickers.append(cols)

"""
def scaplot(ticker1, ticker2, ticker3):
    fig = go.Figure(data=go.Scattergl(
        x = Data.ticker1,
        y = Data.ticker2,
        mode='markers+text',
        marker=dict(
            color=Data.ticker3,
            colorscale='Rainbow',
            line_width=1, showscale=True)
    ))
return
"""


# Update plot sizing
fig.update_layout(
    width=1300,
    height=500,
    autosize=False,
    margin=dict(t=20, b=20, l=20, r=10),
    # template="plotly_white",
)

# Add dropdown menus
# Create dictionaries (dropdown menu options)
botones = []
for i in range(len(tickers)):
    a = dict(args=["visible", tickers[i]],
                    label=tickers[i],
                    method="update")
    botones.append(a)


# Add dropdowns

fig.update_layout(
    updatemenus=[
        # Dropdown menu X-axis
        dict(buttons=botones,
        x =1.5),

        # Dropdown menu Y-axis
        dict(buttons=botones,
        x=2,
        ),

        # Dropdown menu Z-axis
        dict(buttons=botones,
        x=2.5,
        )   
    ]
)

# Labels next to dropdown menu
fig.update_layout(
    annotations=[
        dict(text="X", x=1.25, y=0.98, xref="paper", yref="paper",
                             align="left", showarrow=False),
        dict(text="Y", x=1.75, y=0.98, xref="paper", 
                             yref="paper", showarrow=False),
        dict(text="Colorbar", x=2.27, y=0.98, xref="paper", yref="paper",
                             showarrow=False)
    ])

fig.show()


# .js-plotly-plot .plotly .modebar{left: 40%}