import pandas as pd
import plotly.express as pe

df = pd.read_csv("covid-data.csv")

fig = pe.scatter(df,x= "Date",y= "Cases",color= "Country",size_max= 25)

fig.show()