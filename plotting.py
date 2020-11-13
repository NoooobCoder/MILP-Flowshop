# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:41:53 2020

@author: 91824
"""

import plotly.figure_factory as ff
from datetime import datetime, timedelta
import seaborn as sns
import plotly.io as pio

pio.renderers.default='browser'

def get_df(m):
    df = []
    for i in m.jobs:
        for k in m.machines:
            s = convert_time_format(m.S[i,k].value)
            f = convert_time_format(m.S[i,k].value+m.T[i,k])
            df.append(dict(Task=k,Start=s,Finish=f,Resource=i))
    return df

def convert_time_format(t):
    dt = datetime.now()
    dt = dt+timedelta(minutes=t)
    return str(dt)
    
def get_colors(m):
    n = len(m.jobs)
    clrs = sns.color_palette('husl',n_colors=n)
    c = dict()
    for i in range(len(m.jobs)):
        c[m.jobs[i+1]] = clrs[i]
    return c
    

def plot_gantt(m):
    df = get_df(m)
    colors = get_colors(m)
    
    fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar=True,
                          group_tasks=True)
    fig.show()
    return 0

