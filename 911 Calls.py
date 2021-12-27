#911 Calls Data Analytics Project

import numpy as np
import pandas as pd

#importing the data visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

#loading the dataset
df = pd.read_csv("911.csv")

#information about the dataset
print(df.info())

print("...........................................................................")

#top 5 zip codes for 911 calls
print(df['zip'].value_counts().head(5))

print("...........................................................................")

#top 5 townships for 911 calls
print(df['twp'].value_counts().head(5))

print("...........................................................................")

#no. of unique title codes
print(df['title'].nunique())

print("...........................................................................")

#creating a new feature called reason
def ans(x):
    return x.split(":")[0]

df['reason'] = df['title'].apply(ans) 

'''
alternatively:
df['title'].apply(lambda x: x.split(":")[0])
'''

#top 3 most common reason for a 911 call
print(df['reason'].value_counts().head(3))

print("...........................................................................")

#countplot for 911 calls based on reason
sns.countplot(x='reason', data=df, palette='viridis')
plt.show()

#converting the timeStamp column datatype from str to DateTime objects
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

#creating three new columns year, month, hour and day of week
df['year'] = df['timeStamp'].apply(lambda time: time.year)
df['month'] = df['timeStamp'].apply(lambda time: time.month)
df['hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['day of week'] = df['timeStamp'].apply(lambda time: time.dayofweek)
days = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['day of week'] = df['day of week'].map(days)

#countplot for day of week column based on the reason column
sns.countplot(x="day of week", data=df, hue="reason", palette="viridis")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

#countplot for month column based on the reason column
sns.countplot(x="month", data=df, hue="reason", palette="viridis")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

#the above graph indicates that the data for months september, october and november are missing
#therefore plotting a line chart
monthlyCount = df.groupby("month").count()
sns.lineplot(x='month', y='reason', data=monthlyCount)
plt.show()

#regression plot
sns.lmplot(x='month', y='reason', data=monthlyCount.reset_index())

#creating a new column called date
df['date'] = df['timeStamp'].apply(lambda dt: dt.date())

#distribution plot for date vs no. of 911 calls
dateWiseCalls = df.groupby('date').count()
sns.displot(x='date', y='reason', data=dateWiseCalls)
plt.show()


#line plot for date vs no. of 911 calls
df.groupby('date').count()['twp'].plot()
plt.tight_layout()



#line plots based on the reason of call
df[df['reason']=='Traffic'].groupby('date')['reason'].count().plot()
plt.tight_layout()
df[df['reason']=='Fire'].groupby('date')['reason'].count().plot()
plt.tight_layout()
df[df['reason']=='EMS'].groupby('date')['reason'].count().plot()
plt.tight_layout()





