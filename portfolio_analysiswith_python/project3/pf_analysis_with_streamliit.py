# importing libnaries
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#
st.title("Portfolio Analysis with Streamlit")
assets = st.text_input("Pick your assets (comma separated)", "AAPL, MSFT, GOOGL, AMZN, TSLA")
start = st.date_input("Pick a starting date for the analysis", value = pd.to_datetime("2022-01-01"))

# Fetching the data from y finannce
data = yf.download(assets, start=start)['Close']

# Calculating returns
ret_df = data.pct_change()
cum_ret = (ret_df +1).cumprod() -1
pf_cum_ret = cum_ret.mean(axis=1)

# pf_cum_ret

# defining benachmark
benchmark = yf.download('^GSPC', start = start)['Close']
benchmark_ret = benchmark.pct_change()
benchmark_dev = (benchmark_ret +1).cumprod() -1

# benchmark_dev

# Portfolio risk calculation
W = np.ones(len(ret_df.cov()))/len(ret_df.cov())
pf_std = (W.dot(ret_df.cov()).dot(W))** (1/2)


ret_df.cov()

st.subheader("Portfolio returns vs Index returns")

tog = pd.concat([benchmark_dev, pf_cum_ret],axis=1)
tog.columns = ['S&P 500 Performance', 'Portfolio Performance']

# Plotting the returns
st.line_chart(tog, width=700, height=500, use_container_width=True)

# Calculating portfolio risk vs beanchmark returns
st.subheader("Portfolio Risk:")
# pf_std

st.subheader("Benchmark Risk:")
bench_risk = benchmark_ret.std()
bench_risk

st.subheader("Portfolio Composition")
fig, ax = plt.subplots(facecolor='#123458')
ax.pie(W, labels = data.columns, autopct = '%1.1f%%', textprops={'color':'white'})
st.pyplot(fig)