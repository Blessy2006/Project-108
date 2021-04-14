import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import csv

Mob = pd.read_csv("Mobile.csv")

fig = ff.create_distplot([Mob["Avg Rating"].tolist()],["Avg Rating"],
        show_hist = False)
fig.show()        