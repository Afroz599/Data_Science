import pandas as pd
df1=pd.DataFrame({'ID':[1,2,3],'Name':['Jhon','Anna','Peter']})
df2=pd.DataFrame({'ID':[2,3,4],'Score':[85,90,95]})
df3=pd.DataFrame({'ID_column':[2,3,4],'Score':[85,98,95]})             
print(df1)
print(df2)
print(df3)
#now when we have to know the marks of student and know his name 
#so we have to join the 2 frames
#Merge
Inner=pd.merge(df1,df2,on="ID",how="inner")
print(Inner)
Left=pd.merge(df1,df2,on="ID",how="left")
print(Left)
Right=pd.merge(df1,df2,on="ID",how="right")
print(Right)
Outer=pd.merge(df1,df2,on="ID",how="outer")
print(Outer)
#lets merge based on two different columns from each table
h=pd.merge(df1,df3,left_on="ID",right_on="ID_column",how="outer")
print(h)
#JOIN
df1.join(df2,on="ID",lsuffix="left",rsuffix="right",how="inner")
df1_index=df1.set_index("ID")
df2_index=df2.set_index("ID")
df1_index.join(df2_index,how="outer")
#concat
pd.concat([df1,df2],axis=0,ignore_index=True)
pd.concat([df1,df2],axis=1)


