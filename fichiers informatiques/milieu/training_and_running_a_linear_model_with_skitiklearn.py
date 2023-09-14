import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model
#load the data
oecd_bli=pd.read_csv("oecd_bli_2015.csv",thousands=",")
gdp_per_capita=pd.read_csv("gdp_per_capita.csv",thousands=",",delimiter='\t',encoding='latin1',na_values='n/a')
#prepare the data
country_stats=prepare_country_stats(oecd_bli,gdp_per_capita)
x=np.c_[country_stats["GDP per capita"]]
y=np.c_[contry_stats["Life satisfaction"]]
#Visualize the data
country_stats.plot(kind="scatter",x="GDP per capita",y="Life satisfaction")
plt.show()
#select a linear model
model=sklearn.linear_model.LinearRegression()
#Train the model
model.fit(x,y)
#make a prediction for cyprus
X_new=[[22587]] #cyprus GDP per capita
print(model.predict(X_new))  #outputs [[5.96242338]]