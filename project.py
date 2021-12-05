import pandas as pd
import plotly.express as px


df = pd.read_csv("data3.csv")

p = px.scatter(df,x="date",y="cases",color ="country")

p.show()