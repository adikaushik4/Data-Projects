## Importing libraries
import streamlit as st
import pandas as pd
import yfinance as yf


st.title("Adi's Finance Dashboard")
tickers = ["AAPL", "MSFT", "BTC-USD","ETH-USD" , "AMZN", "TSLA"]

dropdown = st.multiselect('Pick your assets', tickers)

start = st.date_input('Start', value= pd.to_datetime('2022-01-01'))
end = st.date_input('End', value = pd.to_datetime('2024-12-31'))

def relative_returns(data):
    rel_ret = data.pct_change()
    cum_ret = (1 + rel_ret).cumprod()-1
    cum_ret = cum_ret.fillna(0)
    return cum_ret

## Fetching data from Yahoo Finance
if len(dropdown) > 0:
    # data = yf.download(dropdown, start, end)['Close']
    df = relative_returns(yf.download(dropdown, start, end)['Close'])
    st.header("Relative Returns of {}".format(dropdown))
    st.line_chart(df)
