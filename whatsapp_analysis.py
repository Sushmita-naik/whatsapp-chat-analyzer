import pandas as pd
import numpy as np
# to load the whatsapp chat text file
file=open("chat.txt",encoding="utf-8")
data=file.readlines()
df=pd.DataFrame(data,columns=["raw_message"])
print(df.shape)
df["raw_message"] = df["raw_message"].str.replace("<Media omitted>", "📷 Photo", regex=False)
print(df.head(50))
# to split date-time and messages
df[["date_time","message"]]=df["raw_message"].str.split("-",n=1,expand=True)
# separate date and time
df[["date","time"]]=df["date_time"].str.split(", ",n=1,expand=True)
# extract user and message
df[["user","message"]]=df["message"].str.split(":",n=1,expand=True)
# remove the system messages
df=df.dropna()
# to converts the dates as real datetimes objects
df["date"]=pd.to_datetime(df["date"],dayfirst=True,errors="coerce")
# count total messages
df.shape
# most active user
df["user"].value_counts()
# message length
df["message_length"]=df["message"].apply(len)
np.mean(df["message_length"])
df.to_csv("cleaned-whatsapp_chat.csv",index=False)

