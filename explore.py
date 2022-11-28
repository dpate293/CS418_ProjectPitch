import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# read csv with dates

beachQual = pd.read_csv('Beach_Water_Quality_-_Automated_Sensors_-_2017_-_Water_Temperature.csv', parse_dates=["Measurement Timestamp"])

chicagoTemp = pd.read_csv('ChicagoTemps2021.csv', parse_dates=["datetime"])

complaints = pd.read_csv('CDPH_Environmental_Complaints.csv', parse_dates=["Modified Date"])

# have them have same column names
beachQual.rename(columns={"Measurement Timestamp": "datetime"}, inplace = True)

# get just date 
beachQaul = beachQual['datetime'].dt.date

# beach quality temp visualization per month because it is only one year
beachQual["month"] = beachQual["datetime"].dt.month

beachQual = beachQual.groupby("month").mean()

beachQual["month"] = beachQual.index

b = sns.barplot(data=beachQual, x="month", y= "Water Temperature")
b.set_xlabel("Month")
b.set_ylabel("Average Temperature in Celsius")
b.set_title("Temperatures of Ohio Street Beach from May to September")
# plt.show()

#min and max temp visualization per month
chicagoTemp["month"] = chicagoTemp["datetime"].dt.month

chicagoTemp = chicagoTemp.groupby("month").mean()

chicagoTemp["month"] = chicagoTemp.index

chicagoTemp = pd.melt(chicagoTemp, id_vars=["month"], value_vars=["tempmax", "tempmin"], var_name='Type', value_name="Temperature")

ct = sns.barplot(data=chicagoTemp, x="month", y="Temperature", hue="Type")
ct.set_xlabel("Month")
ct.set_ylabel("Temperature in Fahrenheit")
ct.set_title("Minimum and Max Temperature in Chicago per month in 2021")

# plt.show()
