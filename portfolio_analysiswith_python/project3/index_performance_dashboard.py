# importing libnaries
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import pandas.tseries.offsets as pd_offsets

# Pulling the tcikers from Wikipedia\
# tickers = pd.read_html('https://en.wikipedia.org/wiki/NASDAQ-100')[0]['Company'][0].Symbol
# tickers = tickers.tolist()

url = 'https://en.wikipedia.org/wiki/NASDAQ-100'
tables = pd.read_html(url)

# Access table 4 and the 'Ticker' column
tickers = tables[4]['Ticker'].tolist()


# We are going to use Streamlits's caching ability to cache the data
# This way streeamlit will not re-run the code every time we change the input
## We will use the @st.cache decorator to cache the data

@st.cache_data
def getdata():
    df = yf.download(tickers, start='2020-01-01', end='2024-01-01')
    df = df['Close']
    return df

df = getdata()

# Making the dashboard
st.title('S&P Performance Dashboard')
n = st.number_input('Please provide the performance period in months', min_value=1, max_value=24)

# return calculation
# We are simply subtratcing the previous month from the current user input
# df[:df.index[-1] - pd_offsets.DateOffset(months=3)]


def get_returns(df,n):
    previous_prices = df[:df.index[-1] - pd_offsets.DateOffset(months=3)].tail(1).squeeze()
    recent_prices = df.loc[df.index[-1]]
    ret_df = (recent_prices/ previous_prices) -1
    return previous_prices.name, ret_df # We are also returning the dates for the prices

date, ret_df = get_returns(df, n)

# date
# ret_df

winners, losers = ret_df.nlargest(10), ret_df.nsmallest(10)

# winners
# losers

# Adding headers for winners & losers
winners.name, losers.name = 'Winners', 'Losers'

st.table(winners)
st.table(losers)
winners.index

# Plotting the winners & losers
winnerpick = st.selectbox('Pick a winner to visualize', winners.index)
st.line_chart(df[winnerpick][date:])
loserspick = st.selectbox('Pick a loser to visualize', losers.index)
st.line_chart(df[loserspick][date:])


