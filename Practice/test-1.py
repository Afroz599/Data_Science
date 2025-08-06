import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import matplotlib.pyplot as plt
import geopandas as gpd
df=sm.datasets.get_rdataset('EuroEnergy','AER',cache=True).data
df.reset_index(inplace=True)
world=gpd.read_file(r"C:\Users\Asus\OneDrive\Desktop\Data_Science\ne_10m_admin_0_countries.shp")
world=world[world["CONTINENT"]=="Europe"]
world.columns=world.columns.str.lower()
#Data cleaning
df.rename(columns={"rownames":"country"},inplace=True)
df["country"].replace({"wGermany":"Germany","UK":"United Kingdom"},inplace=True)
bins=[-1,5000,30000,df["energy"].max()]
labels=["lower","medium","high"]
df["energy_category"]=pd.cut(df["energy"],bins=bins,labels=labels)
#combine data source
df=world.merge(df,left_on="name",right_on="country",how="left")
df=df[["name","energy","economy","geometry","energy_category"]]
df["energy"].fillna(0,inplace=True)
#Data Viz
fig,ax=plt.subplots(figsize=(10,10),dpi=300)
df.plot(ax=ax,column="energy",legend=True,cmap="crest")
ax.set_xlim(-15,35)
ax.set_ylim(32,72)
plt.show()
sns.barplot(data=df,y="economy",x="energy",estimator="mean")
plt.show()