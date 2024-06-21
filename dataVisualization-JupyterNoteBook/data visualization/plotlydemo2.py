# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:58:07 2019

@author: anilk
"""
print("Hello World!");

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


import pandas as pd
#import plotly.plotly as py

import plotly
import plotly.offline as py
import plotly.graph_objs as go

df = pd.read_csv('https://raw.githubusercontent.com/yankev/test/master/life-expectancy-per-GDP-2007.csv')

americas = df[(df.continent=='Americas')]
europe = df[(df.continent=='Europe')]
#create one graph
trace_comp0 = go.Scatter(
    x=americas.gdp_percap,
    y=americas.life_exp,
    mode='markers',
    marker=dict(size=12,
                line={"width":1},
                color="navy"
               ),
    name='Americas',
    text=americas.country,
    )
#create another graph
trace_comp1 = go.Scatter(
    x=europe.gdp_percap,
    y=europe.life_exp,
    mode='markers',
    marker=dict(size=12,
                line=dict(width=1),
                color="red"
               ),
    name='Europe',
    text=europe.country,
        )
    
    
    
    
data_comp = [trace_comp0, trace_comp1]
layout_comp = go.Layout(
    title='Life Expectancy v. Per Capita GDP, 2007',
    hovermode='closest',
    xaxis=dict(
        title='GDP per capita (2000 dollars)',
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Life Expectancy (years)',
        ticklen=5,
        gridwidth=2,
    ),
)
fig_comp = go.Figure(data=data_comp, layout=layout_comp)
py.offline.plot(fig_comp, filename='life-expectancy-per-GDP')
    
