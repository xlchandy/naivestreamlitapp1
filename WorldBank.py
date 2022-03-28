import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

India=pd.read_csv('World_Bank_India.csv',skiprows=4,index_col='Indicator Name',usecols=["Indicator Name","2010","2011","2012","2013","2014","2015","2016","2017","2018"])
India_Transposed=India.T
India_Transposed.reindex()


Chart1 = alt.Chart(India_Transposed.reset_index()).mark_bar().encode(
       alt.X('index:N',title='Year'),
       alt.Y('Fuel exports (% of merchandise exports):Q',title='Fuel Exports')
       ). properties(
                width=200,
                height=200,
                title='India Fuel Exports (Source - World Bank)')

Chart2 = alt.Chart(India_Transposed.reset_index()).mark_bar(color='Pink').encode(
       alt.X('index:N',title='Year'),
       alt.Y('International tourism, receipts for passenger transport items (current US$):Q',title='International tourism Receipts (US$)')
       ). properties(
                width=200,
                height=200,
                title='India Tourism Receipts (Source - World Bank)')
Chart3=Chart1|Chart2
st.set_page_config(page_title="World Bank Data for India",layout="wide",initial_sidebar_state="expanded")
st.title("World Bank Data for India")
st.altair_chart(Chart3)
