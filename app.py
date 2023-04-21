from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt
from pandas_datareader import data as pdr
import streamlit as st
import streamlit.components.v1 as com


st.set_page_config(
    page_title="Stock"
)  

    
end = dt.date.today()
start = end - dt.timedelta(days=3650)

st.title('Stock Market')

stocks = pd.read_csv('Output 2.csv')
stocks_list = stocks['Ticker'].values.tolist()

yf.pdr_override()
user_input = st.selectbox("Enter Stock Ticker", stocks_list, 0)
df = pdr.DataReader(user_input, start, end)
df = df.reset_index()
################################################################## Describing Data ############################################################
st.subheader(str(user_input) + ' from ' + str(start) + ' to ' + str(end))
st.write(df.describe())
################################################################### Data Insertion #########################################################
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
df.insert(3, "Moving average 100", ma100)
df.insert(4, "Moving average 200", ma200)
################################################################### Visulalizations #########################################################
st.subheader('Closing Price Vs Time Chart with 100 Moving Average')
fig = px.line(df, x=df.Date, y=['Close', 'Moving average 100'])
st.write(fig)
