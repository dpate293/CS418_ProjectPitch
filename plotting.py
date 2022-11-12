import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

temps = pd.read_csv('ChicagoTemps2021.csv', parse_dates=["datetime"])
complaints = pd.read_csv('CDPH_Environmental_Complaints.csv', parse_dates=["Modified Date"])

complaints.rename(columns={"Modified Date": "datetime"}, inplace = True)


df = pd.merge(temps, complaints, how="inner", on="datetime")

df.columns = [c.replace(' ', '_') for c in df.columns]

df["month"] = df["datetime"].dt.month

df = df.groupby(["month", "COMPLAINT_TYPE"]).COMPLAINT_TYPE.count().reset_index(name="count")

p = sns.barplot(data=df, x="month", y="count", hue="COMPLAINT_TYPE")
p.legend(bbox_to_anchor=(1.1, 1.1),title="Complaint Type", loc= "upper right")
p.set_ylabel("# of complaints")
p.set_xlabel("Month")
p.set_title("Number of complaints and their types per month (2021)")
plt.show()