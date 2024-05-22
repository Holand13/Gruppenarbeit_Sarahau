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
    fig1 = auswerten.make_plot(auswerten.df1)
    st.plotly_chart(fig1)

    max_heart_rate = st.number_input("Gib die maximale Herzfrequenz ein, um zu wissen in welcher Zone Sie sich befinden:")
    st.write("Sie befinden sich in Zone:", auswerten.location(float(max_heart_rate)))
