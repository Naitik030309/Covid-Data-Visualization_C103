import pandas as pd
import plotly.express as pe

df = pd.read_csv("covid-data.csv")

fig = pe.bar(df,x= "Date",y= "Cases",color= "Country")

fig.show()