#with the help of pandas library we can do many operations on the data 
#the basic is done by converting the data into series or dataframe
#this conversion is for the data manipulation, easy staticstics applying and more
#few operations like head,tail,describe,info,sort_values,groupby,query,shape
import pandas as pd
data=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(data)
print("Below is the data of voters in the division 9")
data={'Name':['Raju','Shiva','Rony','Monto','joseph','kavi','raman','shardhul','manan','kishore','hari','laxmi','aziba','shareefa','latifa','karishma'],
      'Age':[23,25,45,23,19,23,25,34,12,34,29,21,32,33,45,18],
      'Gender':['M','M','M','M','M','M','M','M','M','M','M','F','F','F','F','F']}
#changing data to dataframe
df=pd.DataFrame(data)
print(df)
#checking the first 5 tuples of data
H=df.head()
print(H)
#checking the last 5 tuples of data
T=df.tail()
print(T)
#to know the voters in this file
Q=df.query('Age>=18')
print(Q)
#to know the male voters
M=df.query('Gender=="M"') # query for string will work as ('attri=="str"')
print(M)
#to know the female voter
F=df.query('Gender=="F"')
print(F)
#to know who are not eligible to vote
N=df.query('Age<18')
print(N)
#to get statistics of the data
D=df.describe()
print(D)
#to get the data types of the program
I=df.info()
print(I)
#to sort values
S=df.sort_values('Age')
print(S)
#to group
G=df.groupby('Gender')
print(G)
#to know the number of rows & columns
S=df.shape
print(S)
#working with different types of files 
df.to_csv("dataframe.csv",index=False)
df.to_excel("dataframe.xlsx")
df.to_json("dataframe.json")
df.to_html("dataframe.html")
# ... (your existing pandas code)

import sqlite3 as sql

# Step 1: Connect and save DataFrame to database
conn = sql.connect('dataframe.db')
df.to_sql("voters", conn, if_exists='replace', index=False)
conn.close()

# Step 2: Reconnect to read from database
conn = sql.connect('dataframe.db')
retrive_df = pd.read_sql("SELECT * FROM voters", conn)
conn.close()

# Step 3: Print retrieved data
print("\nRetrieved data from database:")
print(retrive_df)
