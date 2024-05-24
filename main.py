import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot
import auswerten
import pandas as pd
import plotly

tab1, tab2, tab3 = st.tabs(["EKG-Data", "Power-Data", "Auswertung"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

    df = read_my_csv()
    fig = make_plot(df)

    st.plotly_chart(fig)

with tab2:
    st.header("Power-Data")

with tab3:
    st.header("Auswertung")
    st.write("Die durchschnittliche Leistung beträgt:", auswerten.mittel)
    st.write("Die maximale Leistung beträgt:", auswerten.max)

    fig1 = auswerten.make_plot(auswerten.df1)
    st.plotly_chart(fig1)

    #Herzfrequenz-Zonen Angabe
    st.header("Herzfrequenz-Zonen:")
    st.write("Zone 1: 50-60% der maximalen Herzrate")
    st.write("Zone 2: 60-70% der maximalen Herzrate")
    st.write("Zone 3: 70-80% der maximalen Herzrate")
    st.write("Zone 4: 80-90% der maximalen Herzrate")
    st.write("Zone 5: 90-100% der maximalen Herzrate")
    st.write("")


    st.write("In den jeweiligen Zonen wurden folgende Zeiten verbracht:", auswerten.calculate_zone_time(auswerten.df2))
    #st.dataframe(data=auswerten.calculate_zone_time(auswerten.df2))
    st.write("Die durchschnittliche Leistung in den Zonen beträgt:", auswerten.calculate_zone_power(auswerten.df2))
    #st.dataframe(data=auswerten.calculate_zone_power(auswerten.df2))


    def calculate_zones(max_hr):
        zone_ranges = {
            "Zone 1": (0.5 * max_hr, 0.6 * max_hr),
            "Zone 2": (0.6 * max_hr, 0.7 * max_hr),
            "Zone 3": (0.7 * max_hr, 0.8 * max_hr),
            "Zone 4": (0.8 * max_hr, 0.9 * max_hr),
            "Zone 5": (0.9 * max_hr, max_hr)
        }
        return zone_ranges

    
    st.header("Herzfrequenz-Zonenrechner basierend auf der eingegebenen maximalen Herzfrequenz")

    max_hr = st.number_input("Geben Sie die maximale Herzfrequenz ein:", min_value=1, value=180)
    zone_ranges = calculate_zones(max_hr)

    zones_df = pd.DataFrame.from_dict(zone_ranges, orient='index', columns=['Untere Grenze', 'Obere Grenze'])
    
    st.write("### Herzfrequenz-Zonen:")
    st.dataframe(zones_df)
