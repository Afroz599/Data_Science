#Visualisation using seaborn
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
b=sns.load_dataset("flights")
print(b)
c=sns.get_dataset_names()
print(c)
#lineplot
print("lineplot")
sns.lineplot(data=b,
             x="passengers",
             y="year",
             errorbar=None)
plt.show()
#barplot
print("Bar plot")
sns.barplot(data=b,
            x="passengers",
            y="year",
            errorbar=None)
plt.show()
#Horizontal plot
print("Horizontal Plot")
sns.barplot(data=b,
            y="year",
            x="passengers",
            errorbar=None,
            orient="y")
plt.show()
#scatter plot
sns.scatterplot(data=b,x="year",y="passengers")
plt.show()
#heatmaps
sns.heatmap(b.pivot(index="year",columns="month",values="passengers"),annot=True)
#here annot give the value within the boxes
plt.show()
sns.heatmap(b.pivot(index="year",columns="month",values="passengers"),cmap="crest")
plt.show()
#Histogram
#Basic
sns.histplot(data=b,x="passengers")
plt.show()
#adding no.of bars
sns.histplot(data=b,x="passengers",bins=30)
plt.show()
#adding hue
sns.histplot(data=b,x="passengers",bins=30,hue="month")
plt.show()
#adding sub plots 
sns.histplot(data=b,x="passengers",bins=30,hue="month",multiple="stack")
plt.show()
sns.histplot(data=b,x="passengers",bins=30,hue="month",multiple="dodge")
plt.show()
sns.histplot(data=b,x="passengers",bins=30,hue="month",multiple="fill")
plt.show()
sns.histplot(data=b,x="passengers",bins=30,hue="month",multiple="layer")
plt.show()
#Box/violin
sns.boxplot(data=b,y="passengers",x="year")
plt.show()
sns.violinplot(data=b,x="passengers")
plt.show()