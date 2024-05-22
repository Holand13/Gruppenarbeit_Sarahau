#%%
import pandas as pd
import plotly
from read_pandas import make_plot
import plotly.express as px
import nbformat
import plotly.graph_objects as go

#%%
data = pd.read_csv("data/activities/activity.csv",delimiter=",")
data.head()
print(data.columns)
print(data.shape)
print(data.mean(numeric_only=True))

print(data["PowerOriginal"].max())   
  

data["Time"] = data.index
#Printe die neue Spalte Time
print(data["Time"])

print

df = data[["Time","PowerOriginal","HeartRate"]]


#Erstelle ein px.line mit x Time und y PowerOriginal und HeartRate
def make_plot(df):

    # Erstellte einen Line Plot, der ersten 2000 Werte mit der Zeit aus der x-Achse
    df_subset = df.head(1803)
    
    # Erstelle eine Figur mit plotly.express
    fig = px.line(df_subset, x="Time", y="PowerOriginal", title='Leistung und Herzfrequenz über die Zeit')

    # Füge die Herzfrequenz als zweite Linie hinzu
    fig.add_scatter(x=df_subset["Time"], y=df_subset["HeartRate"], mode='lines', name='HeartRate')

    return fig

make_plot(df)
#%%
# Teilen Sie die Aktivität in fünf Zonen mittels Herzfrequenz:
# Zone 1: 50-60% der Maximalen Herzrate
# Zone 2: 60-70% der maximalen Herzrate
# Zone 3: 70-80% der maximalen Herzrate
# Zone 4: 80-90% der maximalen Herzrate
# Zone 5: 90-100% der maximalen Herzrate

# Berechnen Sie die maximale Herzfrequenz
df = pd.DataFrame(data)

# Berechnen Sie die maximale Herzfrequenz
max_heart_rate = df["HeartRate"].max(numeric_only=True)

# Berechnen Sie die Herzfrequenz-Zonen
zone_1 = [0.5 * max_heart_rate, 0.6 * max_heart_rate]
zone_2 = [0.6 * max_heart_rate, 0.7 * max_heart_rate]
zone_3 = [0.7 * max_heart_rate, 0.8 * max_heart_rate]
zone_4 = [0.8 * max_heart_rate, 0.9 * max_heart_rate]
zone_5 = [0.9 * max_heart_rate, max_heart_rate]

# Fügen Sie die Herzfrequenz-Zonen als neue Spalten hinzu
df["HeartRateZone"] = pd.cut(df["HeartRate"],
                             bins=[0, zone_1[1], zone_2[1], zone_3[1], zone_4[1], zone_5[1]],
                             labels=["Zone 1", "Zone 2", "Zone 3", "Zone 4", "Zone 5"],
                             include_lowest=True)

# Drucken Sie die neue Spalte HeartRateZone
print(df[["HeartRate", "HeartRateZone"]])






# %%
