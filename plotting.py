import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

temps = pd.read_csv('ChicagoTemps2021.csv', parse_dates=["datetime"])
complaints = pd.read_csv('CDPH_Environmental_Complaints.csv', parse_dates=["Modified Date"])

complaints.rename(columns={"Modified Date": "datetime"}, inplace = True)

#COMPLAINTS VISUALIZATION

df = pd.merge(temps, complaints, how="inner", on="datetime")

df.columns = [c.replace(' ', '_') for c in df.columns]

df["month"] = df["datetime"].dt.month

df = df.groupby(["month", "COMPLAINT_TYPE"]).COMPLAINT_TYPE.count().reset_index(name="count")

#NOTE: If you want to see the complaints visualization, ONLY uncomment the code under

#p = sns.barplot(data=df, x="month", y="count", hue="COMPLAINT_TYPE")
#p.legend(bbox_to_anchor=(1.1, 1.1),title="Complaint Type", loc= "upper right")
#p.set_ylabel("# of complaints")
#p.set_xlabel("Month")
#p.set_title("Number of complaints and their types per month (2021)")
#plt.show()


#TEMPS VISUALIZATION

temps["month"] = temps["datetime"].dt.month

temps = temps.groupby("month").mean()

temps["month"] = temps.index

#NOTE: If you want to see the temps visualization, ONLY uncomment the code under

#t = sns.barplot(data=temps, x="month", y="temp")
#t.set_ylabel("Average Temperature (F)")
#t.set_xlabel("Month")
#t.set_title("Average temperatures for Chicago per month (2021)")
#plt.show()


#NOTE: If you want to see the temps vs complaints visualization, ONLY uncomment the code under

#df.reset_index(drop=True, inplace=True)
#temps.reset_index(drop=True, inplace=True)
#df = pd.merge(df, temps, how="inner", on="month")
#df = df[df["COMPLAINT_TYPE"].isin(["AIR POLLUTION WORK ORDER"])]

#s = sns.regplot(data=df, x="count", y="temp")
#s.set_ylabel("Temperature (F)")
#s.set_xlabel("Amount of Pollution Complaints")
#s.set_title("Temperature vs Amount of Pollution Complaints in Chicago (2021)")
#plt.show()