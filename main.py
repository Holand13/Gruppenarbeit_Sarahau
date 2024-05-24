import streamlit as st
from read_pandas import read_my_csv
from read_pandas import make_plot
import auswerten

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
    st.write("Die Mittelwerte betragen:", auswerten.mittel)
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

    max_heart_rate = st.number_input("Gib die maximale Herzfrequenz ein, um zu wissen in welcher Zone Sie sich befinden:")
    st.write("Sie befinden sich in Zone:", auswerten.location(float(max_heart_rate)))

    #st.write("In den jeweiligen Zonen wurden folgende Zeiten verbracht:", auswerten.calculate_zone_time(auswerten.df2))
    #st.write("Die durchschnittliche Leistung in den Zonen beträgt:", auswerten.calculate_zone_power(auswerten.df2))
    st.dataframe(data=auswerten.calculate_zone_time(auswerten.df2))
    st.dataframe(data=auswerten.calculate_zone_power(auswerten.df2))