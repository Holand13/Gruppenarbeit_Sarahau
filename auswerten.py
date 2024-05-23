#%%
import pandas as pd
import plotly
from read_pandas import make_plot
import plotly.express as px
import nbformat
import plotly.graph_objects as go
import streamlit as st

data = pd.read_csv("data/activities/activity.csv",delimiter=",")
data.head()
print(data.columns)
print(data.shape)

mittel= data.mean(numeric_only=True)
max= data["PowerOriginal"].max()

#%%
data["Time"] = data.index
#print(data["Time"])
df1 = data[["Time","PowerOriginal","HeartRate"]]

def make_plot(df):
    df_subset = df1.head(1803)
    fig1 = px.line(df_subset, x="Time", y="PowerOriginal", title='Leistung und Herzfrequenz über die Zeit')
    # Füge die Herzfrequenz als zweite Linie hinzu
    fig1.add_scatter(x=df_subset["Time"], y=df_subset["HeartRate"], mode='lines', name='HeartRate')

    return fig1

make_plot(df1)
#%%
# Teilen Sie die Aktivität in fünf Zonen mittels Herzfrequenz:
# Zone 1: 50-60% der Maximalen Herzrate
# Zone 2: 60-70% der maximalen Herzrate
# Zone 3: 70-80% der maximalen Herzrate
# Zone 4: 80-90% der maximalen Herzrate
# Zone 5: 90-100% der maximalen Herzrate

df2 = pd.DataFrame(data)
max_heart_rate = df2["HeartRate"].max(numeric_only=True)

# Berechnen Sie die Herzfrequenz-Zonen
zone_1 = [0.5 * max_heart_rate, 0.6 * max_heart_rate]
zone_2 = [0.6 * max_heart_rate, 0.7 * max_heart_rate]
zone_3 = [0.7 * max_heart_rate, 0.8 * max_heart_rate]
zone_4 = [0.8 * max_heart_rate, 0.9 * max_heart_rate]
zone_5 = [0.9 * max_heart_rate, max_heart_rate]

# Fügen Sie die Herzfrequenz-Zonen als neue Spalten hinzu
df2["HeartRateZone"] = pd.cut(df2["HeartRate"],
                             bins=[0, zone_1[1], zone_2[1], zone_3[1], zone_4[1], zone_5[1]],
                             labels=["Zone 1", "Zone 2", "Zone 3", "Zone 4", "Zone 5"],
                             include_lowest=True)

# Drucken Sie die neue Spalte HeartRateZone
print(df2[["HeartRate", "HeartRateZone"]])

#Erstelle eine Funktion die durch den input der maximalen Herzfrequenz die Zone ausgibt
def location(max_heart_rate):
    number = float(max_heart_rate)
    if number >= 93 and number <= zone_1[1]:
        return "Zone 1"
    elif number >= zone_2[0] and number < zone_2[1]:
        return "Zone 2"
    elif number >= zone_3[0] and number < zone_3[1]:
        return "Zone 3"
    elif number >= zone_4[0] and number < zone_4[1]:
        return "Zone 4"
    elif number >= zone_5[0] and number <= zone_5[1]:
        return "Zone 5"
    else:
        return "Keine gültige Zone"

#%%
#Zeigen Sie an, wie viel Zeit in welcher Zone verbracht wurde
def calculate_zone_time(df2):
    zone_time = df2.groupby("HeartRateZone")["Time"].sum()
    return zone_time

calculate_zone_time(df2)
# %%
