import pandas as pd
import statsmodels.api as sm
data={
    'class':[1,2,3,4,5,6,7,8,9,10],
    'n.sec':[4,4,3,2,4,2,3,3,2,2],
    'n.stu':[80,80,60,80,40,20,60,70,20,20],
}
df=pd.DataFrame(data)
print(df)
data1={
    'Name':['Jhon','Anna','Peter','Linda','Maria','Daniel','Simon','Monica'],
    'Age':[28,24,35,32,90,42,22,15],
    'Country':['USA','UK','Australia','Germany','USA','Brazil','Germany','Portugal']
}
df=pd.DataFrame(data1)
print(df)
#in regression we deal with only the numeric values but as we dont  have numeric values we encode 
df["Country_encode"]=df["Country"].astype("category").cat.codes
print(df)
#we do have dependent and independent varibles in this regression analysis
df['Name_encode']=df['Name'].astype('category').cat.codes
x=df[['Country_encode','Name_encode']]
y=df['Age']
model=sm.OLS(y,x).fit()
print(model)
z=model.summary()
print(z)