#To work with time-series data
import pandas as pd
import numpy as py
df=pd.DataFrame({
    'Date':pd.date_range(start='2025-01-01',periods=60),
    'value':py.random.randint(0,100,size=60)
})
#month/year value
a=df["Month/Year"]=df["Date"].dt.strftime("%m/%y")
b=df["Month/Year"]=df["Date"].dt.strftime("%b/%y")
#week/year base value
c=df["week/year"]=df["Date"].dt.strftime("%u/%y")
d=df.groupby("week/year")["value"].max()
e=df.groupby("week/year")["value"].agg(["mean","sum","std"])
print(a)
print(b)
print(c)
print(d)
print(e)