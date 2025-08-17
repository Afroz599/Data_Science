#importing libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#loading data from url
url=r"C:\Users\Asus\OneDrive\Desktop\Data_Science\tested.csv"
#creating dataframe for manipulation
df=pd.read_csv(url)
print(df)
#checking for the null values
print(df.isna())
print(df.describe())
#the count of null values in each column
print(df.isna().sum())
print(df.fillna(0,inplace=True))
print(df.isna().sum())
#perfoming manipulations
print(df.groupby(['Survived','Sex']).size())
#using queries
print(df.head())
#to sort according to the gender
print(df.query('Sex=="female"and Survived==1'))
#to know the count of females who survived
print(df.query('Sex=="female"and Survived==1').shape[0])
#to know the count of male who lost life
print(df.query('Sex=="male"and Survived==0').shape[0])
#to know the count of female who lost life
print(df.query('Sex=="female"and Survived==0').shape[0])
# Filter only survived passengers
survived_df = df.query("Survived == 1")
# Count how many males and females survived
print(survived_df['Sex'].value_counts())
#visualisation
print(df.head())
sns.barplot(data=df,x="Age",y="Survived",errorbar=None)
plt.show()
sns.lineplot(data=df,x="Sex",y="Survived",errorbar=None)
plt.show()
sns.barplot(data=df, x='Pclass', y='Survived',errorbar=None)
plt.show()
sns.histplot(data=df,x='Age',bins=30,hue='Survived',multiple="stack")
plt.show()
pivot_data = df.pivot_table(index="Sex", columns="Survived", values="Age", aggfunc="mean")
sns.heatmap(pivot_data, cmap="crest", annot=True)
plt.title("Average Age by Sex and Survival")
plt.show()
