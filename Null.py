#this is to handle the null values in the dataset provided it can help 
#to draw more effective analytics as these null values if not treated lead to 
#crash of analytics
import pandas as pd
import numpy as np
data={'player':['rohit sharma',np.nan,'virat','rahul','shreyas','surya','hardik','jadeja','axar','shami','bhumra','siraj','bhuvi'],
      'Runs':[23000,34000,353234,2456643,np.nan,73837,72837,83839,256173,25263,56272,35262,36372],
      'matches':[252,np.nan,2342,5245,np.nan,234,756,634,734,939,np.nan,839,263]}
df=pd.DataFrame(data)
print(df)
z=df.shape
print(z)
#to know whether null values exists or not in dataframe
a=df.isnull().values.any()
print(a)
#to know the count of null values
b=df.isnull().sum().sum()
print(b)
#to know the null values in the table format
c=df.isnull().sum()
print(c)
#to find the column in which it exists
d=df.isnull().any(axis=1)
print(d)
#to find the row in which it exists
d=df.isnull().any(axis=0)
print(d)
#we can deal with the null values by droping the rows or columns
#drop the rows/columns with null values
z=df.dropna(axis=1,how="all")
print(z)
df.dropna(axis=0,how="all")
df[df["player"].notnull()]
#fill the null values
z=df.fillna(0)
print(z)
y=df['player'].ffill()
print(y)
z=df['player'].bfill()
print(z)
m=df['player'].interpolate()
print(m)
#checking for different data types within the key-value pair of a dictionary
data={'players':['rohit sharma',np.nan,'virat',12.3,'shreyas','surya','hardik','jadeja','axar','shami','bhumra','siraj','bhuvi'],
      'Runs':[23000,34000,353234,2456643,np.nan,73837,72837,83839,256173,25263,56272,35262,36372],
      'matches':[252,np.nan,2342,5245,np.nan,234,756,634,734,939,np.nan,839,263]}
df=pd.DataFrame(data)
print(df)
#as you can see that in the player list we have different values that is str,nap.nan,int
#but it show as object 
n=df.dtypes
print(n)
#make use of 
p=df['players'].apply(type).value_counts()
print(p)
##Dealing with the outliners with differnt methods
#range
df["Range"]=df['Runs'].apply(lambda runs:'x' if runs<300000 or runs>1000000 else"")
b=df["Range"]
print(b)
#z-score
df["z-score"]=(df['Runs']-df['Runs'].mean())/df['Runs'].std()
df["z-score"]=df["z-score"].apply(lambda value:'x' if value<-2 or value>2 else"" )
o=df["z-score"]
print(o)
#IQR we have to find the lower bound as well as the upper bound
q1=df['Runs'].quantile(q=0.25)
q3=df['Runs'].quantile(q=0.75)
IQR=q3-q1
print(IQR)
lower_bound=q1-1.5*IQR
upper_bound=q3-1.5*IQR
df["IQR"]=df['Runs'].apply(lambda runs:'x' if runs<lower_bound or runs>upper_bound else"")
m=df["IQR"]
print(m)
#Isolation_map
from sklearn.ensemble import IsolationForest as IS
model=IS(contamination="auto")
df["Isolation Forest"]=model.fit_predict(df[["Runs"]])
p=df["Isolation Forest"]
print(p)
#Handling outliners
#deleting
x=df.query("Runs>30000 and Runs<100000")
print(x)
#correct
p=df["Runs"].apply(lambda runs:min(runs,65000))
print(p)
print(df)
#adding new values to dataframe
df['Ducks']=[2,4,6,3,8,9,2,9,3,4,2,4,4]
print(df)
df.to_csv("cricket.csv")